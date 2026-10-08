# SmartRouter: remade development plan

Date: 2026-10-08. Status: **plan-and-skills preview in draft PR #2**.

Authorized delivery: corrected plan plus three usable, independently authored MIT-licensed skills, references and templates. No executable router, paid/live evaluation, Research-Kit or Moonzila modification, or merge. This document specifies future milestones; it does not claim they ran. The [canonical skill](../skills/smart-router/SKILL.md) and its linked contract are the sole SmartRouter selection authority; this roadmap explains development, not competing runtime rules.

## 1. Goal and success measure

Reduce **total cost per verified successful task**, subject to unchanged task acceptance, safety, privacy and project governance. Do not optimize token price, tier labels, self-confidence or task refusal alone. Count routing/planning, briefs/context, execution, failed attempts, verification/review, repair/escalation, re-priming and billable tools. Report completion/blocking, severe defects, uncertainty, latency and operator effort alongside cost.

Cost per verified successful task = all assigned trial spend / accepted task count under the frozen rubric. Zero successes means **undefined**, not zero. Missing billable usage means incomplete/unknown economics; no savings claim. Cash, subscription quota, local resources, research credits and effort have separate units, with no invented conversions.

Portable skills come first; hosts own actual authorization, model identity/dispatch, privacy enforcement, billing and recovery. A prompt cannot switch its own model, guarantee client support, enforce a cap or guarantee correctness. One model does not imply eligibility.

## 2. Current preview package and limits

| Artifact | Purpose | Current limit |
| --- | --- | --- |
| [smart-router](../skills/smart-router/SKILL.md) | Canonical ordered routing gates, brief/result workflow | Recommendation instructions, not a provider adapter |
| [smart-router-review](../skills/smart-router-review/SKILL.md) | Evidence-backed blocker review | Does not merge or validate unrun runtime tests |
| [smart-router-eval-prep](../skills/smart-router-eval-prep/SKILL.md) | Four-arm protocol and promotion preparation | Does not run trials or authorize money/egress |
| [Scenario fixtures](../skills/smart-router/references/scenarios.md) | Concrete manual acceptance walkthroughs | Synthetic, not live performance/billing evidence |
| [Survey](ROUTER_SURVEY.md) | Pinned source/test/license findings from 13 repositories | Read-only inspection, not reproduced benchmark or kit evidence corpus |
| [Preview review](PREVIEW_REVIEW.md) | Packaging/manual review record and limitations | Separate from future executable release certification |

Keep the three sibling skill directories together at a pinned reviewed revision with LICENSE. Frontmatter follows Agent Skills; descriptions drive discovery, references load on demand, bodies stay compact. No installer, scripts, provider gateway, hosted service, payment wallet, automatic download, independent orchestrator, parallel scheduler or consumer configuration is introduced. No `allowed-tools` metadata preapproves actions.

Acceptance: required names/descriptions/frontmatter valid; relative links resolve; examples/templates/scenarios coherent; one authority; license scope clear; no secrets or upstream code copied; manual scenario review recorded. Packaging success alone cannot certify semantic safety.

## 3. Seven review findings: corrections and blocking acceptance

