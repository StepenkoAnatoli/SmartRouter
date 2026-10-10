#!/usr/bin/env python3
"""Pilot close generator — per-task closure records + pilot totals for the Phase 4 report.

Reads the same observation ledger as tools/pilot_report.py and produces:
  * per-task closure: total spend, attempts (dispatched count), disposition
    (completed / blocked:cap / blocked:gate / unknown-profile / mixed), and
    whether caps were touched
  * pilot totals: tasks opened, tasks closed, dispatches, blocked dispositions,
    total spend vs. the §5 ceilings, and remaining headroom
  * dual output: machine-readable JSON (default stdout) and a markdown block
    paste-ready for docs/PHASE4_PILOT_REPORT.md (--markdown)

Reuses pilot_report.build_report's accounting validation; if the ledger has
gaps (cost mismatches, cap violations), closure rows are still produced but
flagged `accounting_gap: true` and the tool exits 1 — the §7 accounting rule
says gaps are disclosed, never silenced.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))
import pilot_report as pr  # noqa: E402

LEDGER_DEFAULT = REPO_ROOT / "tools" / "pilot_ledger.jsonl"
PRICES_PATH = REPO_ROOT / "tools" / "prices-2.json"


def disposition_of(task_row: dict) -> str:
    outcome = task_row.get("outcome", "")
    if outcome == "dispatched":
        return "completed"
    if isinstance(outcome, str) and outcome.startswith("blocked:"):
        return outcome  # blocked:cap / blocked:gate
    return outcome or "unknown"


def close_ledger(prices: dict, entries: List[dict]) -> dict:
    base = pr.build_report(prices, entries)
    caps = base["pilot"]["caps"]
    accounting_gap = base["accounting_status"] != "intact"

    closures: List[dict] = []
    for st in base["per_task"]:
        closed = {
            "task_id": st["task_id"],
            "attempts": st["attempts"],
            "spend_usd": round(st["spent"], 6),
            "disposition": disposition_of(st),
            "same_profile_repairs_credited": st.get("same_profile_repairs_credited", 0),
            "within_attempt_cap": st["attempts"] <= caps["max_attempts_per_task"],
            "within_cost_cap": st["spent"] <= caps["max_cost_per_task_usd"] + 1e-9,
            "accounting_gap": accounting_gap,
        }
        closures.append(closed)

    n_completed = sum(1 for c in closures if c["disposition"] == "completed")
    n_blocked = sum(1 for c in closures if c["disposition"].startswith("blocked"))
    pilot = {
        "tasks_closed": len(closures),
        "completed": n_completed,
        "blocked": n_blocked,
        "dispatches": base["pilot"]["dispatches"],
        "total_spend_usd": base["pilot"]["total_spend_usd"],
        "cap_task_usd": caps["max_cost_per_task_usd"],
        "cap_pilot_usd": caps["max_cost_per_pilot_usd"],
        "headroom_usd": round(caps["max_cost_per_pilot_usd"] - base["pilot"]["total_spend_usd"], 6),
        "within_pilot_cap": base["pilot"]["total_spend_usd"] <= caps["max_cost_per_pilot_usd"] + 1e-9,
        "accounting_status": base["accounting_status"],
        "problems": base["problems"],
    }
    return {
        "generator": "tools/pilot_close.py",
        "extends": "docs/PHASE4_PILOT_REPORT.md §2 (per-task evidence ledger)",
        "closures": closures,
        "pilot_totals": pilot,
        "decision_note": "No §7 decision is derived here; closures feed the Phase 4 report only.",
    }


def markdown(closure: dict) -> str:
    rows = ["| Task | Attempts | Spend (USD) | Disposition | Caps OK |",
            "| --- | --- | --- | --- | --- |"]
    for c in closure["closures"]:
        caps_ok = c["within_attempt_cap"] and c["within_cost_cap"]
        rows.append(f"| {c['task_id']} | {c['attempts']} | {c['spend_usd']:.6f} "
                    f"| {c['disposition']} | {'OK' if caps_ok else 'FLAG'} |")
    p = closure["pilot_totals"]
    rows.append("")
    rows.append(f"**Pilot totals**: {p['completed']}/{p['tasks_closed']} tasks completed, "
                f"{p['blocked']} blocked; {p['dispatches']} dispatches; "
                f"spend ${p['total_spend_usd']:.6f} of ${p['cap_pilot_usd']:.2f} "
                f"(headroom ${p['headroom_usd']:.6f}); accounting {p['accounting_status']}.")
    rows.append("_No section-7 decision is derived from this table; see the Phase 4 report's section-4 fields._")
    return "\n".join(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Close pilot tasks from the observation ledger")
    ap.add_argument("--ledger", default=str(LEDGER_DEFAULT))
    ap.add_argument("--prices", default=str(PRICES_PATH))
    ap.add_argument("--markdown", action="store_true", help="emit paste-ready markdown instead of JSON")
    args = ap.parse_args(argv)

    prices = json.loads(Path(args.prices).read_text(encoding="utf-8"))
    if prices.get("revision") != "prices-2":
        print("pilot_close: unexpected prices revision — stop", file=sys.stderr)
        return 2
    entries = pr.load_jsonl(Path(args.ledger))
    if not entries:
        print("pilot_close: ledger empty or missing — nothing to close", file=sys.stderr)
        return 2
    closure = close_ledger(prices, entries)
    if args.markdown:
        print(markdown(closure))
    else:
        print(json.dumps(closure, indent=2, sort_keys=True))
    return 0 if closure["pilot_totals"]["accounting_status"] == "intact" else 1


if __name__ == "__main__":
    sys.exit(main())
