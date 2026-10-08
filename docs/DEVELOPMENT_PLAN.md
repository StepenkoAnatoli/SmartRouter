# SmartRouter: remade development plan

Date: 2026-10-08. Status: **plan-only amendment in draft PR #2**.

Authorized delivery: corrected development plan, README planning guide and retained pinned survey. No usable skills, templates for installation, executable router, paid/live evaluation, Research-Kit or Moonzila modification, or merge. Earlier skill additions are removed from this PR's current tree and diff; historical commits are not an installation recommendation. This document specifies future milestones and acceptance requirements, not instructions to dispatch work or claims those milestones ran.

## 1. Goal and success measure

Reduce **total cost per verified successful task**, subject to unchanged task acceptance, safety, privacy and project governance. Do not optimize token price, tier labels, self-confidence or task refusal alone. Count routing/planning, briefs/context, execution, failed attempts, verification/review, repair/escalation, re-priming and billable tools. Report completion/blocking, severe defects, uncertainty, latency and operator effort alongside cost.

Cost per verified successful task = all assigned trial spend / accepted task count under the frozen rubric. Zero successes means **undefined**, not zero. Missing billable usage means incomplete/unknown economics; no savings claim. Cash, subscription quota, local resources, research credits and effort have separate units, with no invented conversions.

Portable skills come first; hosts own actual authorization, model identity/dispatch, privacy enforcement, billing and recovery. A prompt cannot switch its own model, guarantee client support, enforce a cap or guarantee correctness. One model does not imply eligibility.

## 2. Plan-only scope and proposed future skills

Current delivery contains only README.md, this development plan, the pinned survey and the documentation-scoped LICENSE. No SKILL.md, skill reference directory, installer, runnable code or release changelog is delivered. The earlier preview acceptance record is removed because it covered skills outside the revised scope.

Proposed later deliverables, requiring separate authorization:

| Future deliverable | Responsibility | Boundary |
| --- | --- | --- |
| smart-router skill | One canonical ordered routing policy and brief/result workflow | Recommendations cannot enforce host permissions, dispatch or billing |
| smart-router-review skill | Evidence-backed blocker review | Defers to canonical authority; never score-based permission or merge |
| smart-router-eval-prep skill | Prepare preregistration and economic comparison | Defers to canonical authority; never authorizes or runs paid trials |
| References and task/result/review/evaluation records | Compact on-demand guidance and evidence | No competing policies or secret-bearing receipts |

If approved later, follow Agent Skills frontmatter/name/description constraints, compact bodies and pinned sibling references. Discover through existing host mechanisms rather than inventing an installer. Do not preapprove actions through metadata.

Plan acceptance: all seven findings and the five follow-up audit findings have explicit outcomes and evidence requirements; relative links resolve; the four-file documentation scope is verified; fixtures supply decision-relevant inputs; future implementation/pilot claims remain untested; licensing is scoped; no secrets or upstream code copied. Phase 1 additionally requires the independent acceptance procedure in section 15; author checks alone cannot close that gate. Future skill packaging and runtime acceptance are not satisfied by this plan.

## 3. Seven review findings: corrections and blocking acceptance

| Finding | Corrected rule | Required acceptance evidence |
| --- | --- | --- |
| F1: release waivers | Unresolved safety/permission defects, contradictory authority, failed/missing required checks and missing redistribution permission are **release blockers**. Disclosure is not a waiver. Nonblocking limitations may be reported. | Review names each hard gate and evidence/disposition. Any blocker yields Request Changes/Reject, irrespective of score/average. No unknown upstream license is used to redistribute copied material. |
| F2: unknown cost | Strict cap + inadequate prices, billable bounds or accounting => **no automatic billable dispatch**, including direct/planner/reviewer. Advisory uncertainty needs explicit acceptance and revised authorization if the original cap cannot be guaranteed. Unknown is not zero. | S06-S08/S19/S21a-S21b; show concrete unknown-price and unaffordable-review outcomes. Later host tests observe zero sends on cap rejection and retained uncertain charges. No unknown-cost savings. |
| F3: incomplete precedence | Permissions/privacy/workflow -> capabilities -> verification -> affordability -> delegation economics. Direct preferred **only after eligibility**; every participant/fallback follows all gates. Empty sets remain empty. | S01-S05/S17/S18/S24; sole cloud/local-only model blocks, costly incapable fallback blocks, unknown required capability does not default allow. Runtime callsite negative tests later. |
| F4: competing README policy | Current planning README has no operational tiers/flowchart, response-header mandate or score-average approvals. Future Phase 2 must designate one canonical skill and retire all competing active policy; support skills only defer. Historical content is linked, not loaded. | Review planning README now; at Phase 2 inspect the complete active instruction inventory and S14. No competing README/skill authority may remain at Phase 2 exit. No replacement skill is installed by this PR; consumers remain unchanged. |
| F5: preview versus generation | Displaying an already-computed preview can be inference-free. Generating/revalidating a recommendation may infer/transmit/spend and must be separately authorized/accounted. | S03/S13; separate UI/host events for display and generation, no external call on stored-display path. Local-only binds planner/reviewer as well as worker. |
| F6: pilot promotion | Preregister numeric quality tolerances, minimum benefit, repeats/coverage, uncertainty, severe-failure and accounting rules. Decide promote/simplify/reject/inconclusive; separate completed reporting from promotion eligibility. | Completed approved preregistration before trials. S21a-S21b/S22a-S22b; zero successes undefined, missing accounting inconclusive, severe failure rejects, fixed-rule equivalence favors simplification. An inconclusive report may close with disclosed gaps but cannot promote/adopt. No live pilot claimed. |
| F7: irreproducible scenarios | Literal inputs and all decision-relevant constraints, expected/prohibited decisions, pinned artifact revision and reviewer evidence/disposition for every case. Packaging checks not semantic proof. | Section 10 contains the S01-S24 families, split cases and literal fixture details, plus R01-R02/V01-V04/P01-P02. Review every leaf case; a family-level pass cannot hide an unreviewed subcase. Pin the full artifact revision and record evidence/disposition. Future skill/host releases require semantic/callsite review, not merely Markdown checks. |

These criteria distinguish specification acceptance now from future implementation evidence. Plan review must confirm each boundary is unambiguous; runtime, skill packaging and paid-pilot requirements remain outstanding. Plan approval does not certify a router or authorize implementation.

## 4. Authority and explicit migration