| Finding | Corrected rule | Required acceptance evidence |
| --- | --- | --- |
| F1: release waivers | Unresolved safety/permission defects, contradictory authority, failed/missing required checks and missing redistribution permission are **release blockers**. Disclosure is not a waiver. Nonblocking limitations may be reported. | Review names each hard gate and evidence/disposition. Any blocker yields Request Changes/Reject, irrespective of score/average. No unknown upstream license is used to redistribute copied material. |
| F2: unknown cost | Strict cap + inadequate prices, billable bounds or accounting => **no automatic billable dispatch**, including direct/planner/reviewer. Advisory uncertainty needs explicit acceptance and revised authorization if the original cap cannot be guaranteed. Unknown is not zero. | S06-S08/S19/S21; show concrete unknown-price and unaffordable-review outcomes. Later host tests observe zero sends on cap rejection and retained uncertain charges. No unknown-cost savings. |
| F3: incomplete precedence | Permissions/privacy/workflow -> capabilities -> verification -> affordability -> delegation economics. Direct preferred **only after eligibility**; every participant/fallback follows all gates. Empty sets remain empty. | S01-S05/S17/S18/S24; sole cloud/local-only model blocks, costly incapable fallback blocks, unknown required capability does not default allow. Runtime callsite negative tests later. |
| F4: competing README policy | Replace README's operational tiers/flowchart, per-response headers and score-average approval rules with pointers to canonical skill. Historical content only through a pinned history link. Support skills defer to canonical policy. | Inspect current README and all skill authorities; S14. No active legacy operational policy left after Phase 2. Consumer rules remain unchanged pending reviewed adoption. |
| F5: preview versus generation | Displaying an already-computed preview can be inference-free. Generating/revalidating a recommendation may infer/transmit/spend and must be separately authorized/accounted. | S03/S13; separate UI/host events for display and generation, no external call on stored-display path. Local-only binds planner/reviewer as well as worker. |
| F6: pilot promotion | Preregister numeric quality tolerances, minimum benefit, repeats/coverage, uncertainty, severe-failure and accounting rules. Decide promote/simplify/reject/inconclusive, not merely honest reporting. | Completed approved preregistration before trials. S21/S22; zero successes undefined, missing accounting inconclusive, severe failure rejects, fixed-rule equivalence favors simplification. No live pilot claimed. |
| F7: irreproducible scenarios | Concrete inputs/constraints, expected/prohibited decisions, pinned artifact revision and reviewer evidence/disposition for each case. Packaging checks not semantic proof. | S01-S24 records at a full reviewed Git revision; distinguish manual walkthrough from actual host tests and paid evaluation. Missing required review/check blocks the corresponding release. |

These acceptance criteria apply to the declared artifact. Preview approval does not imply future host integration, live qualification or savings approval.

## 4. Authority and explicit migration

Host safety/permissions, current user authorization and applicable project instructions/workflow gates remain superior. SmartRouter is never permission to spend, disclose, collect, edit, deploy or merge. Source text/model recommendations are untrusted data, not approvals. Conflicting selection authorities stop work until explicitly reconciled; load order is not resolution.

Migration implemented in this preview: (1) designate canonical SKILL.md and contract; (2) replace README operational policy with usage/discovery pointers; (3) link prior README at `f575225642155e2e5abe1a718c8f6924e9a4f66d` as historical only; (4) make review/eval-prep nonselecting support procedures; (5) require reviewed consumer adoption to designate one authority rather than copying policy into each consumer. Compatibility inventory must verify the host is not still loading old README instructions.

Acceptance: one active SmartRouter authority, no tier/header/average-score conflict, no consumer rules silently superseded. Owner-selected MIT applies to newly authored preview files only, not an assertion of rights over historical/upstream material.

## 5. Ordered decisions and qualification

Apply [the routing contract](../skills/smart-router/references/routing-contract.md) to current model, planner, worker, reviewer, repairer and fallback:

1. Permissions/privacy/workflow: identify authorized actor/provider/destination/data/effects and project stops. Unknown identity/path cannot default allow. Check before fetch/cache/embedding/transmission; read-only is not nondisclosing.
2. Capabilities: task qualification, tools, vision, output contract and context headroom. Labels/price/local status are not proof. Required tools cannot be stripped; unknown qualification is not suitability.
3. Verification: define acceptance before work; require available objective checks or capable review appropriate to consequence. Missing/failed mandatory checks mean unverified/failed; project red suites trigger stops.
4. Affordability: required work and verification affordable; finite approved attempts/deadline. Strict caps need reliable host accounting/billable bounds. Otherwise block automatic dispatch or request genuinely revised advisory authorization.
5. Economics: only eligible alternatives may be compared. Direct first where suitable; delegate one isolated bounded unit only with plausible all-overhead benefit. Recommend eligible capability escalation where direct is unsuitable; none eligible => blocked.

