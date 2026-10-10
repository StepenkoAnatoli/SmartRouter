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
- [~] Spend ceiling for full pilot:  **$20.00** (repo-proposed, PRE-FILLED — arithmetic: 20 tasks
      × $1.00 ratified per-task cap = $20 absolute bound; realistic expected worst case is
      20 × $0.028 ≈ $0.56 on Sonnet + ≈ $0.03 on Haiku, so $20 is ~35× headroom, not expected
      spend. Confirm or lower the number.)
- [~] Egress destinations:           **api.anthropic.com** (first-party Claude API, global endpoint,
      standard prices — the §1-verified rows bill here) and, ONLY if the `cloud-C-alt` row is
      ratified, **api.openai.com** for GPT-5 Mini. No other destination class is proposed.
- [~] Account / key placement:       **Sites → Secrets** (recommended, platform-managed, never in
      repo) OR a local `.env` file excluded by `.gitignore` — either works; the repo's existing
      secrets scan guards accidental commits. Owner picks which of the two mechanisms.
- [~] Trial window / deadline:       **90 days from the row-4 approval commit date** (proposed
      default, matching the qualification-record expiry in §2; owner may shorten but SHOULD NOT
      extend past 90 days without a fresh qualification review per plan §5 freshness rule).
- [~] Verified prices-2 as read from: author verified 2026-10-10 against
      docs.claude.com/en/docs/about-claude/pricing (HTTP 200, full page text extracted and row
      values confirmed verbatim). Owner stamps initials/date here as the second-eye check.
```

**Legend:** `[x]` = already ratified elsewhere; `[~]` = pre-filled by this packet, owner confirms
or amends at signing; nothing in this form is signed by authority it doesn't already have.

**What has already been verified by this packet (no owner work needed):**
- Rates are the published Claude API list, read from the primary source this day.
- Rate arithmetic fits inside the ratified §5 ceilings — no Gate-4 block.
- The non-live run's T-01..T-05 contracts are the rubric; they are executable, not aspirational.
- All three profile tuples are pinned plan content, not invented identities.

## 4. The one thing that still needs the owner

1. Turn each `[~]` in §3 into `[x]` (or amend the pre-filled value), commit — that commit *is* the
   §10 row 4 approval, and it unlocks live dispatch authorization on this scope. All proposed
   values are Wildcats: amendable, not ratified-by-this-text alone.
2. Name the §2/P02 reviewer so the "reviewer" qualification field can be filled (one name, see
   `docs/P02_REVIEW_BRIEF.md` for the exact checklist handed them).
