# PHASE 4.16 — Commercial Page Inventory

**Objective:** Resolve the STRONG commercial-keyword cannibalization identified in PHASE 4.15 by establishing ONE primary commercial landing page, differentiating 6 sibling pages by intent, and strengthening internal authority flow — without touching WordPress / production / Cloudflare / DNS, schema architecture, canonical/robots/sitemap, Formspree, visual identity, or fabricating any content or GSC data.

## Summary

- **Commercial pages in scope:** 9 (1 primary + 5 STRONG-cluster siblings + 1 CNC service + 1 finishing support + 1 orphan materials page).
- **STRONG cannibalization cluster (pre-4.16):** 6 pages (`custom`, `oem`, `hifi`, `enclosure`, `box`, `empty`) all competing for "wooden speaker cabinet manufacturer" variants.
- **Primary chosen:** `custom-wooden-speaker-cabinet-manufacturer`, broadened to own the generic head term **"Wooden Speaker Cabinet Manufacturer"**.
- **Orphan fixed:** `mdf-vs-baltic-birch-plywood-speaker-cabinets` received **4 new inbound contextual links** (3 editorial + 1 primary commercial) and is no longer isolated.

## Page-by-page role

| # | Slug | Role | Intent owned |
|---|------|------|--------------|
| 1 | `custom-wooden-speaker-cabinet-manufacturer` | **PRIMARY** | Broad "wooden speaker cabinet manufacturer" (all capabilities) |
| 2 | `oem-wooden-speaker-cabinet-manufacturer` | SIBLING | OEM / ODM contract manufacturing |
| 3 | `hifi-speaker-cabinet-manufacturer` | SIBLING | Hi-Fi / audiophile / high-end acoustic |
| 4 | `wooden-speaker-enclosure-manufacturer` | SIBLING | Acoustic enclosures (technical) |
| 5 | `wooden-speaker-box-manufacturer` | SIBLING | Speaker boxes (general cabinets) |
| 6 | `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | SIBLING | Empty / unfinished cabinets (blank boxes) |
| 7 | `speaker-cabinet-cnc-machining-service` | SERVICE | CNC machining service (process) |
| 8 | `high-gloss-piano-lacquer-finishing-process-wood-speakers` | SUPPORT | Finishing process (outside STRONG cluster) |
| 9 | `mdf-vs-baltic-birch-plywood-speaker-cabinets` | ORPHAN→LINKED | Materials deep-dive (de-orphaned in 4.16) |

## Key structural changes (4.16)

1. **Single primary** — exactly one page owns the generic "Wooden Speaker Cabinet Manufacturer" title/H1/focus keyword. The other 6 siblings keep their distinctive intent-modified titles (OEM / Hi-Fi / Enclosure / Box / Empty / CNC).
2. **Commercial→commercial cross-link bands** added to all 6 sibling pages + the CNC page, using the existing `{{< card-grid >}}` + `link="/slug/"` pattern with relative URLs (rendered as `/woodsat-staging/...` on staging, `/...` on production — no route regression).
3. **Orphan inbound** — 4 contextual links now point to `mdf-vs-baltic-birch-plywood-speaker-cabinets` (verified in built HTML: 4 referencing files).
4. **Editorial→commercial** — `wooden-vs-mdf-speaker-cabinets` and `speaker-box-materials` link to the primary; `custom-cnc-wood-routing-services` links to the CNC service page.
5. **Title anomalies fixed** — `thanks` now renders "Thank You | Woodsat"; `about-us` title improved (P2).

See `commercial_intent_map.md`, `primary_commercial_page_decision.md`, and `internal_link_authority_map.md` for detail.
