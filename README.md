# SmartRouter

## Canonical routing skills — Phase 2 preview (separate authorization required)

This branch adds a proposed, author-amended **skill preview** for the plan's Phase 2 milestone:

- [skills/smart-router/SKILL.md](skills/smart-router/SKILL.md) — the single **canonical** routing
  authority: ordered eligibility gates, recommendation/direct/delegate/escalate/blocked output
  contract, and pinned references [references/gates.md](skills/smart-router/references/gates.md),
  [references/brief-and-result.md](skills/smart-router/references/brief-and-result.md).
- [skills/smart-router-review/SKILL.md](skills/smart-router-review/SKILL.md) — evidence-backed
  blocker review; defers to the canonical policy and never re-selects or grants score-based
  permission.
- [skills/smart-router-eval-prep/SKILL.md](skills/smart-router-eval-prep/SKILL.md) — evaluation
  preregistration preparation; never authorizes or runs a paid trial.
- [tools/validate_skills.py](tools/validate_skills.py) — packaging validator (frontmatter, name
  matching, reference resolution, no-competing-authority sweep). Run: `python tools/validate_skills.py`.

**Status: proposed, not yet approved.** These skills are not yet installed in any consumer. Nothing
here authorizes adoption, spend, dispatch, or_merge. Per plan section 14/15, Phase 2 exits only
after: valid packaging plus semantic review at the full revision, per-scenario dispositions
recorded, no competing operational authority, and no untested runtime claims. A separately
designated non-author review plus owner acknowledgement is still required before Phase 2 sign-off —
see [docs/PHASE2_REVIEW_RECORD.md](docs/PHASE2_REVIEW_RECORD.md) for the author-side validation
record and the outstanding review requirements.

## Historical planning documents (superseded README content preserved)

The Phase-1 plan-only documents remain on this branch as historical/specification references:

- [docs/DEVELOPMENT_PLAN.md](docs/DEVELOPMENT_PLAN.md): original and follow-up correction maps,
  final coverage-gap register, fail-closed qualification, deterministic task/attempt states, complete
  positive/negative/boundary fixtures, independent plan acceptance, pilot prerequisites and separate
  report/adoption gates.
- [docs/ROUTER_SURVEY.md](docs/ROUTER_SURVEY.md): pinned 13-repository survey; no upstream code or
  assets copied.
- [docs/ACCEPTANCE_PACKET_b7e4827.md](docs/ACCEPTANCE_PACKET_b7e4827.md) and
  [docs/REVIEW_BRIEF_4654158.md](docs/REVIEW_BRIEF_4654158.md): reviewer handoffs pinned to
  historical revisions; not current-head acceptance records.

The previous README's tier flowchart, response-header mandates and score-average approvals are
available in the [historical policy](https://github.com/StepenkoAnatoli/SmartRouter/blob/f575225642155e2e5abe1a718c8f6924e9a4f66d/README.md)
only. They are **not** operational instructions on this branch and must be deactivated in any
consumer before Phase 2 exits (plan finding F4/S14).

## Scope and license

Specification fixes are not a claim that all future work is verified. Outstanding owners, evidence
and blocking milestones are named in the plan. Authorization is still required for skill adoption,
paid calls, consumer reconfiguration and merge. Research-Kit and Moonzila sources remain unchanged.
Proposed requirements and synthetic fixture results are not evidence of runtime enforcement,
qualified real models or economic benefit.

[LICENSE](LICENSE) applies to the newly authored planning documents and — for this branch — the new
skill files listed above. It does not license historical SmartRouter content or linked third-party
repositories.
