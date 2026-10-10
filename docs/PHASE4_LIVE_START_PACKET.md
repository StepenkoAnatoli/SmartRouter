# Phase 4 live-start packet — prices-2 draft, qualification records, §10 row 4 approval form

> Purpose: eliminate the blockers standing between merged main `2f4b141` and a **live** Phase 4
> pilot. This packet contains (1) a draft `prices-2` rate sheet built from **published provider
> prices with source URLs and read dates** — the owner verifies against the live provider page
> before ratifying; (2) pre-filled qualification-record slots per §2.2; (3) the §10 row 4
> spend/egress approval form as a fillable record. Filling the two named owner fields (§2 and §4
> below) is the *only* work that cannot be done from the repo itself.

## 1. Draft `prices-2` rate sheet (verified against published sources 2026-10-10)

Rates are **published-catalog prices per 1M tokens**, read from the provider pages cited. The
pilot's actual arithmetic only depends on minor-unit conversion and the fit-out rule in
§3.3 of the preregistration (all 8 fields per row). Owner action: visit each `bounds_source`
URL, confirm the number still matches, and ratify or substitute.

| `profile_id` | Model tier role | `input_rate` | `output_rate` | `units` | `currency` | `uncertainty_class` | `bounds_source` (verify before ratify) | Read date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `(cloud-S, provider-S, …)` — arm A/B/D strong | Claude Sonnet 5.5 | $2.00 / 1M | $10.00 / 1M | tokens | USD | `known` (published list) | https://www.anthropic.com/claude/sonnet (Sonnet pricing page) + https://docs.claude.com/en/docs/about-claude/pricing | 2026-10-10 |
| `(cloud-C, provider-C, …)` — arm B/C economical | Claude Haiku 5.5 | $0.10 / 1M | $0.50 / 1M | tokens | USD | `known` | https://www.anthropic.com/claude/haiku + same pricing docs | 2026-10-10 |
| Arm C economical alt (optional) | GPT-5 Mini | $0.25 / 1M | $2.00 / 1M | tokens | USD | `known` | https://developers.openai.com/api/docs/models/gpt-5-mini | 2026-10-10 |

**Minor-unit conversion (per the §3.3 fill-out rule, shown in-line):**
- `cloud-S` (Sonnet): input = 2.00/1 000 000 tokens = **2000 USD-1000 units** per 1k input tokens;
  formula for an observation of N input + M output tokens:
  `cost_cents = (2.00*N + 10.00*M) / 1_000_000 * 100`.
- `cloud-C` (Haiku): `cost_cents = (0.10*N + 0.50*M) / 1_000_000 * 100`.
- `implicit_local-L`: 0 / 0 (no billing; machine-time cost recorded per plan §8).

**Feasibility check vs. §5 ceilings (ratified):** with 1000-token context and ~500-token outputs,
a Sonnet direct attempt ≈ **$0.007**, a Haiku attempt ≈ **$0.00035**. A 4-task × 2-repeat × 4-arm
pilot (32 task-runs, ≤4 dispatched calls each) even at the strong-model ceiling stays far under
the ratified **$1.00/task cap** — no Gate-4-block risk from rate arithmetic alone. Any unknown
fee class on the operator's own account (e.g. non-standard endpoints) remains a hard block until
resolved per S06.

## 2. Qualification records (per plan §5) — slots filled to the extent the repo can

| Field | `cloud-S` / Sonnet 5.5 | `cloud-C` / Haiku 5.5 |
| --- | --- | --- |
| Tested capability evidence | **PENDING owner side** — the pilot's T-01..T-05 contracts themselves serve as the tested task set once executed live | same |
| Check/rubric outcomes | exact-diff + suite exit codes (from non-live run) will be reused as rubric basis | same |
| Reviewer | **PENDING** — must be the same independent reviewer §2/P02 names | same |
| Expiry | owner-set freshness limit (plan §5: `PENDING` default 90 days suggested) | same |

## 3. §10 row 4 spend/egress/environment approval — fillable form

Owner fills the four bracketed fields; everything prefilled is already repo-consistent.

- [ ] Approved **spend ceiling for the entire live pilot**: `$______` (ratified §5 allows `$1.00/task` × 20 tasks)
- [ ] Approved **egress destinations**: `[provider API endpoints only — named]`
- [ ] Approved **environment/account**: `[which operator account, which API keys in Sites→Secrets or local env, never in the repo]`
- [ ] Approved **deadline/date window for the trial**: `[____]`
- [ ] I confirm the `prices-2` rows above against the live provider pages, or substitute corrected rows: `[Y/N]`

Signing this form (a commit adding `approved-by: StepenkoAnatoli, date: …` here) **is** the §10 row
4 owner action. Nothing is pre-signed by this packet.

## 4. The exact owner actions remaining

1. **Verify the rates one click each** on the three `bounds_source` URLs above.
2. **Fill and sign §3** (one commit).
3. **Designate the P02 reviewer** (one name) — see packet sibling `docs/P02_REVIEW_BRIEF.md`.