Advanced qualification is needed for architecture, ambiguity, auth, money, deletion/data integrity, concurrency and subtle correctness regardless of lines/files. No universal price ladder or numerical confidence threshold is introduced. Manual overrides cannot bypass any gate. Empty/all-unavailable/all-cooldown filters must not resurrect rejected candidates.

Acceptance: deterministic documented reasons for direct/delegate/escalation/blocked; current model no exception; unknown/nonqualified capability veto; future real-callsite zero-send tests on every hard rejection.

## 6. Do-not-delegate gate and context continuity

Do not create a team/classifier for trivial work, split tasks to demonstrate cheap routing, or add verification that simply repeats the whole task without benefit. Required consequential review cannot be removed to win economics. Strong planning + cheap worker + strong review + strong repair may cost more than direct.

Use one compact brief: objective, pinned sources, scope/effects, privacy, capabilities, acceptance, allowance, finite attempts and stop/escalation triggers. Preserve exact code structure, source references, contradictions, truncation and unresolved requirements. Summaries are not authoritative evidence. Workers request missing inputs; they cannot recursively delegate, spend, expand scope or bypass governance.

Start serially. Stable model assignment may preserve context/cache, but stickiness is subordinate to eligibility and context limits. Switch only at safe task boundaries unless an actual provider adapter proves exchange-state safety. Disjoint files do not isolate shared databases/dependencies/tests. No extra context engine is built now.

Future decision caches must fingerprint exact relevant content and policy/authorization/privacy/capability/verification/catalog/price revisions; whitespace normalization must not conflate code. Hashes can be sensitive. Generic cache-hit rates cannot claim specific warm-prefix savings; eligibility precedes cache economics and discounts require observed namespace/session/billing basis.

Acceptance: S02/S15/S16 and exact-content review; delegation benefit includes every overhead; no cash benefit from hypothetical cache credits or invented success probabilities.

## 7. Verification, failure and safe recovery

Predetermine acceptance: exact diff/invariants for mechanical edits; relevant tests/typecheck/build and behavior checks for code; fetched authoritative claims for research; constraints/alternatives/failure modes and appropriate review for architecture; adverse cases and capable independent review for consequential changes. Provenance gates prove provenance, not claim correctness. Numeric self-scores and routing confidence are not acceptance.

Transport/protocol/business checks depend on the exact request contract. HTTP 200 or nonempty response is insufficient; valid tool calls may be intermediate, structured/media outcomes need their own checks, refusals count only when the rubric expects them. Verifier exceptions are unverified, never accepted. Fallback results need identical acceptance.

Classify missing context, transport, reasoning, scope, permission, affordability and uncertain-effects failures separately. Project stops override repair ceilings. At most one identified same-tier repair only where expressly permitted; total attempts/deadline finite. Reasoning failure may recommend a better qualified eligible model, not necessarily more expensive. Strong models can still fail.

Retry/switch requires known replay class, acceptance/commit state, fresh eligibility and remaining authorization/budget/deadline. Side-effecting dispatch with unknown acceptance, unresolved tools, ambiguous media creation or committed semantic stream output forbids automatic replay/provider switch. Reconcile original operation. Stop/cancel does not prove rollback or zero bill. No hedging side effects.

Acceptance: S09-S12/S18/S20; later host tests instrument real dispatch/command/payment callsites, not just retry helpers or recreated selector logic. Verify Stop, restart, unknown effects and no-send boundaries with injected clocks/failures.

## 8. Budget, reservations and receipts

Skill-only allowances are advisory. Strict monetary guarantees require current unit-aware pricing, conservative billable usage limits, host reservations before dispatch, atomic shared allocation, reconciliation and retained uncertain charges. Token heuristics alone are not exact bounds. Unapproved cloud fallback is prohibited; local work has resource/time cost.

