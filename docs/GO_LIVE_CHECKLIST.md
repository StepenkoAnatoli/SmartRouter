# Go-live one-pager — print this, drive the session with it

> Condensed from [GO_LIVE_RUNBOOK.md](GO_LIVE_RUNBOOK.md). If any box fails: **stop, fix,
> re-run the box.** Full details live in the runbook, not here.

## □ 0. PREFLIGHT (≈1 min, no key needed)

```
□ git rev-parse HEAD == ls-remote origin main        → parity
□ python tools/run_regression.py                     → 10 checks, exit 0
□ python tools/check_secrets.py                      → clean, 0 hits
□ git config core.hooksPath                          → .githooks
□ mkdir -p tools/task_state                          → state dir exists
□ python tools/live_dispatcher.py --live … (no .env) → exit 2, "dispatch-refused", no HTTP
```

## □ 1. KEY PLACEMENT (OWNER hands)

```
□ cp .env.example .env
□ paste real ANTHROPIC_API_KEY=sk-ant-… into .env BY HAND
□ git check-ignore .env        → ignored (exit 0)
□ python tools/check_secrets.py → still clean
```

## □ 2. DRY-RUN (no network)

```
□ cloud-C dry run → {"decision":"dispatched","cost_usd":0.0015}, exit 0
□ cloud-XYZ dry run → "unknown-profile", exit 1
```

## □ 3. LIVE SEND (OWNER: GO) — one task, cloud-C

```bash
python tools/live_dispatcher.py \
  --live --confirm-egress \
  --profile cloud-C \
  --task-id live-001 --request "<task prompt>" \
  --work-bound 0.01 --review-bound 0.01 \
  --ledger tools/pilot_ledger.jsonl \
  --task-store tools/task_state
```

```
□ exit 0, "dispatched", nonzero cost_usd
□ BOTH flags present: --live AND --confirm-egress
□ --task-store always on (deadline/counters survive restarts)
```

**Refusals (exit 2, no HTTP) are SUCCESS of the guard**: missing key, unapproved endpoint,
`cloud-C-alt` (different provider) — all correctly blocked.

## □ 4. AFTER EACH DISPATCH

```
□ python tools/pilot_report.py --ledger tools/pilot_ledger.jsonl
□ accounting_status: "intact" → continue   |   GAPS_FOUND / exit 1 → STOP the session
□ (periodic) python tools/task_crosscheck.py — state vs ledger, exit 0
```

**Zero-tolerance**: unauthorized egress / credential exposure / privilege escalation ⇒ freeze
the ledger (copy, never edit), reject (stop). Spend and quality are irrelevant to this rule.

## □ 5. SESSION CLOSE

```
□ ledger honest: blocks + dispatches both recorded, zero manual edits
□ pilot_report intact, exit 0
□ run_regression.py all PASS post-close
□ git status --porcelain       → empty (.env + ledger gitignored)
□ spend ≤ $1.00/task, ≤ $20.00/pilot   (confirm from report JSON)
```

## CAPS ON THE POSTER (row-4, SIGNED 2026-10-10)

$1.00/task · $20.00/pilot · 4 attempts + 1 same-profile repair · 300 s/task wall-clock
(enforced across restarts via the task store) · api.anthropic.com ONLY.
