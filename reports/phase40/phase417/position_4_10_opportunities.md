# PHASE 4.17 — Position 4–10 Opportunities ("striking distance, page 1")

**GSC_DATA_AVAILABLE:** `false`
**Machine-readable twin:** `position_4_10_opportunities.csv` — header row + 1 explicit `NOT_AVAILABLE` status row, **0 fabricated data rows**
**Bucket status:** `NOT_AVAILABLE`

---

## 1. Result

**No queries can be placed in the 4–10 position bucket.** Average position is a Search Console-derived metric. There is no reachable Search Console property for Woodsat, therefore no position values exist for any query or page. Zero rows are emitted rather than inventing plausible ones.

This is a *blocked* measurement, not a measurement returning zero. The distinction is enforced deliberately: the credential probe returned `HTTP 403 — User does not have sufficient permission` for all six Woodsat property forms, which is **not** the same signal as an authorised query returning an empty result set. A 403 tells us nothing about traffic; an empty 200 would. We only have the former, so no traffic inference of any kind is permitted from it.

## 2. Why this bucket matters (kept for when data arrives)

Positions 4–10 are already on page 1 but below the click-dominant top-3. The economics: moving a query from position 6 to position 3 typically multiplies CTR several-fold with no new content required — the page is already deemed relevant. This bucket is therefore the cheapest genuine traffic gain available to any site, and it is the bucket where on-page and internal-link work pays back fastest.

## 3. Exact analysis that will run once access is granted

```
INPUT:  GSC Performance export, dimensions = query × page, 90-day window
FILTER: position >= 4 AND position <= 10 AND impressions >= 10
JOIN:   normalized page → gsc_url_mapping.json → slug
ENRICH: query_classification, query_cluster, intended_owner_slug_phase416,
        contextual_inbound_count, title_tag_len, meta_description_len
DERIVE: correct_owner            := (actual landing slug == intended owner slug)
        ctr_gap                  := expected_ctr(position) - observed_ctr
        internal_priority_score  := commercial_weight × impression_weight × ctr_gap
SORT:   internal_priority_score DESC
OUTPUT: position_4_10_opportunities.csv (real rows replace the status row)
```

## 4. Structural stand-in (clearly labelled, NOT a position estimate)

Position cannot be approximated. What *can* be stated is which pages are best positioned to convert a page-1 placement into clicks if they hold one, because SERP presentation quality is measurable offline:

| Page | Title length | Meta description length | SERP truncation risk | Contextual inbound |
|---|---|---|---|---|
| `custom-wooden-speaker-cabinet-manufacturer` | 45 | 198 | description truncates | 8 |
| `oem-wooden-speaker-cabinet-manufacturer` | **72** | 199 | **title + description truncate** | 7 |
| `speaker-cabinet-cnc-machining-service` | **71** | 184 | **title + description truncate** | 7 |
| `hifi-speaker-cabinet-manufacturer` | **70** | 182 | **title + description truncate** | **4** |
| `wooden-speaker-enclosure-manufacturer` | 64 | 209 | description truncates | 6 |
| `wooden-speaker-box-manufacturer` | 64 | 195 | description truncates | 6 |
| `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | 55 | 189 | description truncates | 11 |

Reading: **three of the seven commercial pages have titles that exceed the ~65-character SERP display budget** (`oem` 72, `cnc` 71, `hifi` 70). If any of them currently sits in positions 4–10, its snippet is being clipped mid-phrase, which suppresses CTR independently of ranking. That is a data-backed defect that would be actionable the moment position data confirms page-1 presence — and it is why these three top the structural priority ranking in `top_20_search_opportunities.json`.

**No claim is made here that these pages do or do not rank 4–10.**

## 5. Status

| Item | Value |
|---|---|
| Rows in bucket | 0 (blocked) |
| Fabricated rows | 0 |
| §12 requirement | **NOT_AVAILABLE** — documented, not skipped |
| Blocking dependency | Search Console access to a Woodsat property |
