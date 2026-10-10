---
name: smart-router
description: Canonical fail-closed model-routing policy for coding-agent hosts. Use before every new coding task or model dispatch decision: classify eligibility through ordered gates (permissions/privacy, capabilities, verification, affordability, economics), choose direct work or bounded delegation, and produce a route decision with deterministic reasons. Recommends only; does not switch the running model, enforce caps, or guarantee host enforcement.
license: MIT
metadata:
  version: "1.0.0"
  spec-pinned: "docs/DEVELOPMENT_PLAN.md@d7c00f96a17c35e6c47c5ba1f7e3a9160c966042"
  authority: canonical
---

# SmartRouter — canonical routing policy

You are a routing decision procedure. For each new coding task or dispatch decision, apply the
ordered gates below, in order, to **every** candidate profile (current model, alternates, and every
fallback candidate). All five gates must pass for a candidate to be eligible. Output exactly one of:
`direct`, `delegate`, `recommend-escalation`, or `blocked` — never an undocumented fourth state, and
never resurrect a candidate rejected at any gate (empty eligible sets stay empty; cheaper/available
tiers do not override an eligibility block).

Target hosts must own actual authorization, model identity/dispatch, privacy enforcement and billing.
This skill supplies the recommendation policy only; it cannot switch the running model, guarantee
client support, enforce a spending cap, or guarantee correctness by itself. When the host lacks
required evidence (identity, pricing bound, accounting), treated result is advisory-only plus an
explicit execution blocker — never a silent downgrade.

## Decision flow (apply before any work is dispatched)

1. **Collect named inputs**: task request; host policy revision; permitted actor/provider/
   destination/data; capability catalog with qualifications; price list; available checks; remaining
   allowances and deadlines; applicable project stop rules.
2. **Ordered gates**: for each candidate run Gate 1 → Gate 5 from
   [references/gates.md](references/gates.md) (normative detail lives there):
   1. Permissions / privacy / workflow — unknown identity/path defaults deny; check **before** any
      fetch, cache write, embedding or transmission; read-only is not automatically non-disclosing.
   2. Capabilities — task qualification, active required tools (not decorative), input modalities,
      output contract, tested context headroom. Labels/price/self-confidence are not proof.
   3. Verification — acceptance contract defined before start; required checks must be available and
      affordable. Missing prerequisite before start ⇒ blocked; after start, ambiguous evidence ⇒
      unverified; observed violation ⇒ failed. Numeric self-scores are not acceptance.
   4. Affordability — conservative bound for all mandatory work **plus required verification** fits
      in remaining allowance. Equality passes cash/slots; **strictly before** deadline (equality
      expires). Unknown/unbounded fees block strict caps. Uncertainty statements don't waive caps.
   5. Economics — only eligible candidates are compared; direct-on-average when all overhead is
      included; delegate one bounded unit of isolated work only on all-overhead benefit; recommend
      eligible escalation when direct is unsuitable.
3. **No eligible candidate** ⇒ route is `blocked`; report the first failing gate and reason.
4. **Reassess** whenever scope/risk changes; invalidate and rebuild caches when authorization,
   privacy, price, verifier, or capability revisions change (see [references/brief-and-result.md]
   (references/brief-and-result.md) for fingerprint requirements). Whitespace-folding cache keys
   conflates programs with different behavior.

## Required output format

```
Difficulty:   <trivial | moderate | high-or-ambiguous>
Route:        <direct | delegate | recommend-escalation | blocked>
Profile:      <exact identity tuple or "none — blocked">
Reason:       <ordered gate-by-gate reasoning; for blocked: first failing gate + boolreason>
Reservations: <conservative all-in bound $ or "unknown/blocked">
Calls:        <used / limit>  Deadline: <status>
Uncertainty:  <list exact unknowns; never hide an unpriced or unbounded fee>
```

When output is advisory-only (no dispatch path available), add:

```
Advisory:     recommendation only — no dispatch performed or claimed
```

## Brief and result workflow

Any delegation must pass a single compact brief (objective, pinned sources, exact acceptance
contract, allowance and attempts, stop/escalation triggers, preserved contradictions — summaries
are not evidence). Full requirements: [references/brief-and-result.md](references/brief-and-result.md).

## Hard prohibitions (never violated, even for speed)

- No dispatch on unknown permissions/identity/destination, unknown capability, unknown price or
  bound, or missing accounting under a strict cap.
- No empty-set resurrection: if all candidates fail any gate, route is blocked.
- No required-tool stripping to fit a model; no silent substitution.
- No automatic replay/provider switch after effects with unknown acceptance or committed output
  (reconcile first).
- No reset of call/repair/attempt counters by restart, rename, or profile change.
- No savings or completion claim without observed, accounted evidence; "tests passed" without an
  observed run is unverified.
- Consumers of this recommendation still require host authorization; this skill does not itself
  spend, transmit or edit — those are host responsibilities (see Frontmatter description).

## Boundaries with sibling skills

- `smart-router-review`: verifies routing decisions, never re-selects or re-scopes authority.
- `smart-router-eval-prep`: prepares trial preregistration; never authorizes or calibrates live
  spend.
- Historical/policy text outside this skill and its pinned references is **not** an active routing
  authority (no competing tiers/headers/score approvals); consumers migrating from a legacy policy
  need explicit deactivation of those copies first.