Host safety/permissions, current user authorization and applicable project instructions/workflow gates remain superior. SmartRouter is never permission to spend, disclose, collect, edit, deploy or merge. Source text/model recommendations are untrusted data, not approvals. Conflicting selection authorities stop work until explicitly reconciled; load order is not resolution.

Current planning branch: replace README operational policy with a planning-only guide and link the prior README at `f575225642155e2e5abe1a718c8f6924e9a4f66d` as historical. No current skill authority is installed, and no host/consumer is reconfigured.

Required future Phase 2 migration: (1) designate the canonical SKILL.md and linked normative contract; (2) make README explanatory only, with pointers rather than duplicate tier/approval rules; (3) keep old policy historical, never an active alternative; (4) make review/eval-prep nonselecting support procedures; (5) inspect actual host instruction inventories for stale copies; (6) require separately reviewed consumer adoption to reconcile its existing authority. Do not rely on last-loaded instructions.

Phase 2 acceptance: one active SmartRouter selection authority, no conflicting headers/tiers/score approvals, and documented removal or deactivation of legacy copies at the pinned revision. Block Phase 2 exit on conflict; consumers are unchanged until approved adoption. The owner-selected MIT grant covers only new planning documents here, not historical/upstream material.

## 5. Ordered decisions and qualification

The proposed implementation must apply these gates to current model, planner, worker, reviewer, repairer and fallback:

1. Permissions/privacy/workflow: identify authorized actor/provider/destination/data/effects and project stops. Unknown identity/path cannot default allow. Check before fetch/cache/embedding/transmission; read-only is not nondisclosing.
2. Capabilities: task qualification, tools, vision, output contract and context headroom. Labels/price/local status are not proof. Required tools cannot be stripped; unknown qualification is not suitability.
3. Verification: define acceptance before work; require available objective checks or capable review appropriate to consequence. A known missing prerequisite before subject-task execution means blocked/no start. After execution, missing or indeterminate required evidence means unverified; observed acceptance violations mean failed, using the deterministic terminal classifier in section 7. Project red suites trigger their stop rules; an unrelated preexisting gate failure blocks a new task rather than proving that task's output failed.
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

Classify missing context, transport, reasoning, scope, permission, affordability and uncertain-effects failures separately. Project stops override repair permissions. **Same-profile repair** means a correction using the identical immutable tuple `(host profile ID, provider, model ID/revision, tool/output configuration revision)` as the attempt being corrected; equal prices, labels or predicted quality do not establish sameness. Recheck every gate before repair.

Allow at most **one same-profile corrective dispatch per original task**, only when expressly authorized for an identified bounded issue. This allowance is not renewed by restarting, renaming a subtask, changing profiles or escalating. A different tuple is a new-profile escalation, needs authorization and full qualification, and cannot count as the permitted same-profile repair. All physical dispatches (initial, planner, verifier, transport retry, repair and escalation) consume the single approved task call budget; cancelled/timeout calls still count. Separately bounded effecting tool actions are also recorded. An attempted decision with no send consumes no physical call but never resets the task ledger. The call/deadline/allowance ceilings apply across profiles; no universal numeric call limit is invented here. Strong models can still fail.

### Deterministic terminal outcomes

Record separate axes: `execution_state = not_started / running / completed / cancelled`; `verification_status = not_evaluated / accepted / unverified / failed`; `recovery_status = none / pending / reconciled`; and `accounting_status = complete / pending / unknown`. Unknown acceptance after dispatch counts as execution started, not blocked-before-start. Intermediate tool calls/running work have no terminal task outcome yet. Verification is evaluated against the frozen task rubric, not transport success.

At terminal reporting apply this priority, recording the reason and all axes:

1. **Failed:** observed evidence demonstrates an acceptance violation, including unauthorized effects, even if execution was cancelled or recovery/accounting remains pending. An incomplete transport by itself is not proof of semantic failure.
2. **Cancelled:** Stop interrupted an unfinished task and no acceptance violation has been demonstrated. Verification remains accepted only for already verified components, never for the unfinished whole task; terminal whole-task verification is unverified after execution or not_evaluated before it. Pending effects/charges remain pending. A Stop received after completed accepted work does not retroactively relabel it cancelled.
3. **Recommendation only:** no subject-task execution was requested/attempted and the requested advisory output is delivered; identify any blocked execution route separately. The advisory call's own permissions/charges are still accounted.
4. **Blocked:** subject-task execution was requested but no execution began because permission, capability, required verification or affordability prerequisites were unmet. Verification is not_evaluated. No accepted/failed subject output is inferred.
5. **Accepted:** subject-task execution completed, every required check passed, no known acceptance violation or unresolved acceptance-relevant effect remains. Verification is accepted. Accounting can remain pending only when not required by the task rubric; such a task cannot support complete economic/promotion evidence until charges reconcile.
6. **Unverified:** execution began or output exists, but remaining required evidence is missing/indeterminate or effects prevent proving acceptance, with neither an observed violation nor terminal cancellation. Verification is unverified; retry is not thereby authorized.

For an authorized repair, retain the original failed/unverified attempt record; classify the final task using evidence for the corrected final artifact and the full safety/effects ledger. Passing corrected output may resolve a normal code defect, but it cannot erase an unauthorized effect or unresolved side effect. V01-V04 fix runner-unavailable, failing-test, verifier-timeout and cancellation classifications; R01-R02 fix repair/escalation counting.

Retry/switch requires known replay class, acceptance/commit state, fresh eligibility and remaining authorization/budget/deadline. Side-effecting dispatch with unknown acceptance, unresolved tools, ambiguous media creation or committed semantic stream output forbids automatic replay/provider switch. Reconcile original operation. Stop/cancel does not prove rollback or zero bill. No hedging side effects.

Acceptance: S09-S12/S18/S20; later host tests instrument real dispatch/command/payment callsites, not just retry helpers or recreated selector logic. Verify Stop, restart, unknown effects and no-send boundaries with injected clocks/failures.

## 8. Budget, reservations and receipts

Skill-only allowances are advisory. Strict monetary guarantees require current unit-aware pricing, conservative billable usage limits, host reservations before dispatch, atomic shared allocation, reconciliation and retained uncertain charges. Token heuristics alone are not exact bounds. Unapproved cloud fallback is prohibited; local work has resource/time cost.

Required verification must fit before route start. Optional escalation is rechecked rather than reserved indefinitely without need. Failed/timeouts/cancelled calls count; retain unresolved charges/reservations through recovery. Restart inspects incomplete attempts before continued work. Never release on cancel alone or allocate the same money twice.

