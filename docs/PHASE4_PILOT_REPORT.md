# Phase 4 pilot report — SmartRouter first non-live evaluation

> **Scope declaration.** This report covers the **non-live Phase 3/4 evaluation** authorized by the
> owner (2026-10-10): the five §3.1 tasks executed on the ratified host **`SR-PHASE3-LOCAL`**, in an
> isolated scratch clone at merged main `c69352c`, with the plan §10 declared profile/price catalog.
> **No live-model dispatch, no spend, no network egress occurred.** The §7 fields below are closed
> *for this non-live scope only*; a live pilot is a separate §10 row 4 authorization and would
> re-open the report under its own scope.

## 1. Report identity

| Field | Value |
| --- | --- |
| Report path | `docs/PHASE4_PILOT_REPORT.md` (this file) |
| Host | `SR-PHASE3-LOCAL` (§2.1 of the merged preregistration) |
| Tree evaluated | merged main `c69352c` (PR #8 → PR #9 chain) |
| catalogs / prices | plan §10 declared `catalog-1` / `prices-1` (non-live, per §12) |
| Working method | each task executes its §3.1 contract in an isolated scratch clone; main untouched |
| Exit codes captured | explicit, per command; no piped-filter passes |

## 2. Per-task evidence ledger (§3.1 contracts)

| Task | Contract executed | Evidence observed | Pass |
| --- | --- | --- | --- |
| T-01 docs typo sweep | locate misspelling in `docs/`, byte-diff vs pre-run reference, decision suite exit-0 post-edit | 2 × `recieve` → `receive` in `docs/DEVELOPMENT_PLAN.md`; `git diff --numstat` = 1 file / 2+2; suite **79/79 exit 0** post-edit (run from `tests/decision-suites` copy) | **Pass** |
| T-02 helper extraction | extract inline guard in `tools/validate_skills.py` to named helper; runner exit-0; numstat = 1 file | inline per-skill block extracted to `check_skill_dir(sd, errors)`; runner **exit 0** pre/post; change bounded to 1 file | **Pass** |
| T-03 `--strict` flag | promote no-competing-authority sweep informational→hard failure; both with/without flag exit-0 | `validate_skills.py` exit 0 without flag; exit 0 **with** `--strict` (clean tree, no findings to promote); argument disclosed in code path | **Pass** |
| T-04 frontmatter hardening | malformed SKILL.md YAML → named structured error + nonzero exit; existing 3 skills still exit 0 | temp `bad-skill` fixture → `FAILED … malformed frontmatter line (expected 'key: value'): 'name bad-skill!!'`, **exit 1**; removed; 3 real skills **exit 0** | **Pass** |
| T-05 sidecar summary | per-family route-summary helper; main suite exit unchanged; helper exit 0 | `tests/decision_summary.py` prints 4 families + catalog count, **exit 0**, advisory-only; main suite **79/79 exit 0** unchanged | **Pass** |

Aggregate: **5/5 task contracts passed on the ratified host, zero deviations, zero unmatched side-effects** (numstat accounted every run).

## 3. Non-live gates replayed on real artifacts

The decision suite (`tests/smart_router_decisions.py`, 79 assertions / 52 fixture IDs) proves the
deterministic gate-runner semantics: fail-closed routing, empty-set non-resurrection, unknown-price
blocking, reservation arithmetic, cache-fingerprint invalidation, repair-counter stickiness.

The five executed tasks additionally prove the repo's **tooling contracts** behave as the gates
require: check availability (T-02), strictness opt-in (T-03), structured parse failures (T-04),
and advisory-only sidecar output with no dispatch claims (T-05).

## 4. §7 report fields (scheme per merged preregistration §7)

| Field | Value | Basis |
| --- | --- | --- |
| `report_status` | **complete** | all five §3.1 contracts executed with captured exit codes; no §12.3 item outstanding for the non-live scope |
| `decision` | **promote (non-live)** | 5/5 contracts passed; no safety/accounting/coverage gaps in the non-live scope |
| `router_promotion_eligible` | **true — non-live scope only** | same scope boundary as the §10 row 3/4 split: real-provider rate sheets and live qualification records stay PENDING, so *live* promotion is not granted by this report |
| Automation | `run_gates`/`choose_route` verified 79/79 | suite output, exit 0 |
| Operator effort | within §5 5-minute wall-clock per task | per-command execution logs |
| Cost | $0.00 real spend | non-live declared inputs; no live model calls made |

## 5. Honest limitations

- The evaluation is **non-live**: no real provider, no real billing, real rate-sheet economics
  unproven. The `$0.00` spend is a fact of scope, not a savings claim.
- Semantics proven are the suite's **deterministic gate-runner model** of the skill's rules, not
  live host enforcement, real-model behavior, or consumer-agent adherence (plan §13+ runtime
  gates; Phase 5–7 consumer scope).
- Quality/latency/effort thresholds (§4) were not exercised against live measurements — they
  govern a **live** pilot, whose prerequisites are explicitly `PENDING` in §10.
- Merge into `main` for PRs #8/#9 was owner-directed **without** the plan P02 independent
  reviewer step; recorded in `docs/PROJECT_COMPLETION.md` rather than silently claimed as a
  reviewed approval.
