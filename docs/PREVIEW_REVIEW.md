# Preview acceptance review

Reviewer: Buffy (author self-review, **not independent review**). Date: 2026-10-08.
Reviewed candidate Git revision: `e30f91da333165340d6269bffa9871ac16baffdc` (core preview snapshot, pinned before PR branch publication).
Scope: plan, three instruction skills, references/templates, README migration, survey and MIT grant. Verdict: **preview coherent for draft review; no unresolved blocker identified within this declared documentation/skill scope**. Not a merge/release approval or runtime safety certification.

The final review-record-only commit pins the candidate; all other candidate files must match byte-for-byte. The candidate intentionally excludes this record, so its one forward link is completed only in the final reviewed package. Evidence below is **performed manual source semantic walkthrough**, not responses from live models, executed dispatch tests or formal proof. No numeric self-score was used. Independent reviewer approval remains pending while the PR stays draft.

## Manual scenario records

Inputs are exactly S01-S24 in [scenarios](../skills/smart-router/references/scenarios.md), with no overrides. Each row is the observed conclusion of reading the written procedure/contract against those inputs; `pass` means the policy specifies the expected boundary, not that a host/model enforces it. Reviewer/date/revision above apply to every row. Evidence: [canonical procedure](../skills/smart-router/SKILL.md), [ordered gates/accounting/recovery contract](../skills/smart-router/references/routing-contract.md), [review procedure](../skills/smart-router-review/SKILL.md), [pilot protocol](../skills/smart-router-eval-prep/references/protocol.md) and [README authority](../README.md).

| ID | Source walkthrough conclusion / evidence section | Disposition |
| --- | --- | --- |
| S01 | All five gates satisfied for fixture; procedure 4 prefers eligible direct; procedure 6 requires exact check before acceptance | pass — manual only |
| S02 | Economics compares $0.04 direct with $0.09 total routing; procedure 5/contract count all overhead, prefer direct | pass — manual only |
| S03 | Permission/privacy rejects S before transmission; current/planner/reviewer share gates, sole model exception absent | pass — manual only |
| S04 | Capability gate removes C for both image and active tools; empty set stays empty, no decorative-tool stripping exception for required tools | pass — manual only |
| S05 | Price tier cannot supply tools/qualification; X/L/S all ineligible; escalation blocks rather than price-ladder promotion | pass — manual only |
| S06 | Strict-cap inadequate price/bound/accounting prohibits automatic billable dispatch including current model and routing generation | pass — manual only |
| S07 | Explicit uncertainty acceptance cannot retain a false strict-cap guarantee; revised authorization/reliable bounds needed | pass — manual only |
| S08 | $0.06 + mandatory $0.05 exceeds $0.10; verification/affordability gates block before start, no check waiver | pass — manual only |
| S09 | Project red-suite stop overrides repair budget and one-repair ceiling; pause/diagnosis required | pass — manual only |
| S10 | Claimed tests without observations cannot satisfy procedure 6; unavailable required checks produce unverified | pass — manual only |
| S11 | Unknown migration acceptance enters reconciliation; no automatic replay despite remaining budget | pass — manual only |
| S12 | Committed semantic stream or ambiguous media acceptance is terminal for automatic retry/switch | pass — manual only |
| S13 | Stored display and inference generation explicitly distinct; generation separately authorized/accounted | pass — manual only |
| S14 | README active old tiers/headers/averages removed; support skills defer; remaining host authority conflict stops until reconciled | pass — manual only |
| S15 | Exact relevant authorization/privacy/policy/price/verifier revisions invalidate cached decisions | pass — manual only |
| S16 | Contract preserves exact code indentation/fences and relevant content; normalization cannot conflate meaning | pass — manual only |
| S17 | Unknown actor/path cannot default allow; authorization before fetch/cache/embedding | pass — manual only |
| S18 | Fresh eligibility required for each retry; permission loss blocks even known-safe replay | pass — manual only |
| S19 | Uncertain charge remains reserved; atomic allocation required in later host, never asserted implemented here | pass — specified boundary; host test untested |
| S20 | Exact tool/refusal/media rubric, intermediate tool status and final task checks; HTTP 200 alone insufficient | pass — manual only |
| S21 | Accounting defines zero-success ratio undefined and missing fees incomplete; protocol bars savings promotion | pass — manual only |
| S22 | Severe effect rejects; safe fixed-rule equivalence favors simplify after complete evidence; no average waiver | pass — manual only |
| S23 | Consumer boundaries preserve builder/evidence/handoff rules and separate adoption; model allowance is no gate override | pass — manual only |
| S24 | Unknown actual identity reported; no dispatch means recommendation only; direct needs qualification, not availability | pass — manual only |

## Seven-finding review

F1 hard blockers, F2 unknown-cost/no-dispatch, F3 complete ordered eligibility, F4 active README migration, F5 display/generation distinction, F6 preregistered promotion rule and F7 concrete pinned scenarios are explicitly specified in [plan section 3](DEVELOPMENT_PLAN.md#3-seven-review-findings-corrections-and-blocking-acceptance). Manual source walkthrough identifies no contradictory selection policy. Future runtime/pilot criteria remain untested, not waived.

## Verification record

- **Verified:** dependency-free inline Python staging check in the Research-Kit workspace, scoped only to `.freebuff/smartrouter-pr2-preview`: three frontmatter names/required field lengths/metadata string version, compact bodies, exact file allowlist, relative links, UTF-8/LF, no executable source, credential-pattern scan. Full check repeated after adding this record, prior to candidate publication.
- **Verified:** 44 pinned survey GitHub links; raw-source HEAD requests returned 200, while pinned tree revisions had been inspected through complete recursive Git trees. This proves availability at checking, not factual correctness/performance.
- **Verified:** manual scenario walkthrough above; source/test/license survey of all 13 repositories. Upstream tests were inspected, **not run**.
- **Untested:** Agent Skills reference-library validator (not installed), discovery/activation in named clients, provider dispatch, permissions/accounting enforcement, real callsite no-send tests, cancellation/restart recovery, live capabilities, paid four-arm pilot and savings.
- **Expected:** a host following these instructions chooses the specified boundaries; instructions are not enforcement. No guarantee of model compliance.
- No product-code build/typecheck suite exists in the reviewed SmartRouter base; running Research-Kit's suite would not validate this remote preview and was not represented as such.

Remote branch/head, byte equality, exact changed-file set and draft/open/unmerged/main status are verified after publication and reported in the PR body/thread; this record does not claim a future remote check already happened.

## What went wrong and was fixed

- Mistake: staging validator assumed two pending review links; only one was present in the parsed Markdown links.
- Where: inline link-check assertion, cwd Research-Kit, `.freebuff/smartrouter-pr2-preview` only.
- Impact: failed local validation before any remote write; no published artifact or consumer changed.
- Cause: mismatched expected pending-link count, plus review record not yet added.
- Fix: corrected interim assertion, added this record, require zero missing links in final validation.
- Verified: interim corrected check passed; full zero-gap validation run before publication.

Public API rate limit interrupted an optional reread; authorized credential used in memory/header for continuation, never reproduced in content/commands/URLs. No permission to copy upstream source, execute it or run paid trials was inferred.

## Remaining limits

Author self-review is not independent semantic certification. Skill formats and written policy can be coherent while real hosts/models still fail. Required executed acceptance and preregistered measurements must precede any runtime/enforcement/savings release claims. Research-Kit/Moonzila adoption, trial budgets and numeric tolerances remain separately approved work. PR #2 remains draft/unmerged.
