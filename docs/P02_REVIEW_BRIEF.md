# P02 review brief — independent non-author reviewer packet (Phase 3 exit)

> Purpose: make reviewer designation the *only* remaining owner action to close the Phase 3
> document gate. This brief hands a designated reviewer everything they must check, in order,
> with the exact deltas and pass criteria. **The owner cannot be the reviewer; the plan (P02)
> requires independence from the author of record.**

## 1. What the reviewer reviews

| # | Delta scope | Commits | Categories to recheck |
| --- | --- | --- | --- |
| 1 | Phase 3 preregistration concrete fill (tasks, seeds, pricing skeleton) | `6d20b04` (PR #8 base) | §3.1 task anchoring, §3.2 seed derivation reproducibility, §3.3 pricing-structure conformance to plan §10/§8 |
| 2 | Phase 3 ratification revision (host, thresholds, non-live fill) | `5d79768` + `23a9ef0` (PR #9 head) | §2.1 host controls vs. plan §7/§8, §4/§5 thresholds matching the preregistered proposal unchanged, §11 history consistency, §4.4 boundary statement |
| 3 | Phase 4 non-live evaluation + completion record | `2f4b141` (final main) | §3.1 contracts executed per evidence captured; §7 report fields coherent; limitations disclosed honestly |

## 2. Pass criteria (from plan P01/P02 and the preregistration itself)

1. **Independence**: reviewer did not author any of the deltas under review.
2. Every substantive amendment carries an explicit status label (`RATIFIED`/`PROPOSED`/`PENDING`/`BLOCKED`) matching its actual owner-authorization state.
3. Numeric values claimed `RATIFIED` trace to either an owner decision recorded in a commit/PR, or to plan-pinned content (`d7c00f96a17c35e6c47c5ba1f7e3a9160c966042`).
4. No silent weakening: the decision suite on the reviewed commit passes **79/79, exit 0** (52 fixture IDs).
5. Seeds reproduce from the documented SHA-256 method (spot-check 3 values).
6. `tools/validate_skills.py` exit 0 on the reviewed tree.
7. Merge-authority record (§3 of `PROJECT_COMPLETION.md`) accurately describes what actually happened (it does — owner-directed merges superseding the normal reviewer step; the reviewer is now providing the *independent* review the plan wanted).

## 3. Recommended reviewer candidates (owner names one)

| Candidate | Why suitable | Action needed |
| --- | --- | --- |
| A fresh Claude Code / Freebuff agent instance, run read-only in a scratch clone | Truly independent of this session's authorship; can run the full §2 checklist in one pass | Owner: open a separate session, paste `docs/P02_REVIEW_BRIEF.md`, and instruct them to file their review record as a commit `docs/P02_REVIEW_RECORD.md` when done |
| A human colleague with repo read access | Max credibility | Owner: request a code review on the 3-commit delta via GitHub (review → file findings as PR comments or a separate PR) |
| The repo owner + a *separate* agent instance | Fastest path already in-repo | Owner: one commit naming the reviewer, then let the new session issue its own review record |

## 4. Post-review closure mechanics (owner + reviewer in tandem)

Once the reviewer names/recomments as above and the record lands:

1. Reviewer files `docs/P02_REVIEW_RECORD.md`: what was checked, evidence level, disposition per category (`corrected and rechecked` / `nonblocking` / `unresolved`), full revision hash reviewed.
2. Owner adds a one-line acknowledgement commit on the same record.
3. Phase 3 document gate closes at that full revision; Phase 4 live start proceeds per
   `docs/PHASE4_LIVE_START_PACKET.md` (row-4 form already staged there).

## 5. What the reviewer does NOT need to do

- Re-merge re-review of already merged material beyond the three deltas in §1.
- Recompute Phase 4 live economics — that trial has not started.
- Independently re-validate the whole history; only the named revisions' deltas.
