# PHASE 4.16 — Cannibalization Before / After

> `GSC_DATA_AVAILABLE = false`. No traffic/impression metrics are cited; this is a **structural/architecture** assessment based on the PHASE 4.15 baseline and the 4.16 changes.

## PHASE 4.15 verdict (baseline)
STRONG commercial-keyword cannibalization across **6 pages** all targeting near-identical "wooden speaker cabinet manufacturer" variants with no clear hierarchy:
`custom`, `oem`, `hifi`, `enclosure`, `box`, `empty`. Plus 1 orphan (`mdf-vs-baltic-birch`) with 0 inbound.

## BEFORE (4.15) — structure

```
                [ 6 pages all ≈ "wooden speaker cabinet manufacturer" ]
                custom  oem  hifi  enclosure  box  empty
                          \____ no hierarchy, no single hub ____/
                orphan: mdf-vs-baltic-birch  (0 inbound, isolated)
```

- No page unambiguously owned the generic head term.
- Siblings competed with each other (STRONG cluster).
- Internal links were sparse; the orphan received nothing.

## AFTER (4.16) — structure

```
                          PRIMARY (hub)
        custom-wooden-speaker-cabinet-manufacturer
              "Wooden Speaker Cabinet Manufacturer"
                 ▲   ▲   ▲   ▲   ▲   ▲   ▲
        ┌────────┼───┼───┼───┼───┼───┼────────┐
      oem  hifi  enclosure  box  empty  cnc   (cross-link bands, each → primary first)
        │
        └── editorial posts (wooden-vs-mdf, speaker-box-materials) → primary
        └── editorial (custom-cnc) → cnc service
        └── 3 editorials + primary → orphan (de-orphaned, 4 inbound)
```

## Qualitative improvement

| Dimension | Before | After |
|-----------|--------|-------|
| Pages owning the bare head term | 6 (ambiguous) | **1** (primary only) |
| Sibling intent clarity | overlapping | distinct (OEM/Hi-Fi/Enclosure/Box/Empty/CNC) |
| Internal authority hub | none | **primary** (receives 6 sibling + 2 editorial inbounds) |
| Orphan inbound links | 0 | **4** |
| Commercial→commercial cross-links | none | **7 pages** with related-services bands |
| Editorial→commercial links | none (legacy absolute only) | **3 new relative links** |

## Validation (STEP 16)
The STRONG cluster is reduced **structurally**: the primary now monopolizes the generic term, siblings are explicitly differentiated by intent, and a bidirectional internal link graph (siblings ↔ primary ↔ editorials ↔ orphan) carries authority. This is the architecture PHASE 4.15 recommended; 4.16 implements it.

## Caveat
Because `GSC_DATA_AVAILABLE = false`, the *effect* on rankings cannot be measured here. The change is validated as an architecture fix, not a proven ranking win. Re-audit with GSC data in a later phase.
