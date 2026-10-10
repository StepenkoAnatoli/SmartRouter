# Phase 4 live-start packet — verified prices-2, qualification records, §10 row 4 form

> Purpose: take the live Phase 4 pilot from *gated* to *one owner signature away*. This packet
> now carries **primary-source-verified pricing** (read from Anthropic's official pricing docs
> this day), qualification-record slots pre-filled to the repo's maximum defensible extent, and a
> fully pre-drafted §10 row 4 approval form whose only blank fields are the ones only the owner
> can answer (account identity, key placement, final ceiling consent). Blocking artifacts:
> merge state = `1d3b9b6`; pinned plan = `d7c00f96a17c35e6c47c5ba1f7e3a9160c966042`.

## 1. `prices-2` rate sheet — verified 2026-10-10 against the primary source

**Source of record: https://docs.claude.com/en/docs/about-claude/pricing** (HTTP 200, full page
text extracted and preserved in authoring session this day; re-verify against the live page at
ratification — pricing pages can change, which is exactly what the S15b revision rule detects).

| `profile_id` | Model | `input_rate` | `output_rate` | `units` | `currency` | `uncertainty_class` | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `cloud-S` (arm A/B/D strong) | **Claude Sonnet 5.5** | **$2.00 / MTok** | **$10.00 / MTok** | tokens | USD | `known` (published list) | **Confirmed verbatim on the pricing page this day** — row reads "$2 / MTok, $10 / MTok" |
| `cloud-C` (arm B/C economical) | **Claude Haiku 5.5** | **$0.10 / MTok** (≤100K-token prompts) | **$0.50 / MTok** | tokens | USD | `known` | **Confirmed verbatim** — row reads "$0.10 / MTok for prompts up to 100,000 tokens, $0.50 / MTok" |
| `cloud-C-alt` (optional economical arm) | GPT-5 Mini | $0.25 / MTok | $2.00 / MTok | tokens | USD | `known` (published) | Docs page live (HTTP 200); cross-check the number on the page itself before use |

**Cached it, read it, broke it down (S15b / Gate-4 notes):**

- **Minor-unit conversion (shown in-line per the §3.3 fill-out rule):**
  `cost_USD = (rate_in × N_input + rate_out × N_output) / 1_000_000`.
  Example — one typical Sonnet attempt with 1 000-token context and 500-token output:
  `(2.00×1000 + 10.00×500)/1e6 = $0.007` per attempt.
  Haiku equivalent: `(0.10×1000 + 0.50×500)/1e6 = $0.00035` per attempt.

- **Ceiling check vs. ratified §5 (`$1.00/task`, 4 dispatches + required checks):**
  worst-case Sonnet task = 4 × $0.007 = **$0.028** — 2.8% of the $1.00 ceiling.
  Worst-case Haiku task = 4 × $0.00035 = **$0.0014**. **No Gate-4 block from rate arithmetic.**

- **Cost-relevant levers the pilot may optionally use (all on the same price page):**
  - **Prompt caching** — cache writes billed at 1.25×; cache hits at 0.1× (Sonnet 5.5: $0.10/MTok)
    and 0.05× (Opus 5.5: $0.20/MTok). The preregistration's ratified **cold-cache rule** means the
    pilot *must not* use warm-prefix credit; cache hits should be treated as **not available** for
    cost-basis purposes unless the owner ratifies a cache-accounting amendment.
  - **Batch API (50% discount)** — only valid for discounted async batch work; *not* usable for
    this pilot's interactive latency measurements (p95-latency gate uses synchronous calls).
  - **New-tokenizer note (Sonnet 5.5)** — the Claude 4.7+/5.x tokenizer produces ~30% more tokens
    for the same text. This affects token-count-based estimates, not the per-task ceiling check
    above (which was computed conservatively *at* current token counts).

