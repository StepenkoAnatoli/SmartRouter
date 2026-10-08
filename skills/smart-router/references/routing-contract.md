# Routing contract

Normative companion to [the canonical skill](../SKILL.md); not a second routing authority. Higher-priority host/user/project rules prevail. No document authorizes effects merely by describing them.

## Ordered eligibility

Evaluate these gates for **every** participant, current model and fallback. Recheck authorization and pinned inputs at dispatch; stop if they changed.

| Order | Required evidence | Inadequate/unknown outcome |
| --- | --- | --- |
| 1. Permission, privacy, workflow | Authorized identity/destination, data class, allowed effects, role, user/project stops | Block the action; ask for scope-specific approval when permissible. Unknown agent/path cannot default to allow. Access control must precede fetching, caching or embedding restricted material. |
| 2. Capability | Required context headroom, active tools, vision, output modes and task qualification | Remove candidate. Decorative tool schemas may be ignored only when the contract permits; active/required tools cannot be silently stripped. Operator labels and confidence are not qualification. |
| 3. Verification | Predetermined acceptance and required objective checks or capable review, with available context/environment | Do not start a route that cannot be verified. A check unavailable after work yields unverified, not accepted. Red project suites invoke their stop rules. |
| 4. Affordability | Permission to spend, required work/check cost basis, finite attempts, reliable bound/accounting if strict cap | No automatic billable dispatch under a strict cap with inadequate accounting. Unaffordable required verification blocks start. Unknown-cost advisory work requires explicit uncertainty acceptance/revised authorization; it cannot claim the strict cap. |
| 5. Delegation economics | Eligible alternatives; bounded isolated unit; all overhead included; evidence of plausible benefit | Prefer eligible direct work. If current model is ineligible, recommend eligible escalation or block; economics cannot reintroduce an ineligible model. |

Selection: **direct**, **delegate**, **recommend escalation**, **blocked**. Execution outcomes: **recommendation only**, **accepted**, **unverified**, **blocked**, **failed**, **cancelled**. A recommendation is not dispatch approval. Empty candidate sets remain empty, including excluded, unavailable, all-cooldown and unknown-required-capability cases. Eligible overrides may change preferences but never vetoes.

## Accounting contract

Total spend is the sum of **every** billable planner/router, framing/context, execution, failed/cancelled attempt, review/verifier, repair/escalation, re-priming and tool charge. Do not double count: if an aggregate escalation estimate includes earlier sunk attempts, identify them and avoid adding them again. Estimates/predicted success are separate from observed charges and verified outcomes. No universal success coefficients; publish calibration/sample basis if later used.

Keep cash/currency, subscription quota, local resources, latency, research credits and operator effort separate. No invented conversion or cash savings from hypothetical cache credits. Price records need source, units, input/output distinction, revision and timestamp. Missing pricing is not a free model. Failed/timeout/cancelled calls may still be billed.

Strict caps require a host with conservative billable limits, reservation before dispatch, atomic shared allocation, reconciliation and retained uncertain charges. Token heuristics, prompt instructions and estimates alone cannot guarantee caps. Under uncertainty keep reservations until reconciled; do not release funds on cancellation alone. Restart must inspect incomplete attempts before more work.

Cost per verified successful task = all assigned trial spend (including failed/blocked/cancelled attempts) / accepted task count under the frozen rubric. With zero successes it is **undefined**, not zero. With missing accounting it is incomplete/unknown, not a savings result. Report counts, blocked work, failures and severe defects beside the ratio.

## Verification, retries and side effects

- Define transport/protocol/business acceptance for each exact contract. HTTP 200, nonempty text and confidence are insufficient. A valid tool call may be intermediate, not final task success; a refusal is acceptable only when the task rubric expects it.
- Before any retry or switch establish replay class, request acceptance, commitment state, remaining attempt/deadline/budget and fresh eligibility. Retryability is not decided by status code alone.
- A replay-safe, known-unaccepted request may retry within authorization/bounds. Side-effecting dispatch with unknown acceptance, unresolved tools, ambiguous media creation or committed semantic stream output is terminal for automatic replay; reconcile on the original route and seek operator approval where required.
- Cancellation is not proof of nonacceptance, zero charges or rollback. Do not hedge/fan out side effects.
- Retry/fallback/repair must run the same permission, capability, verification and affordability gates. A verifier exception is not success. A circuit breaker may stop/escalate, not silently accept cheap unverified output.
- Host acceptance tests must observe the actual callsite and **zero dispatch/zero transmission** on rejection, not only pure selectors or recreated mocks.

## Context, cache and receipts

Preserve authoritative references, pinned revision, exact code indentation/fences, unresolved requirements and contradictions. A truncated summary is not the source; request missing evidence. Do not normalize code whitespace to gain cache hits or shorten prompts. Cache decisions only when authorized; fingerprint exact relevant task/content plus policy, authorization, privacy, catalog/capability, verification and price revisions. Invalidate when any changes. Hashes can remain sensitive and must follow data-retention policy.

Do not send full histories/secrets to a remote classifier. Eligibility precedes cache economics. Stickiness is a preference only: privacy, capability, context limits and explicit eligible override can break it. Claimed warm cache discounts need matching session/namespace evidence and actual billing basis; generic cache-hit averages do not imply future savings.

Receipts contain opaque task/policy references, recommended and observed identities, authorization revision, checks/evidence, attempt/commit/recovery status, accounting basis and uncertainty. No raw prompts, source bodies, API keys, authorization headers or credential-bearing endpoints. Keep secrets in host credential storage, outside routing data.

## Consumer boundaries

Research-Kit retains collector/builder separation, evidence/handoff gates, feature freeze, measurement-first decisions, paid-spend/red-suite stops and existing orchestrator authority. A separate reviewed adoption decision must reconcile ADR-0117/0145/0146 and lead-orchestrator/auto-build rules before any changed model policy; this skill does not supersede them.

Moonzila remains responsible for approved profiles, privacy/egress, reviewed effects, dispatch adapters, Stop, durable reservations and recovery. Existing-preview display can be inference-free; recommendation generation cannot be assumed free/offline. Pin policy and workspace/conversation revisions, invalidate stale recommendations and recheck before prompt bytes.
