# Compact brief and result workflow (canonical)

Complements the main SKILL.md; normative source is plan sections 5-8 at merge `d7c00f9`.

## When to route
Run the decision flow **before any implementation or model dispatch begins**:

1. Collect named inputs: current-task request; host policy revision; permitted actor/provider/
   destination/data; capability catalog; price list; available checks; remaining allowances and
   deadlines.
2. For every candidate profile (current model first, then alternates), apply Gate 1 → Gate 5 in
   order (see [references/gates.md](gates.md)).
3. Choose the unique surviving candidate with the best all overhead-inclusive economics.
   - Direct is preferred when it passes all gates and no eligible delegation beats it all-in.
   - Delegate only one isolated, bounded unit, and only with plausible net benefit.
   - Recommend an eligible capability escalation when direct is unsuitable.
   - **No eligible candidate → route is blocked.** Report the first failing gate and blocking reason.
4. Reassess on scope/risk change; revalidate the whole route, not just the changed field. A
   recommendation cache keyed only on content is invalid (plan S15a/S15b/S15c/S16).

## Brief (single compact document, given to any delegation target)
One brief per delegated unit. It pins:

- Objective and exact acceptance contract (what artifact, which checks which run which commands).
- Pinned source references; exact code structure and line refs; contradictions and unresolved
  requirements preserved verbatim (summaries are **not** authoritative evidence).
- Scope of permitted effects; privacy constraints; unchanged-file guarantees.
- Approved capabilities; explicit non-goals (no recursive delegation, no spend, no scope expansion,
  no governance bypass).
- Reserved allowance(s) and the finite attempt/deadline budget (all dispatches count; see below).
- Stop and escalation triggers, including verification-failure → repair rules.

## Result contract (what a delegated worker returns)
- Artifact or exact diff; files touched; which non-goals were honored.
- All checks actually executed with exit statuses and captured output references. "Passed" claims
  without an observed run are **unverified evidence** (plan S10).
- Ledger deltas: dispatches used, time used, any new uncertain charges (never release reservation on
  cancellation alone — plan S19/B02c).
- Explicit unknowns; nothing may be reported as verified that lacks observed evidence.

## Attempt, repair and ledger rules that override any local preference
- Immutable same-profile tuple `(host-profile-id, provider, model-id/revision, tool/output-config
  revision)` defines a repair as same-profile; equal prices/labels/predicted quality do not.
- At most **one** same-profile corrective dispatch per original task; the allowance is not renewed by
  restarting, renaming, changing profiles or escalating (plan R01/R02/R03).
- All physical dispatches — initial, planner, verifier, transport retry, repair, escalation, and any
  host-internal hidden retry — consume the single approved task call budget; cancelled/timeout calls
  still count (plan R03).
- Before sending, persist the task/attempt id and reserve the call slot; `send_started` with unknown
  acceptance counts as consumed until the host proves otherwise.
- Side-effecting dispatch with unknown acceptance, unresolved tools or committed stream output
  forbids automatic replay/provider switch: reconcile the original operation first (plan S11/S12).
- Stats and completion claims above attempt level belong to the separately authorized evaluation
  flow (see skill `smart-router-eval-prep`), never to per-task routing.