Required verification must fit before route start. Optional escalation is rechecked rather than reserved indefinitely without need. Failed/timeouts/cancelled calls count; retain unresolved charges/reservations through recovery. Restart inspects incomplete attempts before continued work. Never release on cancel alone or allocate the same money twice.

[Receipts](../skills/smart-router/assets/result-receipt.md) separate recommendation from actual host-observed identity, estimate from reported/unknown usage, assertions from observations and recommendation-only/accepted/unverified/blocked/failed/cancelled. No API keys/raw prompts/private bodies/authorization headers/credential URLs. Keep opaque pinned references, attempts, commitment/recovery, check evidence and cost basis. Unknowns remain unknown; no mandatory verbose headers.

Acceptance: all attempts/verifiers accounted once, units/freshness explicit, strict-cap rejection observable, uncertain charges retained, secret-free receipts, zero-success ratio undefined. Host billing remains unimplemented by the preview.

## 9. Survey recommendations and reuse policy

The [13-repository pinned survey](ROUTER_SURVEY.md) distinguishes README/marketing, source behavior, checked-in tests and tests actually run. No upstream repositories executed; no benchmarks reproduced; no models called. It is a planning source review, not a Research-Kit ledger-backed corpus or exploitation finding.

Adopt independently authored concepts: separated decision policy/host effects, capability filtering, exact active-tool requirements, conservative context boundaries, provenance and authorized small context, typed contract validation, replay/commit awareness, all-attempt ledger, transparent fixtures and real-callsite adverse tests. Use explicit no-candidate outcomes and preregistered measured qualification.

Reject patterns found in source: restoring empty filtered fleets, unknown-price=zero, missing identity/path default allow, verifier-error acceptance, cheap-only kill-switch success, below-floor quality fallback, arbitrary confidence constants, unsafe generic retries, whitespace-conflating cache keys and mock tests that recreate production decisions.

Do not adopt a meta-LLM classifier, provider gateway, x402 wallets, blockchain hedging/quorum, paid aggregator or heavy learning infrastructure for skills V1. MIT router-core is a later design reference, **not a dependency now**, and requires correcting fail-open paths before considering integration. AGPL reuse needs compatibility review; source-available/noncommercial/no-clear-grant material cannot be copied on an MIT assumption. No upstream code/assets are vendored in this preview.

Acceptance: pinned links for every repository, actual license-text caveats, source-versus-run-evidence labels; any later copy obtains redistribution/notice permission first. MIT choice for new SmartRouter work does not cure upstream gaps.

## 10. Reproducible validation

Packaging checks: exact approved path set, three Agent Skills frontmatters/names/length constraints, compact bodies, template presence, resolved relative links, UTF-8/line endings, no scripts/product code or secrets, valid MIT scope and remote byte equality. This checks structure, not semantic safety.

Manual review: every S01-S24 input/expected/prohibited outcome at a full candidate Git revision, evidence and disposition, seven-finding matrix and authority inventory. Record reviewer/date/actual reasoning in PREVIEW_REVIEW. Future executed tests must name command/cwd/environment/results and observe actual callsites; semantic phrase scans cannot prove safety.

A required failed check stops release. Fix/recheck; no averaging or disclosure waiver. Preview manual walkthrough is not live model qualification. Native Windows/client claims need their real environment. No typecheck/build suite exists in the reviewed README-only base; Markdown/template validation is applicable now, implementation tests later.

Acceptance: reviewer record complete; no unresolved hard blocker in preview scope; all future unimplemented capabilities labeled untested; remote file set/content and PR draft state verified.

## 11. Evaluation and promotion protocol

Use [eval-prep protocol](../skills/smart-router-eval-prep/references/protocol.md) with four arms: strong qualified directly, economical qualified directly, simple fixed rule, SmartRouter including all overhead. Same acceptance/privacy/effects; do not expose weak baselines to production secrets or consequential writes. Keep kit workflow constant.

