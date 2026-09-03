# PHASE 4.14 — Image / Internal Link / Content SEO QA

**Status:** PHASE_4.14 = IMAGE_INTERNAL_LINK_CONTENT_SEO_QA_PASS
**Generated:** 2026-09-03 11:18 UTC
**Site:** https://diecasting.github.io/woodsat-staging/ (baseURL subpath `/woodsat-staging/`; canonical/OG pinned to production `https://woodsat.com`)
**Pages audited:** 25 (from sitemap.xml)

## Scope & Locks
QA-only phase. No WordPress/Cloudflare/DNS/production changes. No Title/Meta/H1/H2-H4/paragraph
rewrites, no fabricated content, no AI/external images, no Schema/Formspree/route.html changes,
no Header/Hero/Footer/Walnut-Copper-Sand redesign. Auto-fixes limited to P0/P1 (broken links,
broken images, wrong staging routes). P2/P3 recorded only.

## What changed (P0/P1 auto-fixes applied)
1. **Resource page dead links fixed.** `content/resource/_index.md` had two links to non-existent
   pages — `{< card link="/blueprints/" >}` and `[Download All Resources](/download-resources)`
   — both 404 on staging (and production). Repointed both to `/contact/` (existing RFQ page;
   resource-request pathway).
2. **Production-absolute internal links rewritten to staging routes.** The existing
   `layouts/_default/_markup/render-link.html` (PHASE 4.9 routing hook) left `http(s)` links
   untouched, so 124 body links authored as `https://woodsat.com/<slug>/` leaked to production and
   violated PART 21. Extended the hook to rewrite `https://woodsat.com/<known-internal-slug>/` to
   `relURL` (so they resolve as `/woodsat-staging/<slug>/` on staging and `/<slug>/` on production).
   Only REAL internal slugs are rewritten; 7 ghost legacy WP slugs + 1 wp-content media asset stay
   production-absolute (they 301-redirect, not 404). Net: hardcoded-production internal links
   **124 → 0** (to existing pages); 29 production-absolute links remain and are all ghost/asset.

## Images
- total images: **132**
- broken images: **0** (gate PASS)
- missing alt: **0**
- weak/generic alt: **0** (all 14 are external `wp-content/uploads/...` production media; recorded P2, not rewritten)
- alt changed: **0** (no missing/incorrect/keyword-stuffed alts found)
- semantic mismatch (FAIL): **0** (semantic relevance 132/132 PASS)

## Internal Links
- total internal links: **776**
- unique targets: **29**
- orphan pages: **2** (classified below)
- weakly connected pages: **1**
- broken links: **0** (gate PASS — 0 staging-404s)
- anchor issues: generic anchors = **0** (majority descriptive)
- commercial pathways: **10**/10 editorial pages already link to a relevant commercial page

## Content
- heading text loss: **0**
- paragraph loss: **0**
- list item loss: **0**
- table data loss: **0**
(Measured BEFORE vs AFTER build; only link hrefs + 2 link targets changed — text untouched.)

## SEO
- Title regression: **0**
- Meta regression: **0**
- Canonical regression: **0**
- OG regression: **0**
- Robots regression: **0**
- Schema (JSON-LD) regression: **0**

## Route
- bare `/contact/`: **0**
- double prefix: **0**
- broken staging links: **0**
- hardcoded production internal links (existing pages): **124 → 0** (29 ghost/asset remain, recorded)

## Form
- Formspree endpoint: **https://formspree.io/f/xdaqjegz** (unchanged)
- method: **POST** (unchanged)
- fields: **your-name / your-email / your-message** (unchanged)
- regressions: **0**

## Visual (Playwright, 1440/1024/768/390/375)
- combos checked: **125**
- overflow combos: **0** (max 0px)
- desktop overflow: **0**
- tablet overflow: **0**
- mobile overflow: **0**
- broken images (LOCAL only): **0**
- external false-positive broken (blocked by design): **660**
- gate: **PASS**

## Orphan / Weak pages
- **https://woodsat.com/mdf-vs-baltic-birch-plywood-speaker-cabinets/** — EDITORIAL_PAGE — No inbound internal links from any other page. True orphan unless reached via nav/footer or external.
- **https://woodsat.com/thanks/** — SYSTEM_PAGE — No inbound internal links from any other page. True orphan unless reached via nav/footer or external.
- **https://woodsat.com/mdf-vs-baltic-birch-plywood-speaker-cabinets/** — WEAK_COMMERCIAL_CONNECTION — Editorial page with <=1 inbound internal link; limited discovery pathway.

## Recorded-only findings (P2/P3 — no auto-change this phase)
- **28 production-ghost links** (7 legacy WP slugs, e.g.
  `custom-speaker-cabinet-builder`, `most-durable-wood-for-speakers`) appear in body content and
  point to pages that no longer exist (301 on production). Recommendation: repoint to the nearest
  existing relevant page or remove in a future content phase.
- **0 generic alts** on external wp-content media (decorative legacy assets).
- **1 weakly-connected editorial page(s)** with <=1 inbound internal link; consider
  adding a natural link from a related commercial/service page (future phase).
- `--wood-muted` AA contrast opportunity carried over from PHASE 4.12 — deferred (would require a
  new colour token; out of scope).

## Pre-existing anomalies (not 4.14 regressions; HARD LOCK forbids H1 changes)
- `thanks` page has **H1 = 0** (system thank-you page, no heading).
- `wooden-vs-mdf-speaker-cabinets` has **H1 = 2** (theme/hero + article H1 conflict).
Both are pre-existing and recorded for a future content/theme phase; they are not introduced by 4.14.

## Gate
- broken_images: PASS
- broken_internal_links: PASS
- wrong_staging_routes: PASS
- double_prefix: PASS
- heading_text_loss: PASS
- paragraph_loss: PASS
- list_item_loss: PASS
- table_data_loss: PASS
- title_regression: PASS
- meta_regression: PASS
- canonical_regression: PASS
- og_regression: PASS
- robots_regression: PASS
- schema_regression: PASS
- formspree_regression: PASS
- desktop_overflow: PASS
- tablet_overflow: PASS
- mobile_overflow: PASS
- credential_scan: PASS

**VERDICT:** PHASE_4.14 = IMAGE_INTERNAL_LINK_CONTENT_SEO_QA_PASS