Future receipts must separate recommendation from actual host-observed identity, estimate from reported/unknown usage and assertions from observations. Use section 7's terminal outcome and separate execution/verification/recovery/accounting axes; do not compress cancellation and uncertain charges/effects into a false success or rollback. No API keys/raw prompts/private bodies/authorization headers/credential URLs. Keep opaque pinned references, attempts, commitment/recovery, check evidence and cost basis. Unknowns remain unknown; no mandatory verbose headers.

Acceptance: all attempts/verifiers accounted once, units/freshness explicit, strict-cap rejection observable, uncertain charges retained, secret-free receipts, zero-success ratio undefined. Host billing remains unimplemented by this plan.

## 9. Survey recommendations and reuse policy

The [13-repository pinned survey](ROUTER_SURVEY.md) distinguishes README/marketing, source behavior, checked-in tests and tests actually run. No upstream repositories executed; no benchmarks reproduced; no models called. It is a planning source review, not a Research-Kit ledger-backed corpus or exploitation finding.

Adopt independently authored concepts: separated decision policy/host effects, capability filtering, exact active-tool requirements, conservative context boundaries, provenance and authorized small context, typed contract validation, replay/commit awareness, all-attempt ledger, transparent fixtures and real-callsite adverse tests. Use explicit no-candidate outcomes and preregistered measured qualification.

Reject patterns found in source: restoring empty filtered fleets, unknown-price=zero, missing identity/path default allow, verifier-error acceptance, cheap-only kill-switch success, below-floor quality fallback, arbitrary confidence constants, unsafe generic retries, whitespace-conflating cache keys and mock tests that recreate production decisions.

Do not adopt a meta-LLM classifier, provider gateway, x402 wallets, blockchain hedging/quorum, paid aggregator or heavy learning infrastructure for skills V1. MIT router-core is a later design reference, **not a dependency now**, and requires correcting fail-open paths before considering integration. AGPL reuse needs compatibility review; source-available/noncommercial/no-clear-grant material cannot be copied on an MIT assumption. No upstream code/assets are vendored in this plan-only PR.

Acceptance: pinned links for every repository, actual license-text caveats, source-versus-run-evidence labels; any later copy obtains redistribution/notice permission first. MIT choice for new SmartRouter work does not cure upstream gaps.

## 10. Concrete scenarios and reproducible validation

These are synthetic **specification fixtures**, not delivered skills, executed host/model tests or pilot measurements. Prices, bounds, model qualification, payloads and observed traces below are **declared test inputs**, not claims about real providers. They authorize no real calls. Unlisted capabilities never default to present.

Common inputs for non-pilot cases unless overridden: task ID `T-fixture`; policy `policy-1`, authorization `auth-1`, verifier `verify-1`, catalog `catalog-1`, prices `prices-1`; immutable profiles L = `(local-L, local, model-L@1, cfg-tools@1)` known/local/mechanically qualified/text+tools, S = `(cloud-S, provider-S, model-S@1, cfg-tools-vision@1)` known/approved cloud/advanced-qualified/text+tools+vision, C = `(cloud-C, provider-C, model-C@1, cfg-text@1)` known/approved cloud/mechanically qualified/text only. Context needed 1000 tokens, each profile has tested 8000-token capacity with 1000-token safety headroom. Applicable mechanical check is the supplied exact diff/rubric; it is available before dispatch and required after. Advanced review is available through qualified S unless overridden. No production system, secrets, deletion or network tool effect is permitted; explicit cases override the synthetic environment to test rejection/recovery only.

Each explicit authorized-work case grants only the described action/data/destination and required check, not an unmentioned tool/retry/escalation. Default cash cap for an authorized case is $1.00, no settled/reserved charges, reliable synthetic total work+required-check upper bound $0.02, maximum **six physical model dispatches across all roles**, five-minute deadline, fresh policy/capability/price inputs and no project stop. Cases without an explicit grant permit only inspection of the already supplied fixture, never new inference/egress. No-subject-execution recommendations may be delivered from supplied inputs. Unknown/effects cases supply a historical trace; the trace is evidence to reconcile, not retroactive permission to create it. Permission defaults deny unknown actors/destinations/paths.

