# SmartRouter: corrected development plan

Status: proposed roadmap. This PR publishes a plan only.
Date: 2026-10-07.

The [existing policy](../README.md) is preserved apart from a roadmap link.
This document installs no skill, implements no dispatch, authorizes no paid trial,
supersedes no consumer decision, and demonstrates no savings. Milestones below
need implementation and verification before their outcomes can be claimed.

## 1. Product goal and compatibility

Help AI agents complete accepted work at lower total cost through suitable model
capabilities, bounded delegation, verification and permitted escalation. Optimize
cost per accepted task, not token price. Maintain explicit quality requirements;
no model guarantees correctness. Start with coding/research agents and Research-Kit
users, then Moonzila. Keep the policy provider-neutral and independent of a host.

| Level | Behavior | Limit |
| --- | --- | --- |
| Instructions | Read policy and recommend routes | Cannot switch the running model |
| Skill | Discover and activate portable instructions | Discovery is not dispatch |
| Dispatch host | Delegate through actual existing tools | Host enforces permission and accounts for usage |

A prompt cannot create tools, enforce billing or guarantee every client works.
No selection means advisory use. Unavailable model identity/usage is unknown.

## 2. Responsibilities and trust boundaries

| Component | Owns | Does not own |
| --- | --- | --- |
| SmartRouter | Recommendation, brief, escalation/reporting policy | Credentials, networks, permission enforcement |
| Research-Kit | Evidence, provenance, gates, collector/builder roles | Another dispatch engine |
| Moonzila | Profiles, inference, privacy, reviewed effects, Stop, durable state | A separately maintained policy fork |

Sequence: allowed workflow -> task contract -> recommendation -> host eligibility,
privacy and budget checks -> execution -> checks -> outcome. Host authorizes and
executes. Model recommendations are untrusted input, never approvals.

Privacy applies to routing, planning, summaries, workers, review and repair. A local
worker with a cloud reviewer is not local-only. Read-only work can disclose secrets.
Check access and egress before every model call or tool action.

## 3. First release scope

One canonical skill, focused README, compact task/result templates, a small scenario
set, packaging checks, compatibility guidance and a frozen evaluation protocol.
Reuse existing conventions/tooling. Do not build a provider gateway, hosted service,
billing engine, installer, independent orchestrator, parallel scheduler, adaptive
router, Research-Kit command, research-transport router or consumer code changes.

The first release is a policy preview, not measured savings. Confirm licensing,
authorship and notices before redistribution. If no license exists, record the gap
and obtain the owner's decision; do not silently assign one.

## 4. Instruction authority and conflicts

Follow host safety/permissions, current user authorization, applicable project
instructions and workflow gates. SmartRouter is not an override. Spend approval
does not permit disclosure, edits, commands, deployment or merging. Preserve plan-only
and read-only intent across delegation. Use one explicitly designated model-selection
authority; never rely on which competing skill was read last.

Research-Kit constraints reviewed in planning:

- skill-router chooses workflow skills, not models.
- lead-orchestrator defaults to most capable for research, review and many builders,
  and says to escalate the model first on failure.
- Governing auto-build guidance stops for paid spending and red suites. Standing
  mandates do not preapprove those stops.
- ADR-0117 freezes features; ADR-0145 measures before growth; ADR-0146 currently rejects
  model routing in kit-owned code/prose.

A budget cannot silently override these. Report "escalation recommended; approval
required" where appropriate. Failed checks pause routing and follow project diagnosis
and approval rules. A bounded-repair ceiling is not a stop-rule exception.

Adoption requires a reviewed decision identifying authority and reconciling conflicts.
Do not rewrite historical decisions or contaminate the kit's existing comparison by
silently changing workflows/model policy.

## 5. Routing decisions and capabilities

- **Direct:** current model is suitable; avoid extra orchestration. This is the default.
- **Delegate:** one genuinely bounded unit is economical and affordably verifiable.
- **Recommend escalation:** missing capability needs another eligible model.
- **Blocked:** permission, privacy, capability, allowance or mandatory checks are inadequate.

Do not pay a classifier, build a team or demand second-model review for trivial work.
Reassess at meaningful task/scope boundaries, not through headers on every reply.

| Requirement | Suitable work |
| --- | --- |
| Economical | Clear, mechanical, bounded, low-risk and directly checkable |
| Standard | Moderate reasoning with established patterns and bounded impact |
| Advanced | Architecture, ambiguity, auth, money, deletion, important data integrity, concurrency, subtle correctness, consequential interpretation |

