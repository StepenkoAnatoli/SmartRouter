---
name: smart-router-review
description: Review routing plans, skills, host integrations and task receipts for authority conflicts, fail-open eligibility, privacy, cost accounting and verification defects. Use for SmartRouter PR review or acceptance review; report evidence-backed blockers instead of numeric approval scores.
license: MIT
compatibility: Keep the sibling smart-router skill available. Reviews are read-only unless separately authorized; no paid inference or external data transmission is approved.
metadata:
  version: "0.1.0-preview"
---

# SmartRouter review

Read the [canonical skill](../smart-router/SKILL.md) and [routing contract](../smart-router/references/routing-contract.md). They are the only SmartRouter selection authority. This skill supplies review procedure, not competing tiers or dispatch policy. Preserve higher-priority project review requirements.

## Review procedure

1. Pin the artifact revision, scope, governing instructions and reviewed files. State whether evidence is source inspection, a test actually run, host observation or an assumption. Check authorization before new retrieval/model calls; do not execute upstream repositories or live providers merely to review them.
2. Check ordered gates for the current model, every planner/reviewer and every fallback. Examine empty/all-unavailable sets, unknown identity/path/capability and manual overrides. Test evidence should prove rejection causes no send at the real dispatch callsite. Packaging tests alone are not semantic evidence.
3. Check predetermined task acceptance, exact tool/refusal/structured/media contracts, verifier errors, missing checks and severe failures. Do not accept numeric self-grades, confidence or HTTP 200 as task verification.
4. Check strict-cap behavior with missing prices/usage, required verification affordability, total attempts/sunk costs, uncertain charges and cancellation/restart reconciliation. Unknown-cost claims cannot support savings. Distinguish preview display from separately authorized recommendation generation.
5. Check safe retry: no automatic replay after possible effects, committed streams or unknown media acceptance; same gates for repairs/fallbacks. Confirm project red-suite/spending stops override bounded repair permissions.
6. Check one authority, historical README migration, exact-content preservation, cache invalidation, evidence provenance, license/redistribution permission and secret-free receipts.
7. Apply the [concrete scenarios](../smart-router/references/scenarios.md). Record observed walkthrough/evidence and disposition at the reviewed revision. Proposed future tests stay untested.
8. Return the [review report](assets/review-report.md). **Request Changes** for any unresolved safety/permission defect, contradictory authority, failed/missing required check, or missing redistribution permission. Disclosure is not a waiver. **Reject** when the approach is unsafe/out of scope or requires redesign. **Approve** only when all required gates for this declared artifact are evidenced; explicitly exclude unimplemented runtime/pilot claims.

Give each finding a severity, pinned evidence, impact, required correction and concrete acceptance case. Nonblocking limitations may be disclosed; blockers must be corrected and rechecked. Do not merge, expand scope, edit consumers or initiate paid trials.
