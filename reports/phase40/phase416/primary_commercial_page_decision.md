# PHASE 4.16 — Primary Commercial Page Decision

## Decision

The **single primary commercial landing page** for the "wooden speaker cabinet manufacturer" head term is:

> **`custom-wooden-speaker-cabinet-manufacturer`** — retitled to **"Wooden Speaker Cabinet Manufacturer"** (was "Custom Wooden Speaker Cabinet Manufacturer").

## Rationale (from PHASE 4.15 baseline)

1. **4.15 rank-1 recommendation.** PHASE 4.15's `phase415_executive_decision_matrix.json` and `phase415_commercial_keyword_map.json` identified `custom-wooden-speaker-cabinet-manufacturer` as the strongest candidate to own the generic term (broadest existing content, covers custom + OEM + ODM + CNC + finishing).
2. **Broadest existing scope.** It already described full-service manufacturing (prototype → mass production, CNC, veneer, finishing, QC). It is the natural hub; the other pages are specializations of it.
3. **Lowest risk of content loss.** Broadening its title/H1 to the generic term required **no body-content deletion** — only front-matter string changes plus the addition of a cross-link band. Content loss = 0.

## What changed on the primary

| Field | Before | After |
|-------|--------|-------|
| `title` (H1) | Custom Wooden Speaker Cabinet Manufacturer | **Wooden Speaker Cabinet Manufacturer** |
| `yoast_title` | Custom Wooden Speaker Cabinet Manufacturer \| OEM Audio Enclosures | **Wooden Speaker Cabinet Manufacturer \| Woodsat** |
| `focus_keyword` | Custom Wooden Speaker Cabinet Manufacturer | **Wooden Speaker Cabinet Manufacturer** |
| `params.wp_post_title` | Custom Wooden Speaker Cabinet Manufacturer | **Wooden Speaker Cabinet Manufacturer** |
| `description` | (custom-focused) | expanded to "Woodsat is a professional wooden speaker cabinet manufacturer providing custom, OEM and ODM…" |
| Body | (unchanged) + added "Explore Related Woodsat Speaker Cabinet Services" card-grid | cross-links to all 6 siblings |

## Why NOT the others

- `oem` / `hifi` / `enclosure` / `box` / `empty` — each owns a **narrower intent** (OEM, audiophile, enclosure, box, empty). Promoting any of them to the generic head term would *create* cannibalization against the others, not resolve it.
- `speaker-cabinet-cnc-machining-service` — a **service/process** page, not a manufacturer landing page; wrong intent for the head term.
- `high-gloss-...` — a finishing **support** page, outside the STRONG cluster.
- `mdf-vs-baltic-birch-...` — a materials **comparison** page; editorial-style, not a manufacturer landing page. (De-orphaned via inbound links, not promoted.)

## Authority flow

The primary now receives inbound links from:
- 3 editorials (`wooden-vs-mdf-speaker-cabinets`, `speaker-box-materials`, `custom-cnc-wood-routing-services` — the last links to the CNC service page instead, which itself links to primary).
- The cross-link band on all 6 sibling pages (each sibling points to the primary first).
- The orphan materials page (primary → orphan link establishes the orphan, and the orphan's existing outbound links already fan out to siblings).

This concentrates internal authority on the single primary and satisfies PHASE 4.16 STEP 11 ("The primary commercial page should receive contextual links from relevant editorial pages").
