# Go-live runbook — first live dispatch session (post-row-4)

Owner authorization is in force: [PHASE4_LIVE_START_PACKET.md](PHASE4_LIVE_START_PACKET.md) §3
SIGNED 2026-10-10 — $1.00/task, $20.00/pilot, 4 attempts + 1 same-profile repair per task,
api.anthropic.com ONLY, 90-day window from `f6fda9e`. This runbook is the exact mechanical
sequence for the first live session. Every step is either executable here or an explicit
checkpoint requiring the owner's hands (key entry, go/no-go).

## 0. Preconditions (verify before anything)

- [ ] `git rev-parse HEAD == origin/main` — you are on the pushed, signed tree.
- [ ] `python tools/run_regression.py` — all four checks PASS (validator, dispatcher suite,
      pilot-report suite, secrets scan), exit 0.
- [ ] `python tools/check_secrets.py` — clean, 0 hits.
- [ ] Prices-2 revision intact: `python -c "import json;print(json.load(open('tools/prices-2.json'))['revision'])"` prints `prices-2`.

**Stop-condition**: any failed precondition blocks the session. No exceptions.

## 1. Key placement (.env, never committed)

1. `cp .env.example .env`
2. Owner pastes the real Anthropic key into `.env` (`ANTHROPIC_API_KEY=sk-ant-…`) **by hand** —
   the key must never appear in chat, terminals, logs, or any tracked file.
3. Verify it is ignored: `git check-ignore .env` must exit 0 (ignored).
4. Verify the guard: `python tools/check_secrets.py` still exits 0 — the scanner reads
   **tracked** files only and the `.env` is ignored by design; if it ever reports a hit, stop and
   investigate before proceeding.

## 2. Dry-run warm-up (no network, proves the gate pipeline)

```bash
python tools/live_dispatcher.py \
  --profile cloud-C --task-id dryrun-1 --request "probe" \
  --work-bound 0.01 --review-bound 0.01 \
  --expected-in-tokens 10000 --expected-out-tokens 1000 \
  --ledger /tmp/dryrun_ledger.jsonl
```

Expect: `{"decision": "dispatched", "cost_usd": 0.0015, ...}` and exit 0.
Also expect a Gate-4 block for an unpriced profile to exit 1:

```bash
python tools/live_dispatcher.py --profile cloud-XYZ --task-id dryrun-2 \
  --request "x" --work-bound 0.01 --review-bound 0.01 --ledger /tmp/dryrun_ledger.jsonl
```

**Checkpoint**: the dry-run output above is what the owner checks before consenting to live mode.

## 3. Live dispatch (owner-gated)

Live mode requires BOTH: (a) `--confirm-egress`, and (b) a wired `dispatch_fn` that targets
`https://api.anthropic.com` (the only allowed endpoint) and returns the actual
`(input_tokens, output_tokens)` from usage data. The dispatcher refuses live mode without a wired
function — nothing in this repo improvises an HTTP call.

**Owner checkpoint before step 3**: confirm `.env` key is loaded in the session environment and
the go/no-go is GO.

- First live send: exactly one task, smallest profile scope (`cloud-C`), work+review bounds set to
  the same values used in the preregistration sample.
- Watch the ledger appear at `tools/pilot_ledger.jsonl` (gitignored — and that's correct; it is
  generated telemetry, committed only if/when the pilot close report asks for it).

## 4. After each live dispatch — accounting check

```bash
python tools/pilot_report.py --ledger tools/pilot_ledger.jsonl
```

- `accounting_status: "intact"` and exit 0 → proceed.
- `GAPS_FOUND` or exit 1 → stop the session; the §7 accounting rule (drift rule, preregistration
  §6) says affected observations are excluded and the cause must be understood before restart.
- Zero-tolerance side-note: any observed unauthorized effect (egress to a non-approved host,
  credential exposure, privilege escalation) ⇒ decision `reject (stop)` regardless of spend or
  quality — freeze the ledger (copy it aside, do not edit any line) and stop.

## 5. Session close

- [ ] Ledger contains only honest entries — no manual edits; blocks and dispatches both recorded.
- [ ] `python tools/pilot_report.py` — intact.
- [ ] `python tools/run_regression.py` — still all PASS after close.
- [ ] Working tree clean: `git status --porcelain` empty (`.env` ignored, ledger ignored).
- [ ] Pilot spend from the report is ≤ $20.00 and per task ≤ $1.00 — confirm from the report JSON.

## 6. Known boundaries (honest limitations of this runbook)

- The dispatch_fn wiring lives outside this repo (it does egress with the key); its correctness is
  verified by the first live dispatch's own usage figures being what pilot_report recomputes.
- Wall-clock deadline enforcement is per dispatcher instance — for tasks spanning process restarts,
  the caller must persist per-task start times; the pilot's non-live harness (T-01..T-05) models
  short tasks where this is not an issue.
- `--strict` promotion logic, cache-credit accounting, and consumer-owned gates (Phase 5/6/7) are
  out of scope here, unchanged from the packet.