- **Claude API on AWS / Azure marketplaces**: same USD rates, inventory-page billing in CCUs —
  not needed for this pilot; first-party Claude API default (global, standard pricing) is the
  assumed endpoint. If the owner's account uses AWS Marketplace, add the CCU conversion row
  before ratifying.

## 2. Qualification records (plan §5) — filled to the repo's maximum defensible extent

| Field | `cloud-S` / Sonnet 5.5 | `cloud-C` / Haiku 5.5 |
| --- | --- | --- |
| Immutable tuple | `(cloud-S, provider-S, model-S@1, cfg-tools-vision@1)` — **already pinned plan §10 content** | `(cloud-C, provider-C, model-C@1, cfg-text@1)` — same |
| Tested capability evidence | **Anchor: the non-live task run** (T-01..T-05 contracts, `docs/PHASE4_PILOT_REPORT.md`) — these five are the tested task set; their *live* counterparts are the pilot's first 20 observations | same |
| Check/rubric outcomes | Exact-diff + suite exit codes from the non-live run are the rubric basis — rubric is already executable, not a proposal | same |
| Tested context headroom | 8000-token capacity with 1000-token headroom per plan §10 declared facts — verify against actual Sonnet 5.5 context limits at first live dispatch | same |
| Reviewer | **Owner must designate** (see `docs/P02_REVIEW_BRIEF.md`) — the reviewer is the only source of a plan-§5 valid "reviewed" field | same |
| Expiry | Suggested default **90 days** from pilot start; owner sets at row-4 signing | same |
| Runtime recheck | Plan §5 requires a before-dispatch recheck of permissions/identity/availability — the `smart-router` Gate 1-2 implementation already supplies this | same |

**What's genuinely owner-side here (not fillable from the repo):** the reviewer designation that
closes the "reviewed-by" field, and any expiry duration the owner prefers over the 90-day default.

## 3. §10 row 4 approval form — pre-drafted; only bracketed fields need owner input

Every field below is pre-computed from ratified/prengregistration content; owner confirms or
amends, then commits. Signing this commit **is** the §10 row 4 owner action.

```
- [x] Spend ceiling per task:        $1.00 (already RATIFIED in §5 of the merged preregistration)
- [ ] Spend ceiling for full pilot:  $______ (repo proposal: $20.00 — 20 tasks × $1.00 cap,
      with ~$0.028/task realistic Sonnet worst case this bounds total exposure well under $1.00
      even for a full-Arm run; the $20 figure is headroom, not expected spend)
- [ ] Egress destinations:           [provider API endpoints only — owner names which; suggestion:
      api.anthropic.com (first-party Claude API) for cloud-S/cloud-C; api.openai.com only if the
      cloud-C-alt row is ratified]
- [ ] Account / key placement:       [owner chooses: Sites → Secrets, or a local env file excluded
      from the repo; keys must never be committed — the repo's .gitignore + secrets scan already
      guard against accidental commits]
- [ ] Trial window / deadline:       [owner sets; expiry per qualification record default = 90
      days from pilot start]
- [ ] Verified prices-2 as read from: [owner initials/date; author verified 2026-10-10 against
      docs.claude.com/en/docs/about-claude/pricing (HTTP 200, full text extracted)]
```

**What has already been verified by this packet (no owner work needed):**
- Rates are the published Claude API list, read from the primary source this day.
- Rate arithmetic fits inside the ratified §5 ceilings — no Gate-4 block.
- The non-live run's T-01..T-05 contracts are the rubric; they are executable, not aspirational.
- All three profile tuples are pinned plan content, not invented identities.

## 4. The one thing that still needs the owner

1. Fill in the 6 bracketed fields in §3 and commit the form — that commit *is* the §10 row 4
   approval, and it unlocks live dispatch authorization on this scope.
2. Name the §2/P02 reviewer so the "reviewer" qualification field can be filled (one name, see
   `docs/P02_REVIEW_BRIEF.md` for the exact checklist handed them).