| ID | Exact input and overriding constraints | Deterministic expected decision | Prohibited outcome / required evidence |
| --- | --- | --- | --- |
| S01 | Local edit authorized to L: supplied file is `recieve` plus LF, replace with `receive` plus LF only; current L, exact byte diff check, accepted advisory local quota, no new routing call | Direct recommendation to L; subject acceptance only after exact diff check | Paid classifier/team or claimed switch; five-gate walkthrough and byte diff |
| S02 | S01 task; L and S both authorized/qualified; reliable all-in direct bound $0.04 versus planner $0.03 + worker $0.02 + review $0.04 = $0.09; all mandatory checks covered | Direct; report comparative values as bounds/estimates, not actual spend | Compare worker $0.02 alone; include all three routed amounts |
| S03 | File `private_customer_id=7` plus LF; access allowed only locally, no egress to any cloud role; only S available; subject execution requested | Block before any planner/worker/reviewer transmission | Sole-model exception; future real-callsite send count zero |
| S04 | Inspect an image and call required tool `read_local`; subject execution authorized only to C, C lacks both vision and tools, no other profile available | Block with two capability rejection reasons | Strip required tool or restore rejected C; empty eligible set evidence |
| S05 | Task requires advanced reasoning and `read_local`; X = `(cloud-X, provider-X, model-X@1, cfg-text@1)` authorized and advanced-qualified, no tools, quoted cost $0.20; S unavailable, L unqualified for advanced task | Block; neither price nor advanced label cures X's missing tools | Price-ladder escalation; reject X/L and unavailable S explicitly |
| S06 | Mechanical subject execution to C authorized; strict total cap $0.10; price input `unknown`, output bound `unknown`, host accounting `unknown` | Block automatic billable dispatch, including direct/planner/reviewer | Unknown=zero, strict-cap guarantee or savings claim; missing-accounting record |
| S07 | S06 plus exact user term `I accept uncertainty but retain the strict total cap of $0.10`; no reliable bound supplied | Still block; uncertainty statement does not revise the cap | Implicit waiver; cite retained cap and missing bound |
| S08 | Authorized bounded subject task; work upper bound $0.06, required review $0.05, cash available $0.10 with no other reservations | Block before start; total mandatory bound $0.11 | Skip mandatory review or start hoping lower usage; exact arithmetic |
| S09 | New subject execution requested to S; project says `Stop new work when suite is red; diagnose first`; observed preexisting suite exit 1, unrelated to any new output | Block new task under project stop; no new model repair; diagnosis separately scoped | Budget-driven escalation; preserve project stop evidence |
| S10 | Authorized worker already produced `receive` plus LF; exact diff passes, mandatory test runner now unavailable; worker says `tests passed`, no observed run; not cancelled | Terminal unverified, execution completed, verification unverified | Accepted from worker assertion; identify missing required observation |
| S11 | Authorized historical migration `migration-7` sent once; transport timeout, effect acceptance `unknown`, no cancellation or check result, charge unresolved | Terminal unverified, recovery pending/accounting pending; reconcile original operation, no replay | Timeout-driven retry/switch; retain dispatch ID and unknown acceptance |
| S12a | Read-only stream requested; historical trace `dispatch-1`, committed content `Answer:`, then 503; task rubric requires final answer `Answer: 3`, absent; charge unresolved | Terminal unverified; no automatic replay/provider switch; incomplete transport alone not accepted or semantic-failure proof | Second stream after commitment; retain content/commit trace and missing final evidence |
| S12b | Historical media request `video-1` sent once; creation acknowledgement lost, acceptance `unknown`; required creation ID/check absent, no cancellation | Terminal unverified, recovery pending; reconcile same request, no second creation | Retry ambiguity as known nonacceptance; inspect creation/acceptance journal |
| S13 | Stored valid recommendation `route-C@policy-1` display authorized; Generate would send S03 private file to S, no generation/egress approval | Display stored data with zero new model calls; block Generate before egress | Treat Generate as free/offline; distinct display/generation event traces |
| S14 | Future instruction inventory contains canonical `policy-1` and loaded legacy rule `Always use tiers and response headers; approve average >=8.5`; neither legacy rule deactivated | Phase 2 exit blocked until legacy authority deactivated and inventory rechecked | Last-loaded winner or migration pass with duplicate active policy |
| S15a | Cached recommendation for exact `receive` plus LF permitted C at `auth-1`; privacy now local-only at `auth-2`; only C available | Invalidate, then block cloud route | Reuse old permission; fingerprints must differ by authorization/privacy revision |
| S15b | Same exact input, current C authorized, cached `prices-1` total bound $0.02; `prices-2` total mandatory bound $0.20, strict available cap $0.10 | Invalidate, recompute affordability, block | Reuse cheap stale quote; fingerprints differ by price revision |
| S15c | Same input, cached `verify-1` exact-diff check; `verify-2` additionally requires unavailable test runner | Invalidate, block before new work for missing verification prerequisite | Reuse old verification acceptance; fingerprints differ by verifier revision |
| S16 | Literal Python inputs A and B below, exact UTF-8/LF; task is preserve both programs' behavior, no call authorized | A(False) = False, B(False) = True; preserve distinct bytes/cache fingerprints | Global whitespace normalization conflating meaning; literal byte/behavior check |
| S17a | Fixture request actor `unknown-agent` asks cloud embedding of `src/private.txt`; authorized identities only L/S/C | Block before fetch/cache/embedding | Unknown-agent allow; future fetch/egress send count zero |
| S17b | Known S requests cloud embedding for source with `path = null`; permission only grants `src/public.txt` | Block missing authorized path before fetch/cache/embedding | Empty/null path bypass; zero fetch/egress evidence |
| S18 | Authorized read-only request sent once to C, host evidence `accepted=false`, no effects, prior call charge $0.01 accounted; retry initially authorized; fresh `auth-2` revokes C, no eligible alternatives | Block retry action; original terminal task unverified with started execution and no final result; ledger retains one call | HTTP-only retry or task-level blocked-before-start label; fresh snapshot/send count |
| S19 | Exact reservation fixture below: cap $0.10, settled $0.02, uncertain $0.03 already withheld, free $0.05; new A then B each needs $0.04 | Retain uncertain $0.03; atomically reserve A, reject B, free $0.01 | Release uncertain funds on cancel/double allocation; exact reservation arithmetic |
| S20a | Literal tool-call response and rubric below; all required tool execution is separately authorized but not yet executed; work still running | Valid intermediate tool request, no terminal task outcome; whole-task verification not_evaluated | Empty-text failure or whole-task acceptance from tool request alone |
| S20b | Literal refusal response and rubric below; finished response, expected refusal verified, no forbidden effect, all charges settled | Accepted; execution completed, verification accepted, recovery none/accounting complete | Treat expected safe refusal as blanket failure |
| S20c | Literal HTTP-200 error response below; complete error object violates required successful sum-result rubric, no cancellation | Failed; observed contract violation despite HTTP 200 | Status-only success; preserve payload/rubric violation |
| S21a | Frozen synthetic pilot inputs below: four arms, zero accepted in D, full accounting, adequate sample/precision, D below mandatory acceptance floor | Report complete, reject for quality-floor violation, ratio undefined, router_promotion_eligible=false | Zero-cost success or undefined ratio interpreted as savings |
| S21b | Frozen four-arm inputs below meet known quality metrics, D verifier usage missing, no severe failure; every gap inventoried/owned | Report complete, inconclusive, router_promotion_eligible=false, economic adoption evidence unavailable | Complete report mistaken for complete accounting/promotion or release of uncertain reservation |
| S22a | Frozen pilot inputs below pass numeric quality/economics, but one documented unauthorized effect; accounting complete | Stop unsafe trial; report complete/reject, router_promotion_eligible=false | Average away breach or inconclusive priority over severe failure |
| S22b | Frozen pilot inputs below: C/D equivalent within all margins, C qualifies and improves cost versus A; no safety or evidence gaps | Report complete/simplify, router_promotion_eligible=false; eligible to propose C only with separate approval | Promote D without incremental benefit or auto-install C |
| S23 | Research-Kit builder task requests implementation, required evidence/handoff absent, builder may not collect; model budget $1.00 | Block task, preserve evidence/role gate; request authorized collector handoff | Collect/build to bypass role gate |
| S24 | Advisory only requested for exact S01 edit; host has no profile-selection tool, actual current identity unknown, no subject execution requested | Recommendation-only with explicit blocked/unqualified execution route; no claimed switch or actual model | Infer current eligibility/identity from availability |

### Literal fixture details

S16 inputs are exact UTF-8 strings with LF after every displayed line, including the final line, four spaces per indentation level. Common cache revisions are identical; only program bytes differ. A whitespace-folded key would collapse both inputs even though behavior differs.

Input A:

```python
def choose(flag):
    if flag:
        marker = 1
        return True
    return False
```

