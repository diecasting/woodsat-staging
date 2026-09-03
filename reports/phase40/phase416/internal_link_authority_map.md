# PHASE 4.16 — Internal Link Authority Map

Maps every internal link added in 4.16. All new links use **relative URLs** (`/slug/`), processed by Hugo's `render-link` hook + `route.html` so they resolve as `/woodsat-staging/...` on staging and `/...` on production. No new absolute `https://woodsat.com/...` links were introduced.

## 1. Commercial → Commercial cross-link bands

A "Explore Related Woodsat … Services" `{{< card-grid cols=3 >}}` band was added to **7 commercial pages** (primary + 6 siblings/service). Each band links to the primary first, then the other siblings. This:
- Concentrates authority on the single primary (every sibling points up to it).
- Makes sibling intent explicit and navigable (reduces the STRONG cannibalization cluster structurally).

**Primary receives inbound cross-links from:** `oem`, `hifi`, `enclosure`, `box`, `empty`, `cnc`. Verified present in built HTML.

## 2. Editorial → Commercial (primary receives authority)

| Source editorial | Target commercial | Anchor text | Verified |
|------------------|-------------------|-------------|----------|
| `wooden-vs-mdf-speaker-cabinets` | `custom-wooden-speaker-cabinet-manufacturer` | "wooden speaker cabinet manufacturing team" | ✅ |
| `speaker-box-materials` | `custom-wooden-speaker-cabinet-manufacturer` | "wooden speaker cabinet manufacturer" | ✅ |
| `custom-cnc-wood-routing-services` | `speaker-cabinet-cnc-machining-service` | "speaker cabinet CNC machining service" | ✅ |

This satisfies PHASE 4.16 STEP 11 (primary receives contextual links from relevant editorials).

## 3. Orphan → de-orphaned (4 new inbound)

| Source | Target (orphan) | Anchor text | Verified |
|--------|-----------------|-------------|----------|
| `wooden-vs-mdf-speaker-cabinets` | `mdf-vs-baltic-birch-plywood-speaker-cabinets` | "factory-floor MDF vs Baltic Birch plywood deep dive" | ✅ |
| `speaker-box-materials` | same | "MDF vs Baltic Birch plywood speaker cabinet deep dive" | ✅ |
| `custom-cnc-wood-routing-services` | same | "MDF vs Baltic Birch plywood comparison" | ✅ |
| `custom-wooden-speaker-cabinet-manufacturer` (primary) | same | "MDF vs Baltic Birch plywood speaker cabinet deep dive" | ✅ |

**Orphan inbound count: 0 → 4.** The orphan is no longer isolated (PHASE 4.16 STEP 12 satisfied).

## 4. Natural-anchor rules applied

- Anchors use descriptive, intent-matching phrases (no exact-match stuffing of the head term beyond one natural use).
- All new links are contextual (placed inside relevant editorial sections / material-option sections), not footer dumps.
- No `rel="nofollow"` added; all are internal authority pass-through links.
