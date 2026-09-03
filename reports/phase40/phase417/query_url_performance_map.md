# PHASE 4.17 — Query → URL Performance Map

**GSC_DATA_AVAILABLE:** `false`
**Machine-readable twin:** `query_url_performance_map.csv` (46 rows, 18 columns)
**Evidence class:** query taxonomy + ownership = **DATA-BACKED**; all performance columns = **NOT_AVAILABLE**

---

## 1. What this report can and cannot say

Section 11 asks for a map from query → landing URL with clicks / impressions / CTR / position. Because no Search Console property for Woodsat is reachable (see `gsc_data_availability.md`), the six performance columns cannot be populated by any legitimate means. They are emitted as the literal token `NOT_AVAILABLE` in the CSV, never as `0`, never as an estimate.

What **is** fully data-backed and delivered here:

- the query universe carried forward from 4.15 / 4.16 (46 target queries),
- the intent classification of every query (§9 taxonomy),
- the cluster each query belongs to,
- the page 4.16 designated as the **intended owner** of that query,
- whether that owner page actually exists in the build,
- the owner page's contextual inbound link count and word count,
- the structural cannibalization state after 4.16.

The missing half is the *observed* half: which URL Google actually serves, and at what position. That half is blocked on access, not on effort.

## 2. Query universe composition (46 queries, data-backed)

| Classification | Queries | Share |
|---|---|---|
| COMMERCIAL | 11 | 23.9% |
| INFORMATIONAL | 11 | 23.9% |
| PRODUCT_APPLICATION | 9 | 19.6% |
| OEM_ODM | 4 | 8.7% |
| SERVICE | 4 | 8.7% |
| BRAND | 3 | 6.5% |
| MATERIALS | 3 | 6.5% |
| NAVIGATIONAL | 1 | 2.2% |
| **Total** | **46** | **100%** |

Non-brand share = 42 / 46 = **91.3%**. The target universe is overwhelmingly non-brand and money-intent-heavy: COMMERCIAL + OEM_ODM + SERVICE + PRODUCT_APPLICATION = 28 / 46 = **60.9%**.

## 3. Cluster → owner assignment (16 clusters, data-backed)

| Cluster | Queries | Intended owner (4.16) | Owner exists | Owner contextual inbound |
|---|---|---|---|---|
| brand | 4 | `(home)` / `about-us` / `contact` | YES | 0 / 2 / 6 |
| speaker cabinet manufacturer | 3 | `custom-wooden-speaker-cabinet-manufacturer` | YES | 8 |
| custom speaker cabinet | 1 | `custom-wooden-speaker-cabinet-manufacturer` | YES | 8 |
| speaker cabinet supplier | 2 | `custom-wooden-speaker-cabinet-manufacturer` | YES | 8 |
| OEM speaker cabinet | 4 | `oem-wooden-speaker-cabinet-manufacturer` | YES | 7 |
| CNC speaker cabinet | 4 | `speaker-cabinet-cnc-machining-service` (3) / `custom-cnc-wood-routing-services` (1) | YES | 7 / 11 |
| HIFI speaker cabinet | 3 | `hifi-speaker-cabinet-manufacturer` | YES | **4 (lowest of any commercial page)** |
| speaker enclosure | 3 | `wooden-speaker-enclosure-manufacturer` (2) / `acoustic-wood-speaker-enclosures` (1) | YES | 6 / 8 |
| speaker box | 3 | `wooden-speaker-box-manufacturer` | YES | 6 |
| empty speaker box | 3 | `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | YES | 11 |
| subwoofer | 2 | `subwoofer-enclosure-design` | YES | 12 |
| **bookshelf speaker cabinet** | **1** | **NONE** | **NO — content gap** | — |
| MDF | 2 | `mdf-vs-baltic-birch-plywood-speaker-cabinets` / `wooden-vs-mdf-speaker-cabinets` | YES | 4 / 2 |
| Baltic birch | 1 | `mdf-vs-baltic-birch-plywood-speaker-cabinets` | YES | 4 |
| plywood | 1 | `mdf-vs-baltic-birch-plywood-speaker-cabinets` | YES | 4 |
| materials | 9 | 8 informational pages | YES | 3–10 |

**Owner coverage: 45 / 46 queries (97.8%) have an existing owner page. 1 query has none.**

## 4. Findings that survive the absence of GSC data

**F1 — Ownership is architecturally complete except for one gap.**
Every query class except `bookshelf speaker cabinet` resolves to exactly one designated owner page that exists in the build. 4.16 did its job: there is no query in the universe with two co-equal claimants.

**F2 — `hifi` is the weakest-supported commercial page in the set.**
`hifi-speaker-cabinet-manufacturer` owns 3 PRODUCT_APPLICATION queries in the audiophile cluster — the highest-margin segment in the 4.16 model — yet receives only **4** contextual inbound links, against 7 for `oem`, 7 for `cnc`, 8 for the primary hub and 11 for `empty`. Internal support is inversely correlated with commercial value in exactly the wrong direction.

**F3 — Structural cannibalization is resolved, not merely reduced.**
Of the 46 rows: 15 are marked `RESOLVED_STRUCTURALLY_4.16`, 27 `LOW`, 4 `N/A` (brand/navigational). **Zero** rows carry a HIGH or MEDIUM structural cannibalization risk. The 4.16 sibling split (oem / hifi / enclosure / box / empty / cnc under one primary) removed the duplicate-claimant condition.

**F4 — One query has no landing page at all.**
`bookshelf speaker cabinet` (PRODUCT_APPLICATION) has no owner. Notably, the phrase *is* present in a legacy production asset filename (`.../high-gloss-piano-lacquer-bookshelf-speaker-cabinet.png`), so the topic is already visually represented on the site without a page to rank. Detailed in `content_gap_vs_existing_page.md`.

## 5. Column dictionary of the CSV

| Column | Source | Status |
|---|---|---|
| `query` | 4.15 / 4.16 keyword universe | DATA-BACKED |
| `query_classification` | §9 taxonomy applied to the query string | DATA-BACKED |
| `query_cluster` | 4.16 cluster model | DATA-BACKED |
| `intended_owner_slug_phase416` | 4.16 `commercial_intent_map.json` | DATA-BACKED |
| `intended_owner_production_url` | `gsc_url_mapping.json` | DATA-BACKED |
| `owner_page_exists` | `public/` build scan | DATA-BACKED |
| `actual_gsc_landing_page` | Search Console | **NOT_AVAILABLE** |
| `correct_owner` | requires actual landing page | **NOT_AVAILABLE** |
| `clicks` / `impressions` / `ctr` / `position` | Search Console | **NOT_AVAILABLE** |
| `cannibalization_risk_gsc` | requires multi-URL query data | **NOT_AVAILABLE** |
| `cannibalization_risk_structural` | on-page + link graph | DATA-BACKED |
| `opportunity_class` | classification only | DATA-BACKED |
| `contextual_inbound_links` | `<main>` link graph | DATA-BACKED |
| `owner_word_count` | rendered body text | DATA-BACKED |
| `evidence_class` | provenance tag on every row | DATA-BACKED |

## 6. Status

| Item | Value |
|---|---|
| §11 requirement | **PARTIAL** — structure delivered, performance columns blocked |
| Rows emitted | 46 |
| Rows with fabricated metrics | **0** |
