# Phase 3 evaluation preregistration — SmartRouter pilot

Status: **draft awaiting independent review + owner approval** (Phase 3 exit gate per plan §14).
Prepared per [docs/DEVELOPMENT_PLAN.md §11](DEVELOPMENT_PLAN.md) and the
[smart-router-eval-prep skill](../skills/smart-router-eval-prep/SKILL.md). Pinned to plan revision
`d7c00f96a17c35e6c47c5ba1f7e3a9160c966042` and the skill tree at `f7ebe4e1bb18065e1c9cf0ce2243fe7ccea6a63b`.

## 1. Arms

| Arm | Description | Notes |
| --- | --- | --- |
| A | Strong qualified **direct** — dispatch the task straight to the operator's strongest qualified model | Baseline for quality/loss comparison |
| B | Economical qualified **direct** — dispatch straight to the cheapest qualified model | Baseline for cost comparison |
| C | Simple **fixed rule** — deterministic cheap-if-eligible-else-strong selector | Baseline for "simpler policy" comparison |
| D | **SmartRouter** skill flow (ordered gates + brief/verifier/review) including all overhead | The candidate under test |

Same acceptance/privacy/effects rules for all four arms. Weak baselines (B, C) are **never** exposed
to production secrets or consequential writes. Kit workflow constant across arms.

## 2. Host and controls (owner must confirm or supply)

Every field below is **a named owner action** — no value is invented here.

| Control | What must be evidenced | Owner to confirm |
| --- | --- | --- |
| Named evaluation host | Existing host that provides: identity/permissions, usage/billing, call limits, isolation, Stop/recovery, required checks | `StepenkoAnatoli` |
| Model/profile catalog | Immutable qualification tuples (host-profile, provider, model-id/revision, config revision) with tested capability evidence | same |
| Price list | Current unit-aware pricing with a documented revision hash/timestamp | same |
| Test isolation | Tasks run in isolated envs; no shared mutable state across arms | same |
| Stop/recovery | Observable Stop, cancellation, and restart semantics on the chosen host | same |
| Required checks | Available runner (tests/typecheck/lint) with deterministic exit codes | same |
| Conservative bounds | Reliable per-call/prerecorded cost estimate; no unknown/unbounded fees | same |

**If no suitable host exists, Phase 3 stays blocked** — no substitute or scope expansion is implied
(plan §11). Confirming the host is explicitly an owner decision.

## 3. Frozen task set and analysis units

- **Task categories** (must be distinct and representative, not repeated copies of one mechanical
  fixture): bugfix-typo-isolated, small refactor bounded to N files, new endpoint following existing
  pattern, validation/error-handling, component with local state using existing design system.
  (Concrete task list is filled by the evaluation owner on confirmation of the host.)
- **Per-arm sample size**: minimum **20 assigned evaluated observations per arm**.
- **Task coverage**: every task fixture traced to all four arms; unattempted count against coverage
  as preregistered.
- **Tuning/holdout**: tuning data kept in a separate pool; holdout workload used for final
  intervals. Holdout-to-tuning ratio: **50/50**.
- **Repetitions**: **2 repeats per task** per arm (cold cache each repeat).
- **Ordering**: interleaved randomized, seeded with a frozen seed; seeds fixed in this document
  before any trial (seed value filled by evaluation owner at host confirmation).
- **Cache conditions**: cold cache per trial; no per-profile warm-prefix credit claimed.
- **Statistical method**: 95% two-sided tolerance/interval for the difference-in-means of the
  cost-per-success, acceptance, p95 latency, and operator effort between the arms. Paired by task
  fixture when a paired test is valid; otherwise unpaired with the paired/unpaired rule frozen here
  (frozen: paired when the task list is identical across arms, which it will be).
- **Missing-data rule**: an attempt with unknown/missing charge is marked unknown and included as
  such; it never substitutes for a value.

## 4. Numerical thresholds (frozen for this pilot)

Values below are proposed, supported by plan §11's S21a-S22g synthetic examples, and require owner
approval before the pilot starts.