Before trials freeze task/rubric/host/model/policy/catalog/price revisions, task categories, tuning/holdout, cache conditions, ordering/randomization, repetitions, hidden checks and qualitative grading. **Fill approved numerical values** for quality/acceptance loss versus strong direct, mandatory floors, minimum cost benefit, latency/review/effort bounds, D-vs-fixed equivalence margins, sample/coverage, uncertainty/confidence and threshold crossing. Blanks mean not ready. No copied universal .80/.85 confidence gate or marketing coefficient.

Freeze severe-failure stop/zero-tolerance rule, accounting completeness, blocked/cancelled allocation, drift handling, maximum attempts/cost/deadline and explicit data/spend authorization. All charges count. Zero successes => undefined; missing usage cannot establish savings.

Decisions in order: **reject/stop** severe or well-evidenced failing candidate; **inconclusive** accounting/precision/coverage/comparability gaps; **simplify** if safe direct/fixed rules meet requirements and router lacks meaningful incremental benefit; **promote narrowly** only with hard gates, holdout quality noninferiority/floors, minimum supported economic benefit and bounded latency/effort, including meaningful advantage over simpler safe alternatives. Publish negatives/uncertainty; do not retrofit thresholds. Promotion recommends separately approved adoption, not automatic merge/install.

Acceptance: preregistration ready and approved before authorized calls; complete ledger/report and frozen rule applied. No measured result exists in this preview.

## 12. Research-Kit adoption — separate later decision

No Research-Kit changes here. Governed by research-first roles/evidence/handoff, ADR-0117 feature freeze, ADR-0145 measurement-before-growth and ADR-0146 rejection of kit-owned routing. Existing lead-orchestrator defaults strongest for consequential roles and escalates model first; auto-build stops for money/red suites/secrets/permissions/mandate/merge even with standing mandate.

A future nested decision project must fetch/retain evidence under its own contract/ledger, pass its own applicable gates and produce reviewed handoff. External companion-only evaluation first; no contamination of the independent strong-prompt comparison. Builders do not collect. Routing cannot pass evidence gates or authorize build/spending.

Any adoption ADR designates one model authority, names exact restrictions superseded and reconciles orchestrator/stop rules; history remains unchanged. Existing deployment must preserve user skills and pinned versions; no second dispatch engine, kit routing command or speculative config.

Acceptance: approved narrowly scoped governance decision, evidence and external benefit; existing collector/builder/handoff/stops/role tables/discovery/drift checks unchanged except explicitly reviewed scope. This preview supplies no adoption permission.

## 13. Moonzila integration — staged later

No Moonzila changes here. Respect its approved roadmap/research/memory/mission priorities; ordinary chat need not become research. First advisory UI: requested profile, gate reasons, cost basis/unknowns, privacy destination, actual dispatch availability and pinned policy/workspace/conversation revisions. Display stored previews without inference; generate only with explicit permission/accounting; stale authority invalidates recommendations.

Next separately approved serial execution through existing adapters: privacy before prompt bytes, reviewed edits/commands, real local qualification/headroom, manual eligible overrides, Stop and durable attempt/reservation/settlement/recovery. No fabricated receipts/downloads. Reconcile incomplete calls after restart; switching only at tested safe boundaries. Local-only includes all auxiliary inference.

Only after serial safety and measured need consider shared reservations, dependencies, bounded concurrency/conflicts/group cancellation. Reuse existing context/result retrieval. A hosted engine is not the inevitable endpoint.

Acceptance: actual host no-send/privacy/approval tests, serial cancellation/restart/replay/accounting tests, real client environment, separately approved scope and measured benefit. Preview semantics do not satisfy these runtime gates.

## 14. Phases and blocking exit gates