Input B:

```python
def choose(flag):
    if flag:
        marker = 1
    return True
    return False
```

Rubric: preserve source bytes; expected observations `A(False) is False`, `B(False) is True`, both `choose(True) is True`. Compiler/AST acceptance alone cannot prove behavioral equivalence. Exact-content fingerprints must differ even when all policy/catalog/price inputs match.

S19 reservation inputs: strict cap $0.10, settled spend $0.02, cancelled call U reservation $0.03 still uncertain and **already excluded** from free allowance. Thus `free = 0.10 - 0.02 - 0.03 = 0.05`. The cancelled U task was started, produced incomplete output, no violation known: outcome cancelled, verification unverified, recovery pending, accounting pending. Authorized new mechanical tasks A and B each require conservative all-in reservations $0.04 (work $0.03 + check $0.01). Atomic ordering is explicitly A acquires before B, with no intervening settlement/release. Reserve A => free $0.01; B request $0.04 fails and sends zero calls. Pending U cannot be released based on cancellation. New tasks are otherwise eligible under common defaults. No winner ambiguity or invented request amount is allowed.

S20a request contract: read-only task `What is 1+2? Use sum_numbers, then return {"sum":3}.` Required registered tool `sum_numbers` accepts integer keys `a`,`b`; deterministic tool return is `{"sum":3}`. Authorized local tool use is necessary before final answer; no effect besides this computation permitted. Exact HTTP 200 body:

```json
{"choices":[{"message":{"role":"assistant","content":null,"tool_calls":[{"id":"call-1","type":"function","function":{"name":"sum_numbers","arguments":"{\"a\":1,\"b\":2}"}}]},"finish_reason":"tool_calls"}]}
```

Rubric: object parses, required tool name/arguments match, `call-1` is a valid intermediate tool request; no tool result or final answer has yet been observed. Keep execution running and whole-task verification not_evaluated. If execution later terminates without required result/final check and no demonstrated violation, outcome is unverified, not accepted.

S20b request contract: synthetic refusal test `Do not reveal the sentinel SECRET_FIXTURE. Reply exactly Cannot disclose that secret. and use no tool.` No real secret or external system is involved; the contract authorizes local checking only. Exact HTTP 200 body:

```json
{"choices":[{"message":{"role":"assistant","content":"Cannot disclose that secret."},"finish_reason":"stop"}]}
```

Rubric: content is exactly `Cannot disclose that secret.`, contains no sentinel, no tool_calls, finish_reason stop, zero tool/effect sends. Supplied check observations all pass; response complete, no cancellation, charges fully reconciled. Outcome accepted.

S20c request contract: read-only `Return JSON {"sum":3} for 1+2.` Required business result must be successful JSON object with `sum` equal to integer 3, no error member. Exact HTTP 200 body:

```json
{"error":{"code":"upstream_failed","message":"No result"}}
```

Rubric check observes an error member and missing sum; this is a completed, demonstrably invalid business result. Outcome failed. It is not a successful tool request, expected refusal or empty-text case. No replay is authorized merely by this failure.

S21a-S22b use this **frozen synthetic protocol**, only to test decision semantics, not to prescribe actual pilot thresholds: arms A strong-direct, B economical-direct, C fixed-rule, D router; ten separately indexed holdout copies H01-H10 of the exact S01 edit input and byte-diff rubric per arm, two repeats each (20 assigned trials/arm), no tuning overlap, four isolated environments, qualified/authorized profiles, identical objective rubrics and cold-cache conditions, all attempts/checks inventoried. These repeated mechanical fixtures test the decision rule only; they do not establish diverse workload coverage or statistical confidence for a real pilot. Minimum 20 observations/arm and all ten task fixtures covered; mandatory acceptance floor 90%, maximum acceptance loss versus A 5 percentage points; minimum cost-per-success reduction versus A 10%; maximum p95 latency and operator effort increase versus A 10%; C-vs-D cost/latency/effort equivalence margin 5%, acceptance margin 5 percentage points. D must demonstrate an additional cost reduction over qualifying C **strictly greater than 5%** to promote. Frozen uncertainty rule uses supplied 95% comparison intervals; required limits must be met by the entire interval. Intervals crossing a limit imply inconclusive. No severe unauthorized/privacy/data-loss/unsafe-replay failures allowed; any observed instance rejects regardless of other evidence. No missing billable usage allowed for economic adoption recommendations.

For these synthetic cases only, the table entries and intervals are complete declared observations: use them directly rather than infer a sampling model or claim they were measured. Actual pilots must freeze a justified statistical method and collect raw observations before these gates apply. If not explicitly overridden, no protocol drift, missing checks, safety failures or evidence gaps exist, and observations are final. Each report inventories all assigned trials; cancelled/failed attempts are included in total spend.

| Pilot leaf | Supplied observations (all cash in dollars) | Uncertainty/evidence inputs | Required outputs |
| --- | --- | --- | --- |
| S21a | A/B/C accepted 20/20 each; spend A=$2.00 B=$1.20 C=$1.00. D accepted 0/20; spend D=$1.00, all charges settled; every D trial's required exact-diff check fails | D mandatory 90% floor violated by observed 0%; no numeric cost/success for D, precision/accounting otherwise complete | report complete; decision reject (quality floor); D ratio undefined; router_promotion_eligible=false |
| S21b | A/B/C/D each accepted 20/20. Spend A=$2.00 B=$1.20 C=$1.00, all complete; D known spend=$0.90 but exactly one verifier charge `v-20` has amount/usage unknown and remains reserved conservatively at $0.03; no reliable final economic interval for D | Quality loss interval D-A=[0,0] pp; no safety violation. Every trial/attempt listed, gap `v-20` assigned host reconciliation owner, no final charges invented; no evidence-based promotion/simplify comparison possible | report complete; decision inconclusive; D cost/success incomplete/unknown, no savings; router_promotion_eligible=false; $0.03 reservation/recovery obligation retained |
| S22a | All arms accepted 20/20 on output checks; spend A=$2.00 B=$1.20 C=$1.00 D=$0.80, complete; p95/effort equal. Post-run review discovers one D trace `D-4/send-1` transmitted fixture-local-only bytes to unauthorized cloud destination; all recorded runs predate discovery, no further call may occur | Safety ledger has one observed unauthorized effect, even though task output checks passed; accounting/coverage complete | stop unsafe trial; report complete; decision reject; router_promotion_eligible=false; investigate before another trial; do not count D-4 as finally accepted under full safety rubric |
| S22b | A/B/C/D each accepted 20/20; spend A=$2.00 B=$1.20 C=$1.00 D=$1.00; cost/success A=$0.10 B=$0.06 C=D=$0.05; p95 latency 100ms all arms, operator effort 1 minute/trial all arms; no safety/evidence gaps | Quality loss C-A and D-A=[0,0] pp. Cost reduction C-A and D-A=[50%,50%], incremental D-C reduction=[0%,0%]. Latency/effort increase versus A and D-C=[0%,0%], C-D acceptance difference=[0,0] pp; all supplied 95% intervals meet simpler-policy gates/equivalence but D fails >5% incremental benefit | report complete; decision simplify; router_promotion_eligible=false; C adoption may only be proposed for separate authorization, never automatically installed |

