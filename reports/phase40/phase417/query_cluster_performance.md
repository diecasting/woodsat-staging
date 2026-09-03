# PHASE 4.17 — Query Cluster Performance

**GSC_DATA_AVAILABLE:** `false`
**Cluster performance metrics:** `NOT_AVAILABLE`
**Cluster composition & structural support:** **DATA-BACKED — 16 clusters**

---

## 1. Result

§21 asks for aggregate clicks, impressions, CTR and average position per query cluster. All are `NOT_AVAILABLE`. The cluster model itself, its owner assignments and its structural support are fully measured.

## 2. Cluster inventory with structural support (data-backed)

| Cluster | Queries | Dominant intent | Owner page(s) | Owner words | Owner contextual inbound | Clicks / Impr. / CTR / Pos. |
|---|---|---|---|---|---|---|
| brand | 4 | BRAND / NAV | `(home)`, `about-us`, `contact` | 1130 / 772 / 371 | 0 / 2 / 6 | NOT_AVAILABLE |
| speaker cabinet manufacturer | 3 | COMMERCIAL | `custom-wooden-speaker-cabinet-manufacturer` | 1239 | 8 | NOT_AVAILABLE |
| custom speaker cabinet | 1 | COMMERCIAL | `custom-wooden-speaker-cabinet-manufacturer` | 1239 | 8 | NOT_AVAILABLE |
| speaker cabinet supplier | 2 | COMMERCIAL | `custom-wooden-speaker-cabinet-manufacturer` | 1239 | 8 | NOT_AVAILABLE |
| OEM speaker cabinet | 4 | OEM_ODM | `oem-wooden-speaker-cabinet-manufacturer` | 1224 | 7 | NOT_AVAILABLE |
| CNC speaker cabinet | 4 | SERVICE | `speaker-cabinet-cnc-machining-service` (3), `custom-cnc-wood-routing-services` (1) | 1298 / 619 | 7 / 11 | NOT_AVAILABLE |
| HIFI speaker cabinet | 3 | PRODUCT_APPLICATION | `hifi-speaker-cabinet-manufacturer` | 1270 | **4** | NOT_AVAILABLE |
| speaker enclosure | 3 | COMMERCIAL / PRODUCT | `wooden-speaker-enclosure-manufacturer` (2), `acoustic-wood-speaker-enclosures` (1) | 1220 / 1331 | 6 / 8 | NOT_AVAILABLE |
| speaker box | 3 | COMMERCIAL / PRODUCT | `wooden-speaker-box-manufacturer` | 1272 | 6 | NOT_AVAILABLE |
| empty speaker box | 3 | PRODUCT / COMMERCIAL | `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | 1441 | 11 (**36 effective**) | NOT_AVAILABLE |
| subwoofer | 2 | PRODUCT / INFO | `subwoofer-enclosure-design` | 695 | 12 | NOT_AVAILABLE |
| **bookshelf speaker cabinet** | **1** | PRODUCT | **NONE** | — | — | NOT_AVAILABLE |
| MDF | 2 | MATERIALS / INFO | `mdf-vs-baltic-birch-plywood-speaker-cabinets`, `wooden-vs-mdf-speaker-cabinets` | 1087 / 837 | 4 / **2** | NOT_AVAILABLE |
| Baltic birch | 1 | MATERIALS | `mdf-vs-baltic-birch-plywood-speaker-cabinets` | 1087 | 4 | NOT_AVAILABLE |
| plywood | 1 | MATERIALS | `mdf-vs-baltic-birch-plywood-speaker-cabinets` | 1087 | 4 | NOT_AVAILABLE |
| materials | 9 | INFORMATIONAL | 8 informational pages | 619–1141 | 3–10 | NOT_AVAILABLE |

## 3. Cluster-level structural findings

**Q1 — Commercial clusters are complete; one product cluster is empty.**
15 of 16 clusters have at least one existing owner page. `bookshelf speaker cabinet` has none — the only structural hole in the cluster model.

**Q2 — The commercial cluster with the highest margin has the least internal support.**
`HIFI speaker cabinet` (3 audiophile queries) is served by a 1270-word page with only **4** contextual inbound links. Every other commercial cluster owner has 6–11. Content is adequate; support is not.

**Q3 — The CNC cluster is split across two pages of very unequal weight.**
3 queries → `speaker-cabinet-cnc-machining-service` (1298 words, 7 links); 1 query (`cnc wood routing`) → `custom-cnc-wood-routing-services` (**619 words**, 11 links). The support-lighter page carries the deeper content and vice versa. Worth noting: `custom-cnc-wood-routing-services` is the thinnest page in the site that owns a SERVICE-class query, yet is one of the best internally linked. If a CNC query underperforms, this asymmetry is the first place to look.

**Q4 — The MDF cluster has two owners and the weaker one is nearly orphaned.**
`mdf-vs-baltic-birch-plywood-speaker-cabinets` (1087 words, 4 links — de-orphaned by 4.16 from 0) and `wooden-vs-mdf-speaker-cabinets` (837 words, **2 links** — second-lowest in the site). Both are comparison pages on adjacent material questions. Structural cannibalization is marked `LOW` because their owned queries are disjoint (`mdf speaker cabinet` / `baltic birch` / `plywood` vs `mdf vs plywood speaker`), but the pair is the closest thing to a genuine overlap remaining in the architecture and should be the first candidate re-checked once GSC data exists.

**Q5 — The materials cluster is the largest by query count (9) and is served entirely by informational pages.**
This is architecturally correct — those queries are research-stage — but note the funnel consequence: 9 of 46 target queries land on pages whose job is to hand the visitor onward to a commercial page. Only 2 of the 8 materials-cluster pages contain a working contextual link to a commercial page (`speaker-box-materials` → primary hub; `wooden-vs-mdf-speaker-cabinets` → primary hub). The rest attempt it via legacy URLs that 301 into the empty-box sibling. The informational→commercial handoff is therefore largely misrouted (see `internal_link_opportunities.md`).

## 4. Cluster priority for future action (structural basis)

| Rank | Cluster | Rationale |
|---|---|---|
| 1 | HIFI speaker cabinet | highest margin, weakest support (4 links), owner title truncated |
| 2 | OEM speaker cabinet | 4 high-value queries, owner title truncated at 72 chars |
| 3 | speaker cabinet manufacturer / supplier / custom (6 queries, one owner) | hub starved relative to its own sibling |
| 4 | CNC speaker cabinet | split ownership with inverted depth/support |
| 5 | bookshelf speaker cabinet | no owner page — new-page decision required |
| 6 | MDF / Baltic birch / plywood | two adjacent owners, one near-orphaned |
| 7 | materials (9 queries) | handoff to commercial layer misrouted |

## 5. What remains blocked

Cluster-level click and impression share; which clusters drive actual traffic; CTR by cluster; average position by cluster; whether the materials cluster converts to commercial pageviews. Not estimated.

## 6. Status

| Item | Value |
|---|---|
| §21 GSC requirement | **NOT_AVAILABLE** |
| §21 structural requirement | **DATA-BACKED — 16/16 clusters profiled** |
| Clusters without an owner page | 1 (`bookshelf speaker cabinet`) |
| Clusters with split ownership | 3 (CNC, speaker enclosure, MDF) |