| Metric | Threshold |
| --- | --- |
| Mandatory acceptance floor per arm | **90%** of assigned evaluated observations accepted |
| Max acceptance loss vs A | **5 percentage points** (entire interval's upper bound ≤ 5 pp) |
| Min cost-per-success reduction vs A | **10%** (entire interval's lower bound ≥ 10%) |
| Max p95 latency increase vs A | **10%** (entire interval's upper bound ≤ 10%) |
| Max operator-effort increase vs A | **10%** (entire interval's upper bound ≤ 10%) |
| C-vs-D equivalence margin (cost / latency / effort) | **±5%** — the **entire** interval must lie inside for the "favors simpler C" finding |
| C-vs-D equivalence margin (acceptance difference) | **±5 pp** — entire interval must lie inside |
| D-vs-C incremental benefit for promotion eligibility | **strictly > 5%** (lower bound > 5%, not ≥) |
| Zero-baseline rule | A cost/success of $0.00 in arm A makes relative D-vs-A comparison undefined → report `inconclusive`; **no invented infinity/zero-percent** |
| Zero-success rule | Arm with 0 accepted successes has undefined cost ratio. Absent a separately evidenced safety/quality-floor violation, **economic comparison is inconclusive**, never savings |
| Severe-failure stop rule | Any observed unauthorized/safety-violating effect ⇒ **stop trial, decision reject**, regardless of other evidence; safety rejection has priority over missing accounting |
| Uncertainty/confidence level | **95%** throughout |

## 5. Attempt / budget / deadline boundaries (per trial, per task)

- Max attempts per task (any arm): **4** physical model dispatches.
- Max cost per task: **$1.00** (preregistered cap; confirmed or revised by owner at host confirmation).
- Max elapsed wall-clock per task: **5 minutes**.
- All attempts — planner, worker, verifier, transport retry, repair, escalation — count against
  both the attempt and cost ceiling; cancelled/timeout calls count; hidden host retries count.
- Equality-passes rules: cost bound ≤ remaining budget passes; call `used + reserved ≤ limit`
  passes; time **strictly before** deadline passes (equality expires).
- Repairs: at most **one** same-profile correction per original task; a differently-qualified
  profile consumes escalation, not a repair allowance; restart/rename never resets counters
  (plan sections 7-8).

## 6. Drift and restart of the pilot

- If model/price/config drift is detected after a frozen point, the **preregistered rule** is:
  restart the affected workload only, using a fresh pool of tasks from the same frozen category
  list; discard drift-affected observations from the affected arm; do not retrospectively change
  thresholds.
- Missing billable usage cannot establish savings; if accounting is incomplete, the report can
  close `inconclusive` with documented gaps, and **no adoption** is proposed.
- Reservations for unresolved charges persist after report closure; report completion does not
  release them.

## 7. Report and promotion gates

Phase 4 has three separate fields: `report_status ∈ {complete, incomplete}`, `decision ∈ {reject,
inconclusive, simplify, promote}`, `router_promotion_eligible ∈ {true, false}`.

| Predicate | Outcome |
| --- | --- |
| Severe safety failure observed, regardless of other metrics | `decision = reject (stop)`, `router_promotion_eligible = false`; reclassify affected accepted counts |
| Quality/latency/effort floor violated | `decision = reject`, `eligible = false` |
| Accounting/precision/coverage gap (post-safety) | `decision = inconclusive`, `eligible = false` |
| Qualifying simpler C (equivalence held, all gates pass) and no D incremental benefit | `decision = simplify`, `eligible = false`; C may be proposed for separate authorization |
| All hard gates pass and D shows incremental benefit > 5% over qualifying C | `decision = promote narrowly`, `eligible = true` for this pilot's declared scope only; adoption still requires separate approval |
| Complete precise evidence, neither simplify nor promote predicates hold | `decision = reject (insufficient benefit)` |

Report completion is an independent decision from promotion eligibility; a complete report can
close `rejected`/`inconclusive` with disclosed gaps and still release no reservation and authorize
no adoption.

## 8. Severe-failure zero-tolerance register (pre-frozen categories)

- Unauthorized network/data egress.
- Unauthorized deletion / data loss.
- Unauthorized credential exposure.
- Privilege escalation beyond the task grant.
- Any observed effect not covered by the action/data/destination grant.
- Any unknown-acceptance side effect that cannot be reconciled at trial close.

Any of these ⇒ decision `reject (stop)`, regardless of cost savings or output quality.
`router_promotion_eligible = false`.

## 9. On what this document does not authorize anything

This document is a **plan** for an authorized trial; it does not itself authorize spend, dispatch,
or data transmission. Those require separate approval at Phase 4 start (plan §14, Phase 4 gate) and
host-qualification evidence listed in §2 being confirmed.

## 10. Outstanding owner actions before Phase 3 closes

| # | Action | Blocks |
| --- | --- | --- |
| 1 | Confirm or substitute the named evaluation host | Phase 3 exit |
| 2 | Confirm or revise the numeric thresholds in §4 | Phase 3 exit |
| 3 | Supply the concrete task list / seeds / pricing revision | Phase 3 exit |
| 4 | Approve spend/egress/environment for the pilot itself | Phase 4 start |
