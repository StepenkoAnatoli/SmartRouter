#!/usr/bin/env python3
"""Cross-checker: per-task persisted state vs. the observation ledger.

Item-16 guarantee: a mid-restart crash (dispatcher killed between the ledger
append and the state-store save, or vice versa) must not let task spend go
under-reported at close. This tool compares, for every task in either source:

  * ledger view   — what pilot_report derived from the dispatched lines
  * state view    — what the task store says (attempts, spent)

Refusal rules (exit 1, findings printed — never silenced):
  * state.spent < ledger.spent            → crash lost spend (under-report)
  * state.attempts < ledger attempts      → same, in attempt space
  * state.task absent but ledger has dispatched lines for it → lost state
  * state.attempts > ledger attempts      → legal (blocked attempts are
    state-only — blocks never append a cost ledger line), no finding.

Exit 0 with `consistent: true` when every check holds; exit 2 on missing
state dir or empty ledger (same convention as pilot_report).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))
import pilot_report as pr  # noqa: E402
from task_persistence import _sanitize  # noqa: E402


def state_view(state_dir: Path) -> Dict[str, dict]:
    out: Dict[str, dict] = {}
    if not state_dir.is_dir():
        return out
    for p in sorted(state_dir.glob("*.json")):
        try:
            doc = json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue  # corrupt state is the store's absent-fallback; not a mismatch
        if isinstance(doc, dict) and "task_id" in doc:
            out[doc["task_id"]] = doc
    return out


def ledger_view(prices: dict, entries: List[dict]) -> Dict[str, dict]:
    base = pr.build_report(prices, entries)
    return {row["task_id"]: row for row in base["per_task"]}


def check(state_dir: Path, prices: dict, entries: List[dict]) -> dict:
    sv = state_view(state_dir)
    lv = ledger_view(prices, entries)
    findings: List[dict] = []

    for task_id, lrow in sorted(lv.items()):
        l_attempts = lrow.get("attempts", 0)
        l_spent = lrow.get("spent", 0.0)
        if l_attempts == 0 and l_spent == 0.0:
            continue  # blocked-only task: no ledger spend to reconcile
        st = sv.get(task_id)
        if st is None:
            # maybe the file exists under the sanitized id but with a different task_id field
            fallback = state_view_file_guess(state_dir, task_id)
            st = fallback
        if st is None:
            findings.append({
                "task_id": task_id, "kind": "state-missing",
                "detail": f"ledger has {l_attempts} dispatched attempt(s) / ${l_spent:.6f} "
                          "but no persisted state file — restart crash lost state",
            })
            continue
        if st.get("spent", 0.0) < l_spent - 1e-9:
            findings.append({
                "task_id": task_id, "kind": "spend-under-report",
                "detail": f"state says ${st.get('spent', 0.0):.6f} < ledger ${l_spent:.6f} "
                          "— dispatch recorded but counters not persisted",
            })
        if st.get("attempts", 0) < l_attempts:
            findings.append({
                "task_id": task_id, "kind": "attempts-under-report",
                "detail": f"state says {st.get('attempts', 0)} attempts < ledger {l_attempts}",
            })

    return {"consistent": not findings, "findings": findings,
            "tasks_in_state": sorted(sv), "tasks_in_ledger": sorted(lv)}


def state_view_file_guess(state_dir: Path, task_id: str):
    p = state_dir / f"{_sanitize(task_id)}.json"
    if not p.is_file():
        return None
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    return doc if isinstance(doc, dict) and doc.get("task_id") == task_id else None


def main(argv: List[str] = None) -> int:
    ap = argparse.ArgumentParser(description="Cross-check persisted task state against the pilot ledger")
    ap.add_argument("--state-dir", default=str(REPO_ROOT / "tools" / "task_state"))
    ap.add_argument("--ledger", default=str(REPO_ROOT / "tools" / "pilot_ledger.jsonl"))
    ap.add_argument("--prices", default=str(REPO_ROOT / "tools" / "prices-2.json"))
    args = ap.parse_args(argv)

    prices = json.loads(Path(args.prices).read_text(encoding="utf-8"))
    if prices.get("revision") != "prices-2":
        print("task_crosscheck: unexpected prices revision — stop", file=sys.stderr)
        return 2
    ld = Path(args.ledger)
    if not ld.is_file():
        print(f"task_crosscheck: ledger missing at {ld} — nothing to check", file=sys.stderr)
        return 2
    entries = pr.load_jsonl(ld)
    if not entries:
        print("task_crosscheck: ledger is empty — nothing to check", file=sys.stderr)
        return 2

    result = check(Path(args.state_dir), prices, entries)
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["findings"]:
        print("task_crosscheck: FINDINGS FOUND — investigate before close (§7 drift rule)",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