### Additional audit acceptance fixtures

R01-R02 common repair ledger: original task `T-repair` has authorized tuple C as above, one initial dispatch already consumed, observed fixable exact-diff failure, no project stop/effect uncertainty. User expressly authorizes one bounded same-profile correction and, if needed, one new-profile escalation to S after rechecking all gates. All required checks/bounds available; global maximum four physical calls including any planner/verifier, deadline 300 seconds, settled $0.02 within $1.00 cap. No extra routing/verifier calls are made in these traces; required checks are local and free in the fixture. S is independently qualified for the task; similar price or label conveys no qualification.

| ID | Exact supplied trace/conditions | Required result | Prohibited result |
| --- | --- | --- | --- |
| R01 | Corrective dispatch #2 uses identical C tuple and all gates pass | One same-profile repair consumed; total physical calls=2, remaining=2; second same-profile correction for this original task blocked even with remaining global calls | Reset repair allowance after renaming subtask/restart or counting only successful calls |
| R02 | After R01, dispatch #3 uses `(cloud-S, provider-S, model-S@1, cfg-tools-vision@1)`, price equals C but capabilities differ; explicit escalation approval exists and gates pass | New-profile escalation, not same-profile repair; total calls=3, remaining=1; same-profile repair allowance remains consumed; missing escalation approval would block dispatch #3 | Same price/tier construed as sameness, new profile restoring one-repair allowance |

V01-V04: subject task authorized, six-call budget and checks as common defaults, required verification is `assert output == "receive\n"` plus a local runner result; no repair authorized in these traces.

| ID | Exact evidence/state at terminal report | Deterministic outcome and axes | Prohibited result |
| --- | --- | --- | --- |
| V01 | Output is exact `receive` plus LF; worker finished, exact check passes, mandatory runner unavailable after execution; no cancellation, no effects, charges settled | unverified; execution completed / verification unverified / recovery none / accounting complete | failed without observed violation, or accepted without runner evidence; if runner absence was known before start, the new-task gate instead blocks before dispatch |
| V02 | Output is `recieve` plus LF; local assertion observes mismatch and runner exit 1 for this artifact; completed, no effects/cancellation, charges settled | failed; execution completed / verification failed / recovery none / accounting complete | unverified despite demonstrated rubric violation |
| V03 | Worker output exact; verifier dispatched and times out, no verdict/error payload establishing violation, task ends without Stop, verifier charge uncertain | unverified; execution completed / verification unverified / recovery pending for verifier acceptance / accounting pending | timeout-as-semantic-failure or acceptance; no automatic verifier replay until state/eligibility reconciled |
| V04 | Stop interrupts started worker, no final output, no demonstrated violation; request acceptance/effects and charge unknown | cancelled; execution cancelled / verification unverified / recovery pending / accounting pending | accepted, charge released, rollback assumed; if an unauthorized effect is later observed, task outcome must reclassify failed while execution remains cancelled |

P01-P02 independent-acceptance fixtures are supplied review records, not actual approvals of this PR. Their synthetic immutable revision IDs are r1=`1111111111111111111111111111111111111111` and r2=`2222222222222222222222222222222222222222`; they refer only to these fixture records, not real Git objects. Actual reviews must cite the real full commit hash.

| ID | Exact evidence/conditions | Required Phase 1 disposition | Prohibited disposition |
| --- | --- | --- | --- |
| P01 | Author supplies complete self-check at synthetic full revision r1 below; owner designates no independent reviewer and no independent verdict exists | Phase 1 pending, cannot close; PR may remain draft for review | Author self-review counted as independent Approve |
| P02 | Owner-designated non-author reviewer declared independence and approved all required records at `r1`, owner acknowledged `r1`; substantive outcome-classifier amendment creates `r2` with no reaffirmation | Acceptance stale at r2, Phase 1 pending; only reviewer delta review, affected fixture rechecks and new Approve plus owner acknowledgement at full r2 may close gate | Carry r1 approval forward or infer permission to implement/merge from eventual r2 plan acceptance |

Every later scenario review must record: scenario ID; exact fixture/deviations; **full reviewed Git revision**; reviewer/date; ordered gate reasoning and observed result; pinned evidence reference; command/cwd/environment if a test was actually run; prohibited behavior observed; disposition `pass / fail / unreviewed`; correction and recheck evidence; evidence level `manual semantic review / packaging / executed host test / authorized model trial`. A blank or unreviewed record never counts as pass. Immutable revision references belong in review output/PR discussion rather than a self-referential hash in the same commit.

Plan validation now: four-file documentation allowlist, resolved local links/anchors, UTF-8/LF, secret-pattern scan, no SKILL.md/product code/installer, all seven criteria, A1-A5 corrections, all leaf fixtures in the S01-S24 families and R/V/P cases present, scoped license, exact remote content and PR diff. Manual specification review checks coherent boundary wording, not runtime compliance.

Future Phase 2 additionally requires skill metadata/name/reference checks and recorded semantic reviews at its full revision; future hosts require real no-send/effect/payment callsite, replay, cancellation, restart and shared-accounting tests. Packaging or phrase matching is not safety proof. Required failed checks stop the affected release; disclosure is no waiver. Live capability/client/economic claims need their actual authorized environment and evidence.

No product-code build/typecheck suite exists in the reviewed README-only base. Documentation checks are applicable here; no runtime test, named-client qualification, paid pilot or independent approval is claimed. Independent plan acceptance under section 15 remains pending, and Phase 1 cannot close on author self-review alone.

## 11. Evaluation and promotion protocol

Prepare a separately approved protocol with four arms: strong qualified directly, economical qualified directly, simple fixed rule, SmartRouter including all overhead. Same acceptance/privacy/effects; do not expose weak baselines to production secrets or consequential writes. Keep kit workflow constant.

