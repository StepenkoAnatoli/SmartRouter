# Phase 3 evaluation preregistration — SmartRouter pilot

> **Amendment notice (2026-10-10).** This document amends the Phase 3 preregistration accepted at
> `11f677da7af21d4a3a3760e1438425ee73b298dc` (PR #4). The amendment adds explicit per-value and
> per-control ratification status (§4 status column, §2 host/controls status column), proposes a
> concrete task catalogue and seeds as placeholders pending owner selection (§3.1), and updates §10
> to point at the exact evidencing owner. **No numbers, thresholds, hosts, or task lists are hereby
> ratified.** Per plan P02, prior Phase 3 document acceptance is stale until delta-reviewed and
> reaffirmed at this new full revision by an independently designated non-author reviewer, plus a
> separate owner acknowledgement.

Status: **draft amendment awaiting independent review + ratification by owner** (Phase 3 exit gate per plan §14/§15).
Prepared per [docs/DEVELOPMENT_PLAN.md §11](DEVELOPMENT_PLAN.md) and the
[smart-router-eval-prep skill](../skills/smart-router-eval-prep/SKILL.md). Pinned to plan revision
`d7c00f96a17c35e6c47c5ba1f7e3a9160c966042` and the skill tree at merged main at the time of amendment.

## 0. Status vocabulary used throughout this document

| Status | Meaning |
| --- | --- |
| **RATIFIED** | Owner-supplied (or explicitly owner-acknowledged) value; may be used as-is if a Phase 4 start is separately authorized. |
| **PROPOSED** | Documented author default, aligned with plan §11's S21a-S22g reference protocol, **awaiting owner ratification**. Becomes binding only after owner acknowledgement. |
| **PENDING** | Owner must supply; no author-proposed default exists. Blocks the milestone it feeds until supplied. |
| **BLOCKED** | A prerequisite is missing and blocks the next phase milestone until resolved; no workaround is implied. |

Every numeric value and host requirement in this document carries one of these status labels.
Ratification is an owner action recorded in this document's PR or a linked artefact; an agent
cannot self-ratify.

## 1. Arms

| Arm | Description | Notes |
| --- | --- | --- |
| A | Strong qualified **direct** — dispatch the task straight to the operator's strongest qualified model | Baseline for quality/loss comparison |
| B | Economical qualified **direct** — dispatch straight to the cheapest qualified model | Baseline for cost comparison |
| C | Simple **fixed rule** — deterministic cheap-if-eligible-else-strong selector | Baseline for "simpler policy" comparison |
| D | **SmartRouter** skill flow (ordered gates + brief/verifier/review) including all overhead | The candidate under test |

Same acceptance/privacy/effects rules for all four arms. Weak baselines (B, C) are **never** exposed
to production secrets or consequential writes. Kit workflow constant across arms.

**Arm-definition status:** **RATIFIED** as structural (four arms and their roles per plan §11), but
each arm's concrete model/profile identity is **PENDING** until the owner names the host and
supplies the immutable parent tuple in §2.

## 2. Host and controls (status per control)

Every field below is an owner-level decision or an owner-supplied fact. No field is invented here.

| Control | What must be evidenced | Owner to confirm | Status |
| --- | --- | --- | --- |
| Named evaluation host | Existing host that provides: identity/permissions, usage/billing, call limits, isolation, Stop/recovery, required checks | `StepenkoAnatoli` | **PENDING** | — |
| Model/profile catalog | Immutable qualification tuples (host-profile, provider, model-id/revision, config revision) with tested capability evidence (per plan §5 qualification records) | `StepenkoAnatoli` | **PENDING** | — |
| Price list | Current unit-aware pricing with a documented revision hash/timestamp | `StepenkoAnatoli` | **PENDING** | — |
| Test isolation | Tasks run in isolated envs; no shared mutable state across arms | `StepenkoAnatoli` | **PENDING** | — |
| Stop/recovery | Observable Stop, cancellation, and restart semantics on the chosen host | `StepenkoAnatoli` | **PENDING** | — |
| Required checks | Available runner (tests/typecheck/lint) with deterministic exit codes | `StepenkoAnatoli` | **PENDING** | — |
| Conservative bounds | Reliable per-call/prerecorded cost estimate; no unknown/unbounded fees | `StepenkoAnatoli` | **PENDING** | — |
| Host qualification records | Pointer to each profile's qualification record (tested tasks, check/rubric outcomes, reviewer, expiry) per plan §5 | `StepenkoAnatoli` | **PENDING** | — |

**If no suitable host exists, Phase 3 stays blocked** — no substitute or scope expansion is implied
(plan §11). Confirming the host is explicitly an owner decision.

## 3. Frozen task set and analysis units

- **Task categories** (must be distinct and representative, not repeated copies of one mechanical
  fixture): bugfix-typo-isolated, small refactor bounded to N files, new endpoint following existing
  pattern, validation/error-handling, component with local state using existing design system.
- **Per-arm sample size**: minimum **20 assigned evaluated observations per arm** — status
  **PROPOSED**, matches plan §11/S21a-S22g reference protocol.
- **Task coverage**: every task fixture traced to all four arms; unattempted count against coverage
  as preregistered — status **RATIFIED** as a *rule* (the rule, not the concrete task list).
- **Tuning/holdout**: tuning data kept in a separate pool; holdout workload used for final
  intervals. Holdout-to-tuning ratio: **50/50** — status **PROPOSED**, awaiting owner ratification.
- **Repetitions**: **2 repeats per task** per arm (cold cache each repeat) — status **PROPOSED**,
  matches plan §11/S21a-S22g.
- **Ordering**: interleaved randomized with a frozen seed — status: rule **RATIFIED**; concrete
  seed values **PENDING** (owner supplies at host confirmation).
- **Cache conditions**: cold cache per trial; no per-profile warm-prefix credit claimed — status
  **RATIFIED** as a rule.
- **Statistical method**: 95% two-sided interval for the difference-in-means of cost-per-success,
  acceptance, p95 latency, and operator effort; paired by task fixture when the task lists are
  identical across arms (they will be) — status **PROPOSED**, awaiting owner ratification.
- **Missing-data rule**: an attempt with unknown/missing charge is marked unknown and included as
  such; it never substitutes for a value — status **RATIFIED** as a rule.

### 3.1 Concrete task catalogue — **PENDING** (proposed draft supplied below for owner selection)

The actual Holdout task set must be picked by the owner from the proposed pool, and each task must
have its own exact acceptance contract, before any Phase 4 start. Shape below is a **proposal**;
not a promise of concrete trials. Each row must be confirmed or substituted by the owner.

| ID | Category | Shape (proposal, not contract) |
| --- | --- | --- |
| T-01 | bugfix-typo-isolated | Deprecate/replace a single identifier in one file, with an exact-diff acceptance check |
| T-02 | small refactor bounded to N files | Rename a multi-use function across N files with no behavioral change; exact tests pass |
| T-03 | new endpoint following existing pattern | Add one endpoint conforming to existing controller/service patterns; existing unit tests still pass |
| T-04 | validation/error-handling | Tighten input validation with specific error contracts; add unit tests for the new paths |
| T-05 | component with local state using existing design system | Implement a small component using existing design-system primitives; visual/props contract test |

**Common properties (RATIFIED as constraints on every concrete task, whichever the owner picks):**
- Every task must have an exact, checkable acceptance contract (diff assertion, test command, or
  structural check) before work starts.
- Every task must be *repeat-safe* and run in isolation.
- Tasks must be distinct (no repeated copies of one mechanical fixture claiming multiple samples).

## 4. Numerical thresholds — status per value

### 4.1 Core per-arm gates (§4 table, each value individually labelled)

| Metric | Proposed value | Basis | Status |
| --- | --- | --- | --- |
| Mandatory acceptance floor per arm | **90%** of assigned evaluated observations accepted | plan §11 reference protocol (S21a) | **PROPOSED** |
| Max acceptance loss vs A | **5 percentage points** (entire interval upper bound ≤ 5 pp) | plan §11 reference protocol (S22c) | **PROPOSED** |
| Min cost-per-success reduction vs A | **10%** (entire interval lower bound ≥ 10%) | plan §11 reference protocol (S22c) | **PROPOSED** |
| Max p95 latency increase vs A | **10%** (entire interval upper bound ≤ 10%) | plan §11 reference protocol (S22c) | **PROPOSED** |
| Max operator-effort increase vs A | **10%** (entire interval upper bound ≤ 10%) | plan §11 reference protocol (S22c) | **PROPOSED** |
| Confidence level | **95%** throughout | plan §11 | **PROPOSED** |

### 4.2 C-vs-D equivalence and promotion rules

| Rule | Proposed form | Basis | Status |
| --- | --- | --- | --- |
| C-vs-D equivalence margin (cost / latency / effort) | **±5%** — the **entire** interval must lie inside for a "favors simpler C" finding | plan §11 (S22b) | **PROPOSED** |
| C-vs-D equivalence margin (acceptance difference) | **±5 pp** — entire interval must lie inside | plan §11 (S22b) | **PROPOSED** |
| D-vs-C incremental benefit for promotion eligibility | **strictly > 5%** (lower bound > 5%, not ≥) | plan §11 (S22c/S22f explicitly exclude the boundary case) | **PROPOSED** |

### 4.3 Degenerate-evidence rules (structural, not tunable in this pilot)

| Rule | Form | Status |
| --- | --- | --- |
| Zero-baseline rule | A cost/success of $0.00 in arm A makes relative D-vs-A comparison undefined → report `inconclusive`; **no invented infinity/zero-percent** | **RATIFIED** (structural rule per plan §11, not a tunable threshold) |
| Zero-success rule | Arm with 0 accepted successes has undefined cost ratio. Absent a separately evidenced safety/quality-floor violation, **economic comparison is inconclusive**, never savings | **RATIFIED** (structural rule) |
| Severe-failure stop rule | Any observed unauthorized/safety-violating effect ⇒ **stop trial, decision reject**, regardless of other evidence; safety rejection has priority over missing accounting | **RATIFIED** (structural rule, zero-tolerance per plan §11) |

### 4.4 Rule — pending-products boundary

No threshold here becomes *the* operative pilot value until the owner ratifies it in this document
(or replaces it, which itself becomes the ratified version). **Nothing in §4 alone authorizes a
Phase 4 start.**

## 5. Attempt / budget / deadline boundaries — status per value

- Max attempts per task (any arm): **4** physical model dispatches — status **PROPOSED** (tighter
  than plan §10's common fixture default of six; a deliberate, owner-visible tightening).
- Max cost per task: **$1.00** — status **PROPOSED** (matches plan §10 fixture defaults; a
  placeholder pending owner's real-unit price list from §2).
- Max elapsed wall-clock per task: **5 minutes** — status **PROPOSED** (matches plan §10 fixture
  defaults).
- All attempts — planner, worker, verifier, transport retry, repair, escalation — count against
  both the attempt and cost ceiling; cancelled/timeout calls count; hidden host retries count —
  status **RATIFIED** (structural rule plan §7-8).
- Equality-passes rules: cost bound ≤ remaining budget passes; call `used + reserved ≤ limit`
  passes; time **strictly before** deadline passes (equality expires) — status **RATIFIED**
  (structural rule plan §8).
- Repairs: at most **one** same-profile correction per original task; a differently-qualified
  profile consumes escalation, not a repair allowance; restart/rename never resets counters —
  status **RATIFIED** (structural rule plan §7).

## 6. Drift and restart of the pilot

- If model/price/config drift is detected after a frozen point, the **preregistered rule** is:
  restart the affected workload only, using a fresh pool of tasks from the same frozen category
  list; discard drift-affected observations from the affected arm; do not retrospectively change
  thresholds — status **RATIFIED** (structural rule plan §11).
- Missing billable usage cannot establish savings; if accounting is incomplete, the report can
  close `inconclusive` with documented gaps, and **no adoption** is proposed — status **RATIFIED**
  (structural rule).
- Reservations for unresolved charges persist after report closure; report completion does not
  release them — status **RATIFIED** (structural rule plan §8).

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

Status of the whole §7 predicate table: **RATIFIED** as structure (these predicates mirror plan
§11's frozen decision rules; the *numeric thresholds feeding them* stay **PROPOSED** until the
owner ratifies §4/§5).

Report completion is an independent decision from promotion eligibility; a complete report can
close `rejected`/`inconclusive` with disclosed gaps and still release no reservation and authorize
no adoption — **RATIFIED** (structural rule).

## 8. Severe-failure zero-tolerance register (pre-frozen categories)

- Unauthorized network/data egress.
- Unauthorized deletion / data loss.
- Unauthorized credential exposure.
- Privilege escalation beyond the task grant.
- Any observed effect not covered by the action/data/destination grant.
- Any unknown-acceptance side effect that cannot be reconciled at trial close.

Any of these ⇒ decision `reject (stop)`, regardless of cost savings or output quality.
`router_promotion_eligible = false`. Status of the register: **RATIFIED** (structural, plan §11).

## 9. On what this document does not authorize anything

This document is a **plan** for an authorized trial; it does not itself authorize spend, dispatch,
or data transmission. Those require separate approval at Phase 4 start (plan §14, Phase 4 gate) and
host-qualification evidence listed in §2 being confirmed. — **RATIFIED** (structural boundary).

## 10. Outstanding owner actions before Phase 3 closes (exact owner named)

| # | Action | Owner evidencing it | Blocks | Current status |
| --- | --- | --- | --- | --- |
| 1 | Confirm or substitute the named evaluation host | `StepenkoAnatoli` | Phase 3 exit | **PENDING** |
| 2 | Ratify or revise the numeric thresholds in §4/§5 | `StepenkoAnatoli` | Phase 3 exit | **PENDING** |
| 3 | Confirm a concrete task list (from §3.1 battery or substitute), frozen randomization seeds, and pricing revision | `StepenkoAnatoli` | Phase 3 exit | **PENDING** |
| 4 | Approve spend/egress/environment for the pilot itself | `StepenkoAnatoli` | Phase 4 start | **PENDING** |

## 11. Amendment history and reaffirmation requirements

| Revision | Meaning | Acceptance status |
| --- | --- | --- |
| `11f677da7af21d4a3a3760e1438425ee73b298dc` (PR #4) | Original preregistration document | **Approved by independent review + owner acknowledgement**; Phase 3 document gate closed at that revision |
| this amendment | Adds ratification status columns, proposes a concrete task catalogue as a draft, names the per-item owning decision-maker | **Draft; prior acceptance is stale at this full revision** until reviewed and reaffirmed |
