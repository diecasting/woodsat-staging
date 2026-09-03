# PHASE 4.16 — Acceptance Matrix (18 Gates)

All gates must PASS before commit/push. Verified against the built `public/` output (Hugo v0.163.3, `--gc --minify`, exit 0, 27 pages).

| # | Gate | Criterion | Status | Evidence |
|---|-------|-----------|--------|----------|
| 1 | Single primary | Exactly 1 page owns the bare "wooden speaker cabinet manufacturer" head term | ✅ PASS | `custom-wooden-speaker-cabinet-manufacturer` = "Wooden Speaker Cabinet Manufacturer"; siblings keep distinct titles |
| 2 | Primary intent ownership | Primary broadened to own generic term (title/H1/focus) | ✅ PASS | `title`+`yoast_title`+`focus_keyword` = "Wooden Speaker Cabinet Manufacturer" |
| 3 | Sibling intent differentiation | 5 siblings + CNC differentiated by clear intent | ✅ PASS | OEM / Hi-Fi / Enclosure / Box / Empty / CNC titles & focus keywords distinct |
| 4 | Reduced STRONG cluster | 6-page STRONG cluster broken by hierarchy | ✅ PASS | Primary hub + cross-link bands; siblings no longer compete for bare term |
| 5 | Commercial→commercial links | Cross-link bands on sibling pages | ✅ PASS | 7 pages carry "Explore Related Woodsat … Services" bands; verified in build |
| 6 | Orphan fixed | `mdf-vs-baltic-birch` receives ≥1 inbound | ✅ PASS | **4 inbound** (3 editorial + 1 primary); verified in build |
| 7 | Editorial→commercial | Primary receives contextual editorial links | ✅ PASS | `wooden-vs-mdf` + `speaker-box-materials` → primary; `custom-cnc` → CNC service |
| 8 | Natural anchors | No over-optimized/exact-match stuffing | ✅ PASS | `internal_link_anchor_audit.md` |
| 9 | `thanks` title fixed | No longer "Sub-woofer Wooden Box manufacturer" | ✅ PASS | `Thanks You \| Woodsat` in build |
| 10 | `about-us` title improved | P2 title improvement applied | ✅ PASS | "Woodsat — Wooden Speaker Cabinet Manufacturer \| About Us" |
| 11 | Content loss = 0 | No body copy/heading/FAQ removed | ✅ PASS | `content_fingerprint_report.md` (10 deletions = metadata only) |
| 12 | Schema unchanged | No schema edits; prod-pinned | ✅ PASS | 25 JSON-LD blocks, 0 github.io; no schema diff |
| 13 | Canonical/robots/sitemap unchanged | Production-pinned, no github.io | ✅ PASS | canonical = `https://woodsat.com/...`; 0 github.io |
| 14 | Route behavior preserved | No new broken links; subpath correct | ✅ PASS | `route_regression_report.md` (0 4.16-introduced broken links) |
| 15 | Form behavior preserved | Formspree endpoint intact | ✅ PASS | `action=https://formspree.io/f/xdaqjegz` on RFQ pages |
| 16 | Visual identity unchanged | No new colors/images/CSS | ✅ PASS | `visual_regression_report.md` (additive bands only) |
| 17 | No fabrication / GSC | `GSC_DATA_AVAILABLE=false` respected | ✅ PASS | No GSC metrics cited anywhere |
| 18 | Build + no regressions | Hugo build clean; all checks green | ✅ PASS | exit 0; SEO/route/schema/form/visual all PASS |

## Gate verdict
**18 / 18 PASS.** Commit + push authorized.

## Out-of-scope (documented, not blocking)
- 15 legacy `https://woodsat.com/...` body links render without the `/woodsat-staging/` subpath (pre-existing render-link quirk; intentionally untouched per ROUTE HARD LOCK + 4.14 decision). See `route_regression_report.md`.
- Pixel-level multi-viewport screenshots not captured (no headless browser in sandbox); structural/layout-safety checks substitute. See `visual_regression_report.md`.
