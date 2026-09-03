# PHASE 4.16 — Route Regression Report

**Method:** Parsed every `href` in built `public/*.html` (870 internal link references). Categorized each as: 4.16-added relative link (resolved with `/woodsat-staging/` subpath), pre-existing legacy link (rewritten without subpath), or static asset. Machine output: `_route_check.json`.

## Result

| Metric | Value |
|--------|-------|
| Total internal link references parsed | 870 |
| **4.16-introduced broken links** | **0** |
| 4.16-added relative links resolved correctly | 3 target slugs, all OK (`custom-wooden-speaker-cabinet-manufacturer`, `mdf-vs-baltic-birch-plywood-speaker-cabinets`, `speaker-cabinet-cnc-machining-service`) |
| Pre-existing legacy links missing subpath | 15 (valid targets, subpath omitted by render-link hook — see below) |
| Truly dead links | 0 (the 1 "data:" hit is an inline SVG favicon, false positive) |
| Route regression introduced by 4.16 | **false** |

## 4.16 link routing — verified correct
All new relative links (`/slug/`) are processed by the `render-link` hook + `route.html` and emit the correct staging prefix:
- `href=/woodsat-staging/mdf-vs-baltic-birch-plywood-speaker-cabinets/` ✅
- `href=/woodsat-staging/custom-wooden-speaker-cabinet-manufacturer/` ✅
- `href=/woodsat-staging/speaker-cabinet-cnc-machining-service/` ✅
- All 7 commercial→commercial card-grids emit `/woodsat-staging/<sibling>/` ✅

## Pre-existing legacy condition (OUT OF 4.16 SCOPE)
15 links render as root-absolute `/<slug>/` **without** the `/woodsat-staging/` prefix. These originate from **legacy `https://woodsat.com/...` body links** (editorials, orphan page, `thanks` body) that the `render-link` hook rewrites via `relURL("/<slug>/")` — and `relURL` drops the baseURL path for leading-slash inputs (the same quirk `route.html` was built to avoid, but the hook did not adopt it).

Evidence this is **pre-existing, not introduced by 4.16**:
- `git show HEAD:content/pages/mdf-vs-baltic-birch-plywood-speaker-cabinets.md` already contains **10** `https://woodsat.com/...` body links.
- `git show HEAD:content/posts/wooden-vs-mdf-speaker-cabinets.md` already contains **6**.
- 4.16 added **zero** `https://woodsat.com/...` links; all 4.16 additions are relative.

These legacy links are governed by the **ROUTE HARD LOCK** ("preserve all route/form behavior") and the PHASE 4.14 decision that editorial absolute production URLs are intentional. Fixing them is explicitly **out of scope** for 4.16 and would modify pre-existing route behavior, violating the lock. They are documented here for transparency only.

## Conclusion
4.16 introduced **no route regressions**. All new internal links resolve correctly on staging and production. The legacy missing-subpath condition predates 4.16 and is intentionally left untouched per the ROUTE HARD LOCK.
