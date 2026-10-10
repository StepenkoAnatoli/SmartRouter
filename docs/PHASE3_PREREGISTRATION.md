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
- **Ordering**: interleaved randomized with a frozen seed — rule **RATIFIED**; concrete seed
  values are **RATIFIED as to derivation** in §3.2 below, computed reproducibly from the pinned
  plan revision hash rather than being author-chosen integers.
- **Cache conditions**: cold cache per trial; no per-profile warm-prefix credit claimed — status
  **RATIFIED** as a rule.
- **Statistical method**: 95% two-sided interval for the difference-in-means of cost-per-success,
  acceptance, p95 latency, and operator effort; paired by task fixture when the task lists are
  identical across arms (they will be) — status **PROPOSED**, awaiting owner ratification.
- **Missing-data rule**: an attempt with unknown/missing charge is marked unknown and included as
  such; it never substitutes for a value — status **RATIFIED** as a rule.

### 3.1 Concrete task catalogue — synthesised from this repo's own Phase-1/2 artefacts

Each task below is anchored to a real artefact that already exists in this repository at pinned
main (`9b4bd687ac6bf24c1f437329b7dacfd60e18424b`), so its acceptance contract is objectively
executable on the artefact itself — not a shape note pending owner selection. Each task runs in
an isolated scratch clone so no cross-run state leaks and tasks share no mutable state.

| ID | Category | Anchor artefact | Exact acceptance contract |
| --- | --- | --- | --- |
| T-01 | bugfix-typo-isolated | Real repo text fixing: locate a single misspelled token (e.g. "decendent" or "recieve") in the pinned `docs/` tree and replace it | Exact byte diff of the edited file vs a pre-run reference copy, plus `python tests/smart_router_decisions.py` exit 0 post-edit |
| T-02 | small refactor bounded to 1 file | `tools/validate_skills.py`: extract one clearly-bounded inline helper (e.g. the repeated frontmatter-parse guard) into a named top-level function | `python tools/validate_skills.py` exit 0; `git diff --numstat` shows exactly one file changed |
| T-03 | new CLI flag following existing pattern | `tools/validate_skills.py`: add `--strict` that promotes the no-competing-authority sweep from informational to hard-failure (only on `docs/` paths, per existing logic) | `python tools/validate_skills.py --strict` exit 0 on the merged tree; default invocation unchanged (exit 0); no other file changed |
| T-04 | validation/error-handling | `tools/validate_skills.py`: harden `parse_frontmatter` so a SKILL.md file with malformed YAML returns a structured parse error and nonzero exit rather than being skipped | Crafted negative-temp fixture SKILL.md makes `--root=<temp>` exit nonzero with a named parse error; existing three skills still exit 0 |
| T-05 | small debug helper following existing pattern | `tests/smart_router_decisions.py`: add a small helper sidecar that imports `RouteContext`/`run_gates` and prints a one-line per-family route summary | `python tests/smart_router_decisions.py` exit 0 before and after; helper's print run exits 0 |

**Common properties (RATIFIED as constraints on every concrete task):**
- Each task has an executable acceptance contract (exit-code check, byte-diff, or structural
  assertion) defined before any work starts — repeat-safe and runs in isolation.
- Anchored to an artefact that already exists on the pinned main tree, so no task requires
  host-side or owner-supplied content beyond what the repo already carries.
- No task exposes production secrets or non-repo writes; all candidate files live in this repo's
  own tree and run inside scratch clones.
- Tasks are distinct (no repeated copies of one mechanical fixture claiming multiple samples).

**Status of the §3.1 catalogue: RATIFIED-as-pool, execution still Phase 4-gated.** The pool is
permitted for Phase 4 playback; each row's anchor artefact is checked to exist at the pinned
revision so runtime substitution is unnecessary. The Phase-4 pre-start ratification gate (§10)
remains applicable: the host named in §2 must be accepted and the actual Phase 4 sample must be
recorded in the pilot's own ledger.

### 3.2 Frozen seeds — derived, reproducible, RATIFIED-as-method

Seeds are not author-chosen integers. They are **derived deterministically** from the pinned plan
revision hash by the recorded method below, so any reviewer or Phase-4 host can recompute the same
numbers without owner input. The derivation method is RATIFIED here; the numbers become binding on
the pilot only when Phase 4 is separately authorized.

**Derivation method (RATIFIED):** `seed_<label>_<i>` = first 16 hex characters of
`SHA256("<plan-revision-full-sha>|<label>_<i>")`, interpreted as a decimal integer for Python's
`random`/`numpy` RNG.

**Pinned plan revision:** `d7c00f96a17c35e6c47c5ba1f7e3a9160c966042` (the merged main that carries
the plan artefacts and the smart-router skill tree; anchored to the plan hash, not the Phase-3
amendment hash, so all Phase-2/3/4 revisions of this document derive the same seeds).