Assess consequences, clarity, reversibility, dependencies, context/tools, data sensitivity,
external facts and check strength. Lines/files changed are not risk measures. One-line
authorization edits can need advanced reasoning. Price, brand, model size and local status
do not establish capability.

Host inventory identifies profiles, tools/structured-output support, context, locality,
qualification evidence, limitations and cost information. Operator tiers are assignments,
not measured qualifications. Unknown capability is not suitability evidence.
Escalation reselects an eligible candidate meeting missing requirements, not a price ladder.
A costlier model can lack tools/context/permission. None eligible means stop, not downgrade.

## 6. Do-not-delegate gate and hidden costs

Consider planning, briefs, duplicated context, worker output, review, repair and switching.
Strong planning + cheap execution + strong review + strong repair can exceed direct cost.
Delegate only where isolation, inputs and affordable checks are established and avoided work
plausibly exceeds overhead. Preview uses no invented probability or universal threshold;
record uncertainty and calibrate with pilot evidence.

Prefer stable assignment across related work. Switching may lose context caching, add
framing or incur local startup. Measure usage/latency; shorter prompts do not establish
proportional savings. Do not manufacture subtasks to demonstrate cheap routing.
If review essentially repeats the task, choose direct work. Required consequential review
cannot be removed to meet savings goals. Capability/price maintenance is recurring overhead.

## 7. Briefs, context and execution

One compact brief: objective, authoritative inputs, allowed scope/effects, capability,
acceptance checks, privacy, applicable allowance and escalation triggers. Preserve necessary
dependencies and revision information without a hierarchical orchestration protocol.

Send relevant context, not entire conversations. Preserve references, uncertainty,
contradictions, truncation and unresolved requirements. Summaries are not authoritative
sources. Permit requests for missing inputs. Historical reads/results may be stale.

Start serially with at most one delegated unit. Workers cannot expand permissions,
allocate funds, recursively delegate or start unauthorized side-effecting tools.
Switch at safe task boundaries, not mid-provider tool exchange unless a tested adapter
supports it. Disjoint files do not isolate databases, dependency changes, commands or tests.
Defer parallelism and another context engine; reuse host functionality where sufficient.

## 8. Acceptance and failure handling

Define acceptance before work:

| Work | Evidence |
| --- | --- |
| Mechanical edit | Exact diff/invariants and relevant existing checks |
| Code implementation | Relevant tests, applicable typecheck/build, behavior checks |
| Research interpretation | Claims checked against fetched authoritative sources |
| Architecture | Constraints, alternatives, failure modes, appropriate independent review |
| Consequential change | Capable independent review and targeted adverse cases |

Self-assertion and numeric self-scores are not gates. Distinguish assertions, host observations
and check evidence. Required blocked checks mean unverified, not accepted. A valid corpus
or passing provenance gate does not establish supported claims or correct implementation.

Classify failures: missing context -> permitted retrieval; transient transport -> safe bounded
retry when allowed; weak reasoning -> capability escalation recommendation; failed checks ->
project stop/diagnosis before approved repair; scope change -> reclassification/authorization;
permission/privacy/allowance gap -> stop; uncertain effects -> recovery, never blind replay.

Where project rules permit, at most one same-tier repair for an identified bounded issue.
Total attempts remain finite and approved. This ceiling never overrides stops. Escalation
starts from current observations/journals, not just the original request. Strongest eligible
models can still fail; report unresolved outcomes.

## 9. Budget semantics

Total cost = planning/routing + briefs/context + execution + failed attempts + review
+ repair/escalation + billable tools. Separate inference, research credits, local resources,
latency and operator effort; invent no conversion rates. Subscription hosts report quota
or usage instead of fictitious cash savings.

Cost per accepted task = total spend across all attempts / count of accepted tasks.
Also report completion/blocking and severe defects so refusal does not masquerade as savings.

Skill-only budgets are advisory, never enforced caps:

- Unknown prices/usage are not zero; disclose missing accounting.
- Authorization bounds providers, privacy, scope and attempts as well as allowance.
- Automatic escalation needs both host and project permission.
- Mandatory verification must be affordable before starting a route.
- Optional escalation need not be reserved forever; stop if it becomes unaffordable.
- Failed calls, timeouts and cancellation can still cost money.
- No unapproved cloud fallback. Local execution has resource/time cost.

Later hosts reserve conservatively, reconcile reported usage, retain uncertain charges,
prevent double allocation and block insufficient funds. Context heuristics are not exact
billing bounds. Hard monetary guarantees need reliable pricing and conservative billable
usage limits. Inadequate accounting under strict budgets means manual/advisory mode.

## 10. Packaging and reports