Before trials freeze task/rubric/host/model/policy/catalog/price revisions, task categories, tuning/holdout, cache conditions, ordering/randomization, repetitions, hidden checks and qualitative grading. **Fill approved numerical values** for quality/acceptance loss versus strong direct, mandatory floors, minimum cost benefit, latency/review/effort bounds, D-vs-fixed equivalence margins, sample/coverage, uncertainty/confidence and threshold crossing. Blanks mean not ready. No copied universal .80/.85 confidence gate or marketing coefficient.

Freeze severe-failure stop/zero-tolerance rule, accounting completeness, blocked/cancelled allocation, drift handling, maximum attempts/cost/deadline and explicit data/spend authorization. All charges count. Zero successes => undefined; absent a separately evidenced safety/mandatory-floor violation, zero success in a required economic comparison is inconclusive, never savings. Missing usage cannot establish savings. The S21a rejection is due to its explicit observed quality-floor violation, not the undefined ratio itself.

Freeze explicit predicates for each decision before trials, then apply in order: **reject/stop** on a severe safety failure or an evidenced mandatory quality/latency/effort floor violation; **inconclusive** on remaining accounting/precision/coverage/comparability gaps; **simplify** when a safe eligible direct/fixed arm meets the preregistered quality and economic requirements and the router has no meaningful incremental benefit under frozen equivalence margins; **promote narrowly** only when all hard gates, holdout noninferiority/floors, minimum supported cost benefit and latency/effort limits pass, with meaningful advantage over safe simpler alternatives. With complete precise evidence but neither simplify nor promote predicates true, **reject** for insufficient benefit; uncertainty crossing a threshold is inconclusive, not reject. Safety rejection has priority even when accounting is missing. S21a-S22b supply deterministic examples with explicitly frozen synthetic numbers, not universal pilot defaults.

**Report completion is a separate decision from promotion eligibility.** A report is complete when every assigned task/attempt is inventoried, known observations and missing charges/checks are honestly listed, protocol deviations and recovery obligations have owners, and the frozen rule yields a disposition. It can close as `rejected` or `inconclusive` with unresolved accounting; report closure does not release reservations, erase recovery duties or permit savings claims. Complete accounting, supported comparisons and all required checks are mandatory for simplify-as-adoption or promote-as-adoption recommendations. Only a promote recommendation is eligible to propose router adoption; simplify may propose the separately qualified simpler policy instead. Reject/inconclusive block both adoption recommendations from that trial. Every adoption still requires separate authorization.

Phase 4 therefore has two outputs: `report_status = complete / incomplete` and `decision = reject / inconclusive / simplify / promote` with `router_promotion_eligible = true / false`. Missing billable usage can yield `(complete, inconclusive, false)` once documented; it never yields promotion. Stop safety-invalid trials immediately, document them for report closure, and investigate before any new trial. An incomplete report cannot close Phase 4. A complete negative/inconclusive report closes evidence collection only; downstream adoption remains gated.

Acceptance: preregistration ready and approved before authorized calls; all attempted work and evidence gaps recorded; report-completion rule and frozen disposition applied separately. S21b demonstrates complete/inconclusive/no-promotion despite unresolved verifier fees. No measured result exists in this plan-only delivery.

## 12. Research-Kit adoption — separate later decision

No Research-Kit changes here. Governed by research-first roles/evidence/handoff, ADR-0117 feature freeze, ADR-0145 measurement-before-growth and ADR-0146 rejection of kit-owned routing. Existing lead-orchestrator defaults strongest for consequential roles and escalates model first; auto-build stops for money/red suites/secrets/permissions/mandate/merge even with standing mandate.

A future nested decision project must fetch/retain evidence under its own contract/ledger, pass its own applicable gates and produce reviewed handoff. External companion-only evaluation first; no contamination of the independent strong-prompt comparison. Builders do not collect. Routing cannot pass evidence gates or authorize build/spending.

Any adoption ADR designates one model authority, names exact restrictions superseded and reconciles orchestrator/stop rules; history remains unchanged. Existing deployment must preserve user skills and pinned versions; no second dispatch engine, kit routing command or speculative config.

Acceptance: approved narrowly scoped governance decision, evidence and external benefit; existing collector/builder/handoff/stops/role tables/discovery/drift checks unchanged except explicitly reviewed scope. This plan supplies no adoption permission.

## 13. Moonzila integration — staged later

No Moonzila changes here. Respect its approved roadmap/research/memory/mission priorities; ordinary chat need not become research. First advisory UI: requested profile, gate reasons, cost basis/unknowns, privacy destination, actual dispatch availability and pinned policy/workspace/conversation revisions. Display stored previews without inference; generate only with explicit permission/accounting; stale authority invalidates recommendations.

Next separately approved serial execution through existing adapters: privacy before prompt bytes, reviewed edits/commands, real local qualification/headroom, manual eligible overrides, Stop and durable attempt/reservation/settlement/recovery. No fabricated receipts/downloads. Reconcile incomplete calls after restart; switching only at tested safe boundaries. Local-only includes all auxiliary inference.

Only after serial safety and measured need consider shared reservations, dependencies, bounded concurrency/conflicts/group cancellation. Reuse existing context/result retrieval. A hosted engine is not the inevitable endpoint.

Acceptance: actual host no-send/privacy/approval tests, serial cancellation/restart/replay/accounting tests, real client environment, separately approved scope and measured benefit. Written planning requirements do not satisfy these runtime gates.

## 14. Phases and blocking exit gates

| Phase | Deliverable | Exit gate |
| --- | --- | --- |
| 0: discovery | Instructions, scope, owner license choice, pinned survey/gaps | No guessed blocking facts; no copying without permission |
| 1: specification (this PR; plan-only) | Self-contained ordered gates, cost/verification/retry requirements, seven-finding criteria, concrete fixtures and future migration | Four documentation files only; coherent boundaries and resolved links; independent acceptance at full revision plus owner acknowledgement under section 15; no unresolved blocking finding; no usable skills; draft/unmerged; author self-review insufficient |
| 2: future skill preview (separate authorization) | Proposed three skills, references/records, completed single-authority migration | Valid packaging plus semantic review at full revision; every scenario has evidence/disposition; no competing old policy; runtime claims still untested |
| 3: evaluation preparation | Filled approved numerical preregistration/host qualification/accounting | No blanks/unknown blocking facts; separate spend/egress approval still required |
| 4: authorized exploratory/holdout pilot | Inventoried report/ledger, explicit report status and frozen decision | Complete report may close reject/inconclusive with disclosed gaps; complete accounting/checks and qualifying decision required for adoption recommendations; no severe failure waiver, recovery/reservations persist independently |
| 5: optional kit companion | Separate nested decision/adoption ADR and pinned deployment | Governance and single-authority reconciliation; existing stops/gates preserved |
| 6: optional app advisory | Authorized generation and inference-free stored display | Separate paths; stale preview invalidation; no egress without permission |
| 7: optional app serial host | Adapters/accounting/Stop/persistence/recovery | Real-callsite privacy/capability/cap/replay/cancel/restart checks; qualified live evidence |
| 8: optional expansion/maintenance | Only justified concurrency/caches/learning/adapters | Measured need, compatibility/license review, repeated adverse tests and reviewed version updates |

