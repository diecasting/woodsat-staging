# PHASE 4.17 — High Impression / Low CTR Analysis

**GSC_DATA_AVAILABLE:** `false`
**Impression / CTR findings:** `NOT_AVAILABLE`
**SERP-presentation findings:** **DATA-BACKED** (25 / 25 pages audited)

---

## 1. Result

The impression-and-CTR half of §16 is `NOT_AVAILABLE`. Impressions and CTR exist only in Search Console; no Woodsat property is reachable. No page is labelled "high impression" and no CTR value is stated anywhere in this report.

However, "high impression / low CTR" has two independent causes, and only one of them requires GSC:

| Cause | Requires GSC? | Status here |
|---|---|---|
| Ranking position too low for the impression volume | YES | `NOT_AVAILABLE` |
| **SERP snippet fails to earn the click at any position** | **NO** | **fully audited below** |

The second cause is measurable from the rendered `<head>` of every page. That audit was performed and is the substantive content of this report.

## 2. Title tag audit — SERP display budget (~65 characters)

3 of 25 pages exceed the display budget. All three are **commercial** pages.

| Page | Title length | Verdict |
|---|---|---|
| `oem-wooden-speaker-cabinet-manufacturer` | **72** | **TRUNCATED** — ~7 chars clipped |
| `speaker-cabinet-cnc-machining-service` | **71** | **TRUNCATED** — ~6 chars clipped |
| `hifi-speaker-cabinet-manufacturer` | **70** | **TRUNCATED** — ~5 chars clipped |
| `wooden-speaker-box-manufacturer` | 64 | at limit |
| `wooden-speaker-enclosure-manufacturer` | 64 | at limit |
| `speaker-box-materials` | 61 | OK |
| `speaker-box-calculator` | 60 | OK |
| 15 further pages | 45–59 | OK |
| `thanks` | **19** | below useful length (conversion page, low priority) |

**Why this matters more than it looks.** The three truncated titles are exactly the three highest-value non-primary commercial pages: OEM/ODM, CNC service and audiophile. In each case the clipped tail is the brand-differentiating suffix that 4.16 deliberately added to distinguish the siblings from one another (`| Custom Audio Enclosure Factory`, `| Precision Wood CNC Manufacturer`, `| Premium Wooden Speaker Enclosures`). The differentiation is being paid for in title length and then discarded by the SERP before the user sees it.

This is the reason these three pages occupy the top three slots of `top_20_search_opportunities.json` (`hifi` 72.0, `oem` 68.2, `cnc` 65.4) — each carries the maximum `serp_presentation_risk` component of 25/25.

## 3. Meta description audit — snippet budget (~160 characters)

**17 of 25 pages exceed 160 characters.**

| Page | Description length | Overshoot |
|---|---|---|
| `mdf-vs-baltic-birch-plywood-speaker-cabinets` | **336** | **+176 — more than double the budget** |
| `speaker-box-calculator` | 226 | +66 |
| `speaker-box-materials` | 214 | +54 |
| `wooden-speaker-enclosure-manufacturer` | 209 | +49 |
| `oem-wooden-speaker-cabinet-manufacturer` | 199 | +39 |
| `custom-wooden-speaker-cabinet-manufacturer` | 198 | +38 |
| `wooden-vs-mdf-speaker-cabinets` | 196 | +36 |
| `wooden-speaker-box-manufacturer` | 195 | +35 |
| `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | 189 | +29 |
| `speaker-cabinet-manufacturing` | 183 | +23 |
| `speaker-cabinet-cnc-machining-service` | 184 | +24 |
| `hifi-speaker-cabinet-manufacturer` | 182 | +22 |
| `wooden-speaker-cabinet-designs` | 180 | +20 |
| `subwoofer-enclosure-design` | 177 | +17 |
| `acoustic-wood-speaker-enclosures` | 176 | +16 |
| `custom-cnc-wood-routing-services` | 173 | +13 |
| `high-gloss-piano-lacquer-finishing-process-wood-speakers` | 170 | +10 |

Within budget (8 pages): `speaker-box-veneering` 160, `speaker-box-finishes` 155, `about-us` 150, `best-wood-for-speaker-boxes` 148, `thanks` 137, `resource` 135, `(home)` 134, `contact` 130.

**Severity is not uniform.** An overshoot of 10–30 characters usually costs the closing clause and is a minor CTR tax. `mdf-vs-baltic-birch-plywood-speaker-cabinets` at 336 characters loses roughly half its description — whatever call-to-action or differentiator sits in the second half is guaranteed never to render. That page is also the 4.16 de-orphaning target (raised from 0 to 4 contextual inbound links), so effort has already been invested in driving authority to a page whose snippet is half-invisible.

**All 7 commercial pages overshoot the description budget.** There is no commercial page with a snippet that renders in full.

## 4. Combined exposure ranking (data-backed, position-free)

Pages carrying *both* a truncated title and an over-budget description — i.e. both SERP lines degraded:

| Rank | Page | Title | Description | 4.16 role |
|---|---|---|---|---|
| 1 | `oem-wooden-speaker-cabinet-manufacturer` | 72 | 199 | OEM/ODM sibling |
| 2 | `speaker-cabinet-cnc-machining-service` | 71 | 184 | CNC service sibling |
| 3 | `hifi-speaker-cabinet-manufacturer` | 70 | 182 | audiophile sibling (**only 4 inbound links**) |

These three are the phase's P1 metadata recommendations. `hifi` ranks first overall in the opportunity model because it compounds the SERP defect with the weakest internal-link support of any commercial page.

## 5. What remains blocked

Without GSC, the following cannot be produced and are not guessed:

- which pages actually accumulate high impressions,
- observed CTR per page or per query,
- CTR gap versus position-expected CTR,
- whether a low CTR is caused by snippet quality or by ranking depth,
- ranking of pages by absolute click opportunity.

## 6. Status

| Item | Value |
|---|---|
| §16 impression/CTR requirement | **NOT_AVAILABLE** |
| §16 snippet-quality requirement | **DATA-BACKED — 25/25 pages audited** |
| Titles over budget | 3 (all commercial) |
| Descriptions over budget | 17 (including all 7 commercial) |
| Fabricated metrics | 0 |
