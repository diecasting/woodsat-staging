# PHASE 4.17 — Top Commercial Keywords

**GSC_DATA_AVAILABLE:** `false`
**Ranking by search performance:** `NOT_AVAILABLE`
**Ranking by commercial value × structural readiness:** **DATA-BACKED**

---

## 1. Basis of this ranking

§27 asks for the top commercial keywords ranked by opportunity. Without GSC there are no impressions to rank by, so ranking is derived from two measured inputs:

1. **Commercial value tier** — assigned by intent class, per the 4.16 model. OEM/ODM enquiries are the highest-value outcome for a contract manufacturer; audiophile/hi-fi is the highest-margin product segment; generic commercial head terms are high-volume but lower-qualification.
2. **Structural readiness of the owner page** — contextual inbound links, word count, title/description budget compliance. Measured directly from the build.

The ranking answers *"which commercial keyword is best worth attention, and is its page ready?"* — not *"which keyword gets the most impressions"*.

## 2. The 28 commercial-intent queries with owner readiness

All performance columns are `NOT_AVAILABLE` and are omitted rather than shown as empty noise.

### Tier 1 — OEM / ODM (highest value, 4 queries)

| Query | Owner | Owner inbound | Owner words | Title | Desc | Readiness |
|---|---|---|---|---|---|---|
| `oem wooden speaker cabinet manufacturer` | `oem-wooden-speaker-cabinet-manufacturer` | 7 | 1224 | **72 ✗** | 199 ✗ | **snippet defect** |
| `oem speaker cabinet` | same | 7 | 1224 | **72 ✗** | 199 ✗ | **snippet defect** |
| `speaker cabinet oem manufacturer` | same | 7 | 1224 | **72 ✗** | 199 ✗ | **snippet defect** |
| `odm speaker enclosure` | same | 7 | 1224 | **72 ✗** | 199 ✗ | **snippet defect** |

Four highest-value queries share one owner whose title is clipped by ~7 characters, discarding `| Custom Audio Enclosure Factory` — the exact phrase that qualifies the page as an OEM supplier.

### Tier 2 — Audiophile / Hi-Fi (highest margin, 3 queries)

| Query | Owner | Owner inbound | Owner words | Title | Desc | Readiness |
|---|---|---|---|---|---|---|
| `hifi speaker cabinet manufacturer` | `hifi-speaker-cabinet-manufacturer` | **4** | 1270 | **70 ✗** | 182 ✗ | **worst in set** |
| `hifi speaker cabinet` | same | **4** | 1270 | **70 ✗** | 182 ✗ | **worst in set** |
| `audiophile speaker cabinet` | same | **4** | 1270 | **70 ✗** | 182 ✗ | **worst in set** |

The highest-margin segment is served by the least internally supported commercial page in the site (4 links vs 6–11 elsewhere), with a clipped title. Content is not the problem — 1270 words, 16 H2s. Support and presentation are.

### Tier 3 — Primary commercial head terms (6 queries)

| Query | Owner | Owner inbound | Title | Desc |
|---|---|---|---|---|
| `wooden speaker cabinet manufacturer` | `custom-wooden-speaker-cabinet-manufacturer` | 8 | 45 ✓ | 198 ✗ |
| `speaker cabinet manufacturer` | same | 8 | 45 ✓ | 198 ✗ |
| `custom speaker cabinet manufacturer` | same | 8 | 45 ✓ | 198 ✗ |
| `speaker cabinet supplier` | same | 8 | 45 ✓ | 198 ✗ |
| `wooden speaker cabinet supplier` | same | 8 | 45 ✓ | 198 ✗ |
| `speaker cabinet factory` | same | 8 | 45 ✓ | 198 ✗ |

Six head terms on one hub. Title is well within budget. The defect is authority: the hub holds 8 contextual inbound links while its empty-box sibling effectively holds 36 — and 25 of those carry anchor text written for *this* page (see `wrong_landing_page_analysis.md`).

### Tier 4 — CNC / manufacturing service (4 queries)

| Query | Owner | Owner inbound | Owner words | Title |
|---|---|---|---|---|
| `speaker cabinet cnc machining` | `speaker-cabinet-cnc-machining-service` | 7 | 1298 | **71 ✗** |
| `speaker cabinet cnc machining service` | same | 7 | 1298 | **71 ✗** |
| `cnc speaker cabinet manufacturing` | same | 7 | 1298 | **71 ✗** |
| `cnc wood routing` | `custom-cnc-wood-routing-services` | 11 | **619** | 56 ✓ |

Split ownership with inverted profiles: the 3-query owner has depth (1298 words) but a clipped title; the 1-query owner has the best link support in the informational layer (11) but the thinnest body in the site owning a service query (619 words).

### Tier 5 — Enclosure / box / empty terminology variants (11 queries)

| Query | Owner | Owner inbound | Desc |
|---|---|---|---|
| `wooden speaker enclosure manufacturer` | `wooden-speaker-enclosure-manufacturer` | 6 | 209 ✗ |
| `speaker enclosure manufacturer` | same | 6 | 209 ✗ |
| `acoustic speaker enclosure` | `acoustic-wood-speaker-enclosures` | 8 | 176 ✗ |
| `wooden speaker box manufacturer` | `wooden-speaker-box-manufacturer` | 6 | 195 ✗ |
| `speaker box manufacturer` | same | 6 | 195 ✗ |
| `speaker box` | same | 6 | 195 ✗ |
| `empty speaker cabinet manufacturer` | `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | 11 (36 eff.) | 189 ✗ |
| `empty speaker box` | same | 11 (36 eff.) | 189 ✗ |
| `blank speaker cabinet` | same | 11 (36 eff.) | 189 ✗ |
| `subwoofer cabinet` | `subwoofer-enclosure-design` | 12 | 177 ✗ |
| `bookshelf speaker cabinet` | **NONE** | — | — | 

## 3. Findings

**K1 — Value and readiness are inversely correlated.** The two highest-value tiers (OEM, hi-fi) are served by the two commercial pages with the worst presentation defects, and hi-fi additionally has the weakest link support. The lowest-value commercial tier (empty/blank boxes) has by far the strongest support.

**K2 — Every commercial keyword in the universe has an owner except one.** 27 of 28 commercial-intent queries resolve to an existing, adequately-deep page. `bookshelf speaker cabinet` has none.

**K3 — No commercial keyword suffers from thin content.** All owner pages sit at 1220–1441 words except `custom-cnc-wood-routing-services` (619). Content volume is not the lever here.

**K4 — Two commercial head terms have no place in the architecture at all**, discovered via legacy URL analysis: `loudspeaker cabinet manufacturer` and `custom speaker cabinet builder` both had dedicated production URLs that now 301 to the empty-box page. Neither term appears in the 46-query universe. If they carried historical relevance, that relevance is now pointed at a page about empty boxes.

## 4. Recommended attention order (structural basis)

1. `hifi speaker cabinet` cluster — highest margin, worst-supported owner.
2. `oem …` cluster — highest value, clipped qualifying title.
3. `wooden speaker cabinet manufacturer` cluster — hub starved by its own sibling.
4. `speaker cabinet cnc machining` cluster — clipped title + split-ownership asymmetry.
5. `bookshelf speaker cabinet` — new-page decision.
6. `loudspeaker cabinet manufacturer` — evaluate as an unowned head term.

## 5. Status

| Item | Value |
|---|---|
| §27 GSC ranking requirement | **NOT_AVAILABLE** |
| §27 commercial keyword inventory | **DATA-BACKED — 28 queries, 27 with owners** |
| Fabricated metrics | 0 |