Future phases are options, not commitments to implement all systems. Simplify/stop if direct is cheaper, fixed rules equally effective, accounting/dispatch absent, review repeats work or adoption weakens project stops.

## 15. Release gates and delivery

**Hard blockers:** unresolved safety/privacy/permission defects; competing authority; failed or missing required checks; missing redistribution permission; exposed secrets; unsupported runtime/enforcement/savings claims. Correct and recheck before releasing the affected artifact. Merely documenting them cannot yield approval. Unimplemented future milestones are explicitly outside this plan-only artifact; their required gates remain outstanding and cannot be represented as passed.

### Independent Phase 1 acceptance

The repository owner must designate an independent reviewer and acknowledge their acceptance before Phase 1 closes. The reviewer may be a person or a separately tasked agent that did not author/amend this plan; the current author auditing its own work is not independent. No paid or external review call is authorized by this requirement alone. Designation may remain pending while the PR stays draft.

Required evidence in PR discussion or a review artifact: reviewer identity/role and independence declaration; **full reviewed Git revision**; read-only scope; F1-F7 plus A1-A5 disposition; specification walkthrough of every section 10 leaf fixture with inputs, expected/prohibited outcome and pinned evidence; named documentation checks with results; limitations; explicit `Approve / Request Changes / Reject`. Author packaging checks may be reused if their exact revision/result is cited, but cannot substitute for the independent semantic verdict.

Phase 1 closes only after independent `Approve` with no unresolved blocker or missing required review record, and explicit owner acknowledgement at that revision. Any substantive amendment invalidates the affected acceptance: the reviewer must inspect the delta, recheck affected fixtures/findings and reaffirm at the new full revision. P01-P02 make author-only rejection and approved-revision drift deterministic. Approval closes a specification gate only; this PR remains draft/unmerged unless separately instructed, and implementation/spend/consumer adoption still require separate authorization.

### Five follow-up audit findings: acceptance map

| Audit ID | Correction | Required acceptance evidence |
| --- | --- | --- |
| A1: incomplete fixtures | Literal code/payloads, explicit reservation arithmetic and separate pilot cases; no invented inputs | S16, S19, S20a-S20c, S21a-S21b, S22a-S22b plus common defaults; every leaf has deterministic expected/prohibited outcomes |
| A2: report versus promotion | Report closure independent from complete-economic/adoption gate | S21b yields complete report/inconclusive/no promotion; obligations remain pending; Phase 4 wording matches section 11 |
| A3: undefined repair tier | Immutable same-profile tuple; one correction per original task, all dispatches consume global authorized bound | R01-R02 distinguish same-profile correction from differently qualified/profile escalation; changed price/labels never reset allowance |
| A4: ambiguous outcomes | Section 7 priority classifier and independent execution/verification/recovery/accounting axes | V01-V04 plus S20a-S20c show missing runner, failed assertion, timeout and cancellation without false success/rollback |
| A5: independent acceptance | Non-author reviewer designated by owner, full-revision approval and owner acknowledgement; substantive changes require reaffirmation | P01 blocks author-only closure; P02 blocks stale approval and permits only reaffirmed new-revision closure |

Current delivery amends existing draft PR #2 on `docs/corrected-smartrouter-development-plan`, preserving observed parent/concurrent changes, verifying expected head before publication and using non-force branch update. No new PR/main update/merge. Upload only owned planning documents and remove only the prior additions made in this thread; credential in memory/header only, never in files/logs/URLs. Re-read PR/head/diff and verify remote bytes, changed-file set, draft/open/unmerged status and unchanged main after publishing.

Maintenance: consumer-pinned reviewed versions; no silent live downloads; changelog for policy changes; rerun scenario reviews and relevant runtime checks; freshness/provenance for capabilities/prices; respect retention/licensing. Users can disable routing and return to **eligible** manual selection.

## 16. Open decisions and deferred work

Resolved by the latest instruction: plan-only scope, proposed future skill roles (not delivery), MIT for new planning content, deterministic outcome/repair rules, independent acceptance requirement, draft PR target and no merge. Open before Phase 1 closure: owner-designated independent reviewer, full-revision approval and owner acknowledgement. Open before pilots: tested host/model inventory, exact dataset, numeric tolerances/repeats/benefit/uncertainty, spend/egress approval and reliable accounting. Open before adoption: kit governance exception/reconciliation, companion-versus-bundled decision and Moonzila roadmap slot.

Deferred: provider/gateway SDK, paid classifier, learned task-quality model, context engine, hosted payments, adaptive caching, parallel teams, broad adapters and research-transport economics. Trigger is observed need plus new approved evidence, not upstream feature envy. No missing license/capability/price fact is silently guessed.

## 17. Sources and evidence limits

- [Pinned SmartRouter original policy](https://github.com/StepenkoAnatoli/SmartRouter/blob/f575225642155e2e5abe1a718c8f6924e9a4f66d/README.md); historical reference only on the planning branch, with no consumer instructions changed.
- [Agent Skills specification](https://agentskills.io/specification), inspected 2026-10-07; mutable format source, not runtime qualification.
- [Pinned routing survey](ROUTER_SURVEY.md): all 13 repository heads and source/test/license samples.
- [Research-Kit](https://github.com/StepenkoAnatoli/Research-Kit), reviewed governance/skills; re-read and fetch under its nested workflow before adoption.
- [Moonzila](https://github.com/StepenkoAnatoli/Moonzila), future host boundary; current policies must be revalidated before integration.

Source/static test inspection != tests run. This public survey is not a kit provenance corpus and must not be presented as one. No benchmark, measured saving, live capability, exploit or commercial license permission is inferred from README labels. Runtime/economic claims require the later authorized evidence specified above.
