#!/usr/bin/env python3
"""Tests for tools/task_crosscheck.py — persisted state vs. ledger reconciliation.

Covers the item-16 guarantee: a mid-restart crash that loses a state-store save
must surface as an explicit finding at close, never as silent under-report.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
import task_crosscheck as tc  # noqa: E402

PRICES = json.loads((REPO / "tools" / "prices-2.json").read_text(encoding="utf-8"))


def ledger_entry(tid, pid, dec, in_t, out_t, cost):
    return {"ts": 0.0, "task_id": tid, "attempt_no": 1, "profile_id": pid,
            "input_tokens": in_t, "output_tokens": out_t, "cost_usd": cost,
            "decision": dec, "reason": "test"}


def state_doc(tid, attempts, spent):
    return {"task_id": tid, "attempts": attempts, "spent": spent,
            "started": 0.0, "repairs": 0, "last_profile": "cloud-C"}


class Crosscheck(unittest.TestCase):

    def test_consistent_state_and_ledger(self):
        with tempfile.TemporaryDirectory() as td:
            sd = Path(td) / "state"
            sd.mkdir()
            (sd / "T1.json").write_text(json.dumps(state_doc("T1", 2, 0.003)), encoding="utf-8")
            entries = [ledger_entry("T1", "cloud-C", "dispatched", 10_000, 1_000, 0.0015),
                       ledger_entry("T1", "cloud-C", "dispatched", 10_000, 1_000, 0.0015)]
            r = tc.check(sd, PRICES, entries)
            self.assertTrue(r["consistent"], r["findings"])
            self.assertEqual(r["findings"], [])

    def test_state_below_ledger_spend_flagged_as_crash_underreport(self):
        with tempfile.TemporaryDirectory() as td:
            sd = Path(td) / "state"
            sd.mkdir()
            # ledger saw 2 dispatches ($0.003); state only persisted 1 ($0.0015)
            (sd / "T1.json").write_text(json.dumps(state_doc("T1", 1, 0.0015)), encoding="utf-8")
            entries = [ledger_entry("T1", "cloud-C", "dispatched", 10_000, 1_000, 0.0015),
                       ledger_entry("T1", "cloud-C", "dispatched", 10_000, 1_000, 0.0015)]
            r = tc.check(sd, PRICES, entries)
            self.assertFalse(r["consistent"])
            kinds = {f["kind"] for f in r["findings"]}
            self.assertIn("spend-under-report", kinds)
            self.assertIn("attempts-under-report", kinds)

    def test_missing_state_for_dispatched_task_flagged(self):
        with tempfile.TemporaryDirectory() as td:
            sd = Path(td) / "state"
            sd.mkdir()
            entries = [ledger_entry("T9", "cloud-C", "dispatched", 10_000, 1_000, 0.0015)]
            r = tc.check(sd, PRICES, entries)
            self.assertFalse(r["consistent"])
            self.assertEqual(r["findings"][0]["kind"], "state-missing")

    def test_state_only_task_is_not_a_finding(self):
        # a blocked-only task exists in state but never reached the ledger with spend:
        # ledger records the block (attempts 0, spent 0) — legal, must NOT flag.
        with tempfile.TemporaryDirectory() as td:
            sd = Path(td) / "state"
            sd.mkdir()
            (sd / "T2.json").write_text(json.dumps(state_doc("T2", 0, 0.0)), encoding="utf-8")
            entries = [ledger_entry("T2", "cloud-C", "blocked-cost-cap", 0, 0, 0.0)]
            r = tc.check(sd, PRICES, entries)
            self.assertTrue(r["consistent"], r["findings"])

    def test_state_above_ledger_is_legal_no_finding(self):
        # blocked attempts live in state but produce no ledger cost line:
        with tempfile.TemporaryDirectory() as td:
            sd = Path(td) / "state"
            sd.mkdir()
            (sd / "T3.json").write_text(json.dumps(state_doc("T3", 3, 0.003)), encoding="utf-8")
            entries = [ledger_entry("T3", "cloud-C", "dispatched", 10_000, 1_000, 0.0015)]
            r = tc.check(sd, PRICES, entries)
            self.assertTrue(r["consistent"], r["findings"])

    def test_main_exit_codes(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            sd = tmp / "state"
            sd.mkdir()
            led = tmp / "led.jsonl"
            led.write_text(json.dumps(ledger_entry("T1", "cloud-C", "dispatched", 10_000, 1_000, 0.0015)) + "\n",
                           encoding="utf-8")
            prices = str(REPO / "tools" / "prices-2.json")
            # finding -> exit 1
            self.assertEqual(tc.main(["--state-dir", str(sd), "--ledger", str(led), "--prices", prices]), 1)
            # consistent -> exit 0
            (sd / "T1.json").write_text(json.dumps(state_doc("T1", 1, 0.0015)), encoding="utf-8")
            self.assertEqual(tc.main(["--state-dir", str(sd), "--ledger", str(led), "--prices", prices]), 0)
            # missing ledger -> exit 2
            self.assertEqual(tc.main(["--state-dir", str(sd), "--ledger", str(tmp / "nope.jsonl"),
                                      "--prices", prices]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
