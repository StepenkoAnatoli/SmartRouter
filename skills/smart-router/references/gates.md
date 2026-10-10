# Ordered gates — normative contract (canonical)

Pinned specification: [docs/DEVELOPMENT_PLAN.md](../../../docs/DEVELOPMENT_PLAN.md) section 5 at merge
commit `d7c00f96a17c35e6c47c5ba1f7e3a9160c966042`. These gates apply to **every** profile under
consideration: current model, planner, worker, reviewer, repairer and every fallback candidate.
All five gates run in order for each candidate; a candidate failing any gate is rejected. Recommended
eligibility = all five gates pass. Violations must stop work per the plan's conflict rule.

## Gate 1 — Permissions / privacy / workflow
Identify the authorized actor, provider, destination, data classes and effects. Default deny for
unknown identities, paths or destinations. Read-only is **not** automatically non-disclosing: a
read-only model call still transmits prompt bytes and needs permission.

**Stop conditions:** unknown identity or path; destination not covered by authorization; project stop
rules (an unrelated preexisting gate failure blocks a new task rather than proving that task's output
failed); workflow gates not yet satisfied. Check **before** any fetch, cache write, embedding call or
transmission.

**Why:** fixtures S03 (local-only data, sole cloud profile → block), S17a/S17b (unknown actor / null
path → block before fetch/embedding/cache write), S09 (red-suite project stop blocks new work).

## Gate 2 — Capabilities
Check task qualification, required tools (active, not decorative), vision/input modalities, output
contract support, and context headroom against tested limits. Labels, price tier, local execution or a
model's self-reported confidence are **not** capability proof. Required tools must not be stripped;
unknown qualification is not suitability.

**Why:** fixtures S04 (vision + active tools both required, both missing → block), S05 (expensive
advanced label does not cure missing tools → block with explicit rejects).

## Gate 3 — Verification
Define the acceptance contract **before** work starts. Every route must have available objective
checks, or capable independent review, appropriate to the task's consequence class. A known missing
verification prerequisite before execution means **blocked, no start**; after execution, missing or
indeterminate required evidence means **unverified**; observed acceptance violations mean **failed**
(classified per plan section 7's terminal-outcome priority — recorded here as route evidence, not
decided by the router).

**Why:** fixtures S15c (verifier revision requiring an unavailable runner → invalidate cache, block),
V01-V09 (outcome-axis cases), S10 (worker's "tests passed" without observed runner evidence →
unverified, never accepted).

## Gate 4 — Affordability
All mandatory work plus required verification must fit inside approved cash and resource caps, before
any reserve. Strict caps additionally require a reliable conservative billable bound and reliable host
accounting; otherwise **block automatic dispatch** (advisory uncertainty requires explicit, revised
authorization — a user's statement of uncertainty acceptance does not waive a retained cap).

Equality passes: a route is affordable when its known bound is **less than or equal to** free
allowance; call slots satisfy `used + reserved ≤ limit`; deadline requires current time **strictly
before** deadline (equality expires). Unknown or unbounded fees block a strict cap regardless of
nominal size.

**Why:** fixtures S06/S07 (unknown price/bound/accounting → block), S08 ($0.06 work + $0.05 required
review > $0.10 available → block before start), S19 (atomic reservation, uncertain charges retained),
B01/B02a/B02b (equality/expiry boundaries), S15b (stale price quote invalidates affordability).

## Gate 5 — Economics (delegation)
Only after all eligibility gates pass, compare candidates: prefer **direct** where suitable; delegate
one isolated, bounded unit of work only with a plausible **all-overhead** benefit (include planning,
brief/context, execution, review, repair/escalation and re-priming costs; compare against the full
direct bound, not the worker token cost alone). Recommend eligible capability escalation where direct
is unsuitable; if no candidate is eligible, the route is **blocked** — do not resurrect rejected
candidates and do not fall back to a cheaper tier to avoid blocking.

**Why:** fixtures S02 (direct $0.04 beats planner $0.03 + worker $0.02 + review $0.04 = $0.09 only
when all overhead is counted), D01 (eligible, economical delegation → delegate with reserved bound),
D02 (expired worker qualification + reduced allowance → block), E01 (recommend escalation to a
qualified, affordable, available profile even though it is more expensive than the failing direct
candidate).

## Qualification, freshness and pre-dispatch binding
A recommendation is only as strong as its evidence. Before any recommendation or dispatch:

1. **Profiles** must carry an immutable identity tuple `(host-profile-id, provider, model-id,
   revision, tool/output-config revision)` plus tested capability/qualification evidence.
2. **Bind** every recommendation to the task/input content, workspace, authority and authorization
   revision, capability/catalog revision, verifier contract revision and price-list revision; record
   a timestamp and freshness limits.
3. **Recheck** immediately before dispatch: current permission, identity, availability, remaining
   call allowance and deadline. Changed, expired or unknown evidence invalidates the route; cache
   keys containing only content bytes are insufficient (fixtures S15a/S15b/S15c and S16: a
   whitespace-folded cache key conflates programs with different behavior).
4. Revocation always wins over a stale cache (fixture B02c); quote/deadline equality is expiry
   (fixtures B02a/B02b).
5. No host support for required identity or fresh evidence means **advisory-only** output with an
   explicit execution blocker (fixture S24) — never a claimed successful switch.