Use Agent Skills format: one skill directory with root SKILL.md frontmatter. Keep core
instructions compact and references on demand. README explains rather than duplicates policy.

Deliver: focused README; canonical skill; routing/cost/safety/compatibility references;
brief/result templates; direct/delegated/escalated/blocked examples; scenario fixtures;
lightweight packaging checks if needed; evaluation protocol; conventional changelog.

Separate requested route from actual host-reported model. Report rationale, observed and
unavailable checks, estimated/reported/unknown usage and residual uncertainty. Outcomes:
recommendation, accepted, unverified, blocked, failed, cancelled. Cancellation can leave
charges/effects needing reconciliation. Do not force verbose headers on ordinary replies.

## 11. Research-Kit adoption (later)

Evaluate externally before consumer changes. Research adoption as a separate nested decision
project with fetched evidence and reviewed handoff. Keep it separate from root corpus;
collect only on an authorized collector and reuse applicable evidence.

Start companion-only. Workflow gates establish permitted work before model selection.
Builders do not collect; missing facts go to collectors. Preserve warnings, source references
and known unknowns. A routing recommendation never authorizes building or passes a gate.

Adoption ADR identifies one selection authority, reconciles spending/failure stops and names
only restrictions superseded. Respect feature freeze and measure-before-growth unless the
owner approves a narrow exception. Historical decisions remain records.

If justified, pin provenance/license and use existing skill deployment. Validate discovery,
role tables, user-owned skill preservation, drift and unchanged gates with existing tests.
No second dispatch engine or speculative configuration system. This PR changes none of it.

## 12. Moonzila integration (later)

Fit the approved app roadmap; do not displace current research/memory/mission work or make
ordinary chat depend on research. Start advisory: profile, reason, checks, cost basis/unknowns,
privacy destination, real dispatch support. Treat recommendations as untrusted and bind them
to workspace/conversation/project policy revisions.

Then serial execution through existing adapters/ownership. Recheck policy before prompt
bytes. Reuse real local qualification and measured headroom, not fabricated receipts or
automatic downloads. Keep reviewed edits/commands, Stop and uncertain-operation recovery.
Only safe task-boundary transitions unless a provider-specific adapter is tested.

Persist policy/version, identities, attempts, profile, reservations, usage, reconciled and
uncertain charges, checks and recovery outcomes. Restart reconciles incomplete calls before
releasing funds/continuing. Controls: on/off, eligible manual overrides, approved providers,
local-only, budget, finite attempts and route explanation. Overrides never bypass permission.

Only after serial correctness consider shared reservations, bounded workers, dependencies,
conflict prevention and group cancellation. Reuse existing context/result retrieval.

## 13. Validation and adverse cases

Reuse tooling. With none, dependency-free packaging checks suffice: frontmatter/names,
metadata constraints, references, template/example structure and fixture consistency.
These do not prove routing semantics or live capability. Avoid lexical phrase checks
advertised as safety proofs. Manually review policy meaning as well as packaging.

| Scenario | Required boundary |
| --- | --- |
| Routed plan/worker/review costs more | Direct work |
| Single model/no dispatch | Direct/advisory; no claimed switch |
| Needed capability absent | Block; no silent downgrade |
| Cloud planner/reviewer on local-only data | Block before transmission |
| Sensitive read-only task | Access and egress checks |
| Source instructs provider change | Untrusted reference data |
| Worker claims tests without observations | Unverified |
| Budget exists but spending approval required | Ask/stop |
| Red project suite | Project stop/diagnosis |
| Unaffordable required checks | Do not start route |
| Timeout after possible command effect | Recover, never replay |
| Costlier model lacks tools/context | Reselect/block |
| Interrupted call has missing usage | Retain uncertain charges |
| Concurrent duplicate reservation | Later host prevents over-allocation |
| Builder lacks evidence/handoff | Preserve kit blocker |

Run relevant tests/typechecks/builds for implementation. Report verified/untested/expected
honestly. No paid/live trials without authorization. Native/Windows claims need their
actual acceptance environment; fixture success is not real-model quality.

## 14. Evaluation protocol

Four arms: strong eligible model directly; economical eligible directly; simple fixed
rule (economical for predefined mechanical work, strong otherwise); SmartRouter.
If fixed rules perform equally well, keep them. Do not engineer elaborate routing to
beat a deliberately weak baseline.

Freeze tasks/rubrics, eligibility, versions, allowances and quality tolerances before trials.
Explicitly approve spend/data transmission. Repeat trials; isolate workspaces; use comparable
cache conditions; separate tuning/holdout cases; blind qualitative grading where practical.
Count planning, retries/review and operator effort. No production credentials or consequential
access for unsuitable baseline models. Keep kit workflow constant when evaluating routing.

