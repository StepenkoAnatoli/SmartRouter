#!/usr/bin/env python3
"""Tests for tools/arm_matrix.py — 4×5 coverage, evidence quality, determinism."""
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("am", TOOLS / "arm_matrix.py")
am = importlib.util.module_from_spec(spec)
spec.loader.exec_module(am)


class ArmMatrix(unittest.TestCase):

    def setUp(self):
        self.rep = am.build_matrix()

    def test_20_cells(self):
        self.assertEqual(len(self.rep["cells"]), 20)
        self.assertEqual(self.rep["coverage"]["complete"], True)

    def test_every_arm_x_task_pair(self):
        for arm in ("A", "B", "C", "D"):
            for tid in ("T-01", "T-02", "T-03", "T-04", "T-05"):
                self.assertIn(f"{arm}|{tid}", self.rep["cells"],
                              f"missing cell {arm}|{tid}")

    def test_evidence_non_empty(self):
        for key, cell in self.rep["cells"].items():
            self.assertTrue(cell["evidence"].strip(), f"empty evidence in {key}")
            self.assertTrue(cell["observed"], f"empty observed in {key}")

    def test_direct_arms_resolve_expected_profiles(self):
        for tid in ("T-01", "T-02", "T-03", "T-04", "T-05"):
            cat = self.rep["cells"][f"A|{tid}"]["task_category"]
            self.assertEqual(self.rep["cells"][f"A|{tid}"]["observed"], am.STRONG[cat])
            self.assertEqual(self.rep["cells"][f"B|{tid}"]["observed"], am.CHEAP[cat])

    def test_C_arm_goes_through_choose_route(self):
        # deterministic selector must produce the same resolution every run
        r1 = am.cell_C("typo")
        r2 = am.cell_C("typo")
        self.assertEqual(r1["observed"], r2["observed"])

    def test_D_arm_passthrough_gate_runner(self):
        # resolved profile must be one of the four fixture profile ids
        for tid in ("T-01", "T-02", "T-03", "T-04", "T-05"):
            obs = self.rep["cells"][f"D|{tid}"]["observed"]
            import re as _re
            m = _re.match(r"route='(direct|delegate|recommend-escalation|blocked)' resolved='([A-Za-z\-]+)' rejects=", obs)
            self.assertIsNotNone(m, f"unexpected arm-D observation format: {obs!r}")
            self.assertIn(m.group(2), ("local-L", "cloud-S", "cloud-C", "cloud-X"),
                          f"resolved profile not a fixture profile: {obs!r}")

    def test_accounting_note_present(self):
        self.assertIn("labels, not measurements", self.rep["accounting_note"])
        self.assertIn("$0.00", self.rep["accounting_note"])

    def test_decision_note_present_and_neutral(self):
        self.assertIn("No §7 decision", self.rep["decision_note"])

    def test_main_writes_and_returns_0(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "m.json"
            rc = am.main(["--out", str(p)])
            self.assertEqual(rc, 0)
            data = p.read_text(encoding="utf-8")
            self.assertIn("T-01", data)
            self.assertIn("arm-D", data or "\"arm\": \"D\"")

    def test_capped_cell_rule_respected(self):
        # R-D cell coverage must never claim live spend
        for cell in self.rep["cells"].values():
            self.assertNotIn("live", cell["evidence"].lower().replace("non-live", "").replace("live-model", ""),
                             f"cell may not claim live scope: {cell['evidence'][:80]}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