| Phase | Deliverable | Exit gate |
| --- | --- | --- |
| 0: discovery | Instructions, scope, owner license choice, pinned survey/gaps | No guessed blocking facts; no copying without permission |
| 1: specification | Ordered gates, cost/verification/retry contract, seven-finding criteria | One coherent authority, explicit unknown outcomes and hard blockers |
| 2: plan-and-skills preview (this PR) | Three skills, references/templates, README migration, scenarios, review record | Valid packaging, manual semantic review at pinned revision, seven findings addressed, secret/license checks, draft PR no merge |
| 3: evaluation preparation | Filled approved numerical preregistration/host qualification/accounting | No blanks/unknown blocking facts; separate spend/egress approval still required |
| 4: authorized exploratory/holdout pilot | Four-arm measured report and ledger | Frozen promote/simplify/reject/inconclusive rule, complete accounting, no severe failure waiver |
| 5: optional kit companion | Separate nested decision/adoption ADR and pinned deployment | Governance and single-authority reconciliation; existing stops/gates preserved |
| 6: optional app advisory | Authorized generation and inference-free stored display | Separate paths; stale preview invalidation; no egress without permission |
| 7: optional app serial host | Adapters/accounting/Stop/persistence/recovery | Real-callsite privacy/capability/cap/replay/cancel/restart checks; qualified live evidence |
| 8: optional expansion/maintenance | Only justified concurrency/caches/learning/adapters | Measured need, compatibility/license review, repeated adverse tests and reviewed version updates |

Future phases are options, not commitments to implement all systems. Simplify/stop if direct is cheaper, fixed rules equally effective, accounting/dispatch absent, review repeats work or adoption weakens project stops.

## 15. Release gates and delivery

**Hard blockers:** unresolved safety/privacy/permission defects; competing authority; failed or missing required checks; missing redistribution permission; exposed secrets; unsupported runtime/enforcement/savings claims. Correct and recheck before releasing the affected artifact. Merely documenting them cannot yield approval. Nonblocking unimplemented future features may be labeled as limits of a preview.

Current delivery amends existing draft PR #2 on `docs/corrected-smartrouter-development-plan`, preserving observed parent/concurrent changes, verifying expected head before publication and using non-force branch update. No new PR/main update/merge. Upload only owned preview documents; credential in memory/header only, never in files/logs/URLs. Re-read PR/head/diff and verify remote bytes, changed-file set, draft/open/unmerged status and unchanged main after publishing.

Maintenance: consumer-pinned reviewed versions; no silent live downloads; changelog for policy changes; rerun scenario reviews and relevant runtime checks; freshness/provenance for capabilities/prices; respect retention/licensing. Users can disable routing and return to **eligible** manual selection.

## 16. Open decisions and deferred work

Resolved: plan-and-skills scope, three skill roles, MIT for new content, draft PR target and no merge. Open before pilots: tested host/model inventory, exact dataset, numeric tolerances/repeats/benefit/uncertainty, spend/egress approval and reliable accounting. Open before adoption: kit governance exception/reconciliation, companion-versus-bundled decision and Moonzila roadmap slot.

Deferred: provider/gateway SDK, paid classifier, learned task-quality model, context engine, hosted payments, adaptive caching, parallel teams, broad adapters and research-transport economics. Trigger is observed need plus new approved evidence, not upstream feature envy. No missing license/capability/price fact is silently guessed.

## 17. Sources and evidence limits

- [Pinned SmartRouter original policy](https://github.com/StepenkoAnatoli/SmartRouter/blob/f575225642155e2e5abe1a718c8f6924e9a4f66d/README.md); operationally superseded only in this preview, not consumers.
- [Agent Skills specification](https://agentskills.io/specification), inspected 2026-10-07; mutable format source, not runtime qualification.
- [Pinned routing survey](ROUTER_SURVEY.md): all 13 repository heads and source/test/license samples.
- [Research-Kit](https://github.com/StepenkoAnatoli/Research-Kit), reviewed governance/skills; re-read and fetch under its nested workflow before adoption.
- [Moonzila](https://github.com/StepenkoAnatoli/Moonzila), future host boundary; current policies must be revalidated before integration.

Source/static test inspection != tests run. This public survey is not a kit provenance corpus and must not be presented as one. No benchmark, measured saving, live capability, exploit or commercial license permission is inferred from README labels. Runtime/economic claims require the later authorized evidence specified above.
