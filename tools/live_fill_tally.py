#!/usr/bin/env python3
"""Tally the live-fill sheet against the §8 sampling plan.

Reads tools/live_fill_sheet.json and prints:
  * per-cell: slots recorded / repeats per task / filled?
  * per-arm: observations recorded vs the 20/arm target
  * pilot-level: cells filled, observations recorded, cells remaining

Exit codes: 0 = tally printed (sheet state is honest, however empty);
1 = integrity violation (an observation marked filled but carrying
'not_measured' fields, or a filled arm under target) — never silence a
lie; 2 = sheet missing/corrupt.

This tool never edits the sheet. Record observations by editing
live_fill_sheet.json's slots (or the CSV)-> keep task_id/ts/profile/tokens/
cost/latency from the real dispatch's ledger line only.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict

NOT_MEASURED = "not_measured"
MEASURED_REQUIRED = ("ts", "profile_dispatched", "input_tokens", "output_tokens",
                     "cost_usd", "latency_s", "outcome", "task_id")


def check_integrity(sheet: dict) -> list:
    problems = []
    for cell_id, c in sheet["cells"].items():
        for obs in c["observations"]:
            marked = all(obs.get(k) != NOT_MEASURED for k in MEASURED_REQUIRED)
            if marked and not c.get("filled"):
                continue  # record exists but cell not yet marked filled: fine mid-fill
            if c.get("filled") and not marked:
                problems.append(f"{cell_id} slot {obs.get('slot')}: cell says filled "
                                "but this observation still has not_measured fields")
            if obs.get("accounting_intact") is False and c.get("filled"):
                problems.append(f"{cell_id}: filled with accounting_intact=false "
                                "(§8 completion rule violated)")
        n = sum(1 for obs in c["observations"]
                if all(obs.get(k) != NOT_MEASURED for k in MEASURED_REQUIRED))
        c["_recorded"] = n
    return problems


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Tally live-fill sheet vs §8 plan")
    ap.add_argument("--sheet", default=str(Path(__file__).resolve().parent / "live_fill_sheet.json"))
    args = ap.parse_args(argv)

    p = Path(args.sheet)
    if not p.is_file():
        print(f"live_fill_tally: sheet missing at {p} — run gen_live_fill_sheet.py", file=SystemExit and __import__("sys").stderr)
        return 2
    try:
        sheet = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"live_fill_tally: corrupt sheet: {e}", file=__import__("sys").stderr)
        return 2

    problems = check_integrity(sheet)

    per_arm: Dict[str, int] = {arm: 0 for arm in sheet["arms"]}
    cells_filled = 0
    print(f"{'cell':6} {'recorded':>8} /{sheet['repeats_per_task'] * len(sheet['cells']) // len(sheet['cells'])} {'filled':>6}")
    for cell_id in sorted(sheet["cells"]):
        c = sheet["cells"][cell_id]
        n = c.get("_recorded", 0)
        per_arm[c["arm"]] += n
        tag = "yes" if c.get("filled") else "no"
        cells_filled += 1 if c.get("filled") else 0
        print(f"{cell_id:6} {n:>8} {tag:>6}")
    recorded = sum(per_arm.values())
    print()
    for arm, n in per_arm.items():
        target = sheet["observations_per_arm_target"]
        status = "OK" if n >= target else f"{target - n} to go"
        print(f"arm {arm}: {n}/{target} observations ({status})")
    print(f"\ncells filled: {cells_filled}/{len(sheet['cells'])} · "
          f"observations recorded: {recorded}/{target * len(per_arm)}")

    if problems:
        print("\nINTEGRITY VIOLATIONS:", file=__import__("sys").stderr)
        for pr_ in problems:
            print("  -", pr_, file=__import__("sys").stderr)
        return 1
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