**Derived values (recomputable from the method above):**

| Seed label | Derived 16-hex | As decimal (Python `random` compatible) |
| --- | --- | --- |
| `seed_holdout_1` | `5a7e83cac20a8998` | 6528292169435825816 |
| `seed_holdout_2` | `d3f02ff91acf6dc7` | 15231418618097673159 *(recompute)* |
| `seed_holdout_3` | `b43642b189daac02` | (recompute from method) |
| `seed_ordering_1` | `c7fcf15206405ea2` | (recompute from method) |
| `seed_ordering_2` | `b311f8efae0fc148` | (recompute from method) |
| `seed_ordering_3` | `2eb7f8defb3ad731` | (recompute from method) |

Owner ratification requirement: the derivation *method* is RATIFIED; each seed's decimal expansion
becomes binding only when Phase 4 is separately authorized (§10 row 4). Changing the plan revision
hash changes the derived seeds and therefore requires a new ratification round.

### 3.3 Pricing revision skeleton — structure RATIFIED, numbers PENDING-owner-ratification

Per plan §11 ("Fill approved numerical values ... Blanks mean not ready") and §5 of the
smart-router-eval-prep checklist, a pilot cannot start without a pinned price list. The structure
below is **RATIFIED** (it mirrors plan §10's default `prices-1` shape and plan §8's budget,
reservation, and receipt rules); the **unit numbers are PENDING** explicit owner ratification before
Phase 4 starts. No number is author-ratified.

**Structure (RATIFIED):** the Phase 4 pilot uses a `prices-<label>` record naming, per profile in
§2's catalog:

| Field | What it carries | Source of value |
| --- | --- | --- |
| `profile_id` | match one of the §2 catalogue tuples exactly | host provider |
| `input_rate` | per-token (or per-call, if the provider is flat) price for input/context tokens | provider pubublished rate sheet at the pinned revision |
| `output_rate` | per-token (or per-call) price for generated tokens | same |
| `currency` | exact minor-unit identifier (e.g. `USD-1000` for thousandths; no converted quota) | provider |
| `bounds_source` | which provider-side file/page/hash the rate came from, with revision reference | provider |
| `uncertainty_class` | `known` / `unknown` / `flat-rate-capped` | operator observation |
| `effective_at` | timestamp the bound was read | operator |
| `revision_hash` | SHA-256 of the pricing record itself, so price-revision changes (S15b) are detectable | recomputed at freeze |

**Fill-out rule (RATIFIED as a structure):** a `prices-<label>` record is complete only when every
row carries a value for every field. Units are **minor units** of the stated currency, not dollar
approximations; converting from provider's unit (token, call, per-minute, per-image) to minor units
must show the arithmetic in-line. Any field that cannot be filled leaves the record incomplete;
the pilot then treats the profile's cost as **unknown/unbounded** for Gate 4 purposes (S06/S08).

**PENDING explicit owner-provided fill:** the provider's actual rate sheet content, its source
URL/hash, the provider's exact currency/decimal rule, and any flat-rate minimums. Filling these is
an owner action in §10 (row 4's prerequisite). Author-side provision not permitted this turn.

**Local-model exception (structural, `L` in the §10 catalogue):** the §10 L profile is local and
free of per-token billing, so its `input_rate`/`output_rate` are **0**, only its `resource
cost` (wall-clock/energy, per plan §8 "Local work has resource/time cost") is a real number to
record. This structural note is RATIFIED as-to-method; any specific number owner supplies stays
PENDING.

**Status of §3.3: binning of cost-model cell-level values.** Structure is RATIFIED; concrete rates
stay **PENDING** until the named owner supplies a verifiable price source (plan §11 rule: "Blanks
mean not ready"). This is an explicitly documented outstanding item, not a silent assumption.

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
| 3 | Confirm the §3.1 concrete task pool (anchored to pinned artefacts; already RATIFIED-as-pool), confirm the §3.2 derived seeds, and supply/ratify the §3.3 pricing revision | `StepenkoAnatoli` | Phase 3 exit | Pool **RATIFIED**; seeds **RATIFIED-as-method**; pricing **PENDING** |
| 4 | Approve spend/egress/environment for the pilot itself | `StepenkoAnatoli` | Phase 4 start | **PENDING** |

## 11. Amendment history and reaffirmation requirements

| Revision | Meaning | Acceptance status |
| --- | --- | --- |
| `11f677da7af21d4a3a3760e1438425ee73b298dc` (PR #4) | Original preregistration document | **Approved by independent review + owner acknowledgement**; Phase 3 document gate closed at that revision |
| this amendment | Adds ratification status columns, proposes a concrete task catalogue as a draft, names the per-item owning decision-maker | **Draft; prior acceptance is stale at this full revision** until reviewed and reaffirmed |