Cover mechanical/read-only work, bounded features, architecture, conflicting sources,
consequential changes, long context, unavailable capability, budgets, privacy and recovery.
Measure acceptance/blocking, cost per accepted task, defects/severity, unsupported claims,
truthful reports, retries/escalations, latency/context, review/operator effort and observed
policy violations. Prefer hidden checks and environment outcomes over model grades.
Severe failures are separate: averages cannot excuse unauthorized effects or data loss.

A small pilot is exploratory. Publish counts, failures, uncertainty and accounting basis;
no universal same-quality or percentage-saving claim. Require holdout evidence before broader
defaults. Do not alter Research-Kit's separate strong-prompt comparison mid-run.

## 15. Phases, dependencies and exit gates

| Phase | Deliverable | Exit gate |
| --- | --- | --- |
| 0: discovery | Instructions, license, factual constraints, open questions | No guessed blocking facts |
| 1: specification | Rubric, templates, precedence, budget semantics | Coherent rules and honest limits |
| 2: preview | Compact skill, references, checks, examples | Valid packaging and adverse-case review |
| 3: manual pilot | Four-arm exploratory report | Honest cost/quality outcomes; simplify if justified |
| 4: kit companion adoption | Reviewed integration decision | Governance, roles and gates preserved |
| 5: app advisory | Validated route preview | Preview itself sends no inference |
| 6: app serial execution | Dispatch, accounting, persistence, recovery | Privacy, approval, Stop and accounting checks |
| 7: optional expansion | Concurrency/task qualification | Demonstrated need and new evidence |
| 8: maintenance | Pinned compatibility, reproducible records | Claims fit tested versions/workloads |

Implement phases 0-2 in SmartRouter only first. Live trials and consumer changes are
separately approved. No packaging task implicitly permits spend, deployment or cross-repo
changes. Optional stages are possibilities, not promises to build every system.

## 16. Delivery, release acceptance and maintenance

Current delivery: publish this plan plus a README link on a dedicated SmartRouter docs
branch and open a plan-only PR. Existing policy and default branch remain unchanged.
No clone is required. No product code, Research-Kit edits or Moonzila edits. No auto-merge.

Future implementation: inspect branch/status/remotes before consequential Git operations;
preserve unrelated work; stage only owned changes; review exact diffs/commit style; verify;
push only the authorized branch/repository. Keep credentials out of content, command
arguments, remote URLs and logs. If authentication/verification fails, report the blocker.

Release gates: one coherent selection policy; direct work first-class; restrictions
preserved; advisory/executable distinction; checks pass; findings fixed or disclosed;
license gaps explicit; no unsupported savings/enforcement claims; no private data/secrets.
A red or blocked check is not success. Actual runtime/model quality remains unverified
until the corresponding acceptance exercise runs.

One source of truth, consumer-pinned revisions/versions, reviewed updates rather than
silent live policy downloads, changelog for behavior changes, rerun scenarios, provenance
and freshness for capability/pricing facts. Unknown compatibility remains unknown.
Users can disable routing and return to eligible manual selection.

Simplify/stop if direct is cheaper, fixed rules are equally effective, review repeats the
whole task, dispatch/accounting is absent or adoption weakens project stops. Mechanical-only
savings are useful but must be described narrowly. A skill must earn its maintenance cost.

## 17. Open decisions, deferred features and references

Open: license; first tested hosts/models; pilot dataset/budget and numerical tolerances;
companion-only vs bundled kit adoption; Moonzila scheduling. Resolve at the milestone that
needs them. Defer task-specific catalogues, learning, cached artifact reuse, research-tool
economics, broad adapters and hosted service until observed outcomes justify complexity.

Planning sources (not a ledger-backed research corpus or runtime qualification):

- [Reviewed SmartRouter base policy](https://github.com/StepenkoAnatoli/SmartRouter/blob/f575225642155e2e5abe1a718c8f6924e9a4f66d/README.md).
- [Agent Skills specification](https://agentskills.io/specification).
- [Research-Kit](https://github.com/StepenkoAnatoli/Research-Kit): skill-router, lead-orchestrator,
  governing auto-build guidance and ADR-0117/0145/0146. Re-read current rules before adoption.
- [Moonzila](https://github.com/StepenkoAnatoli/Moonzila): privacy policy, context assembly and
  local selection. Revalidate current source before integration.

Mutable source references are not pinned evidence. Fetch and retain primary facts through
applicable research workflow before implementation depends on them. Valid packaging, fetched
pages and passing provenance gates do not prove semantic correctness, capability or savings.
