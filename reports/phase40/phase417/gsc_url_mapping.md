# PHASE 4.17 — GSC URL Normalization & Mapping

**Phase:** 4.17 — GSC Data + Search Performance Opportunity Analysis
**Mode:** READ-ONLY / ANALYSIS-ONLY
**GSC_DATA_AVAILABLE:** `false`
**Baseline commit:** `366334a`
**Machine-readable twin:** `gsc_url_mapping.json`

---

## 1. Purpose

Section 8 of the phase brief requires a canonical mapping between the URLs that Google Search Console would report and the routes that exist in the Hugo staging build, so that any future GSC export can be joined to the site structure without ambiguity.

This mapping is **fully data-backed**. It does not depend on GSC. It was derived from the built artefacts in `public/` plus `public/sitemap.xml`, not from assumptions.

## 2. Normalization rule applied

GSC reports pages by their **absolute, canonical, indexable URL**. The staging build is served from a sub-path and is deliberately excluded from indexing, so the two never coincide. The mapping key is therefore the **production canonical URL**, and the staging route is stored as an analysis-only alias:

```
GSC page key        := https://woodsat.com/<slug>/          (canonical, production)
Staging alias       := https://diecasting.github.io/woodsat-staging/<slug>/   (analysis only)
Join key            := <slug>
```

Normalization steps encoded in `gsc_url_mapping.json`:

1. Force scheme `https`.
2. Force host `woodsat.com` (no `www`; the `www` variant is not the canonical form emitted by the build).
3. Force trailing slash — Hugo emits directory-style URLs (`/slug/index.html`), so every page URL ends in `/`.
4. Strip query strings and fragments.
5. Home page normalizes to `https://woodsat.com/` with the empty slug, recorded as `(home)`.

## 3. Mapping table (25 / 25 pages mapped)

| Slug | Production URL (GSC key) | Staging route (analysis alias) | Canonical host = production | In sitemap | `meta robots` on staging |
|---|---|---|---|---|---|
| `(home)` | https://woodsat.com/ | `/woodsat-staging/` | YES | YES | noindex,nofollow |
| `about-us` | https://woodsat.com/about-us/ | `/woodsat-staging/about-us/` | YES | YES | noindex,nofollow |
| `acoustic-wood-speaker-enclosures` | https://woodsat.com/acoustic-wood-speaker-enclosures/ | `/woodsat-staging/acoustic-wood-speaker-enclosures/` | YES | YES | noindex,nofollow |
| `best-wood-for-speaker-boxes` | https://woodsat.com/best-wood-for-speaker-boxes/ | `/woodsat-staging/best-wood-for-speaker-boxes/` | YES | YES | noindex,nofollow |
| `contact` | https://woodsat.com/contact/ | `/woodsat-staging/contact/` | YES | YES | noindex,nofollow |
| `custom-cnc-wood-routing-services` | https://woodsat.com/custom-cnc-wood-routing-services/ | `/woodsat-staging/custom-cnc-wood-routing-services/` | YES | YES | noindex,nofollow |
| `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | https://woodsat.com/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/ | `/woodsat-staging/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` | YES | YES | noindex,nofollow |
| `custom-wooden-speaker-cabinet-manufacturer` | https://woodsat.com/custom-wooden-speaker-cabinet-manufacturer/ | `/woodsat-staging/custom-wooden-speaker-cabinet-manufacturer/` | YES | YES | noindex,nofollow |
| `hifi-speaker-cabinet-manufacturer` | https://woodsat.com/hifi-speaker-cabinet-manufacturer/ | `/woodsat-staging/hifi-speaker-cabinet-manufacturer/` | YES | YES | noindex,nofollow |
| `high-gloss-piano-lacquer-finishing-process-wood-speakers` | https://woodsat.com/high-gloss-piano-lacquer-finishing-process-wood-speakers/ | `/woodsat-staging/high-gloss-piano-lacquer-finishing-process-wood-speakers/` | YES | YES | noindex,nofollow |
| `mdf-vs-baltic-birch-plywood-speaker-cabinets` | https://woodsat.com/mdf-vs-baltic-birch-plywood-speaker-cabinets/ | `/woodsat-staging/mdf-vs-baltic-birch-plywood-speaker-cabinets/` | YES | YES | noindex,nofollow |
| `oem-wooden-speaker-cabinet-manufacturer` | https://woodsat.com/oem-wooden-speaker-cabinet-manufacturer/ | `/woodsat-staging/oem-wooden-speaker-cabinet-manufacturer/` | YES | YES | noindex,nofollow |
| `resource` | https://woodsat.com/resource/ | `/woodsat-staging/resource/` | YES | YES | noindex,nofollow |
| `speaker-box-calculator` | https://woodsat.com/speaker-box-calculator/ | `/woodsat-staging/speaker-box-calculator/` | YES | YES | noindex,nofollow |
| `speaker-box-finishes` | https://woodsat.com/speaker-box-finishes/ | `/woodsat-staging/speaker-box-finishes/` | YES | YES | noindex,nofollow |
| `speaker-box-materials` | https://woodsat.com/speaker-box-materials/ | `/woodsat-staging/speaker-box-materials/` | YES | YES | noindex,nofollow |
| `speaker-box-veneering` | https://woodsat.com/speaker-box-veneering/ | `/woodsat-staging/speaker-box-veneering/` | YES | YES | noindex,nofollow |
| `speaker-cabinet-cnc-machining-service` | https://woodsat.com/speaker-cabinet-cnc-machining-service/ | `/woodsat-staging/speaker-cabinet-cnc-machining-service/` | YES | YES | noindex,nofollow |
| `speaker-cabinet-manufacturing` | https://woodsat.com/speaker-cabinet-manufacturing/ | `/woodsat-staging/speaker-cabinet-manufacturing/` | YES | YES | noindex,nofollow |
| `subwoofer-enclosure-design` | https://woodsat.com/subwoofer-enclosure-design/ | `/woodsat-staging/subwoofer-enclosure-design/` | YES | YES | noindex,nofollow |
| `thanks` | https://woodsat.com/thanks/ | `/woodsat-staging/thanks/` | YES | YES | noindex,nofollow |
| `wooden-speaker-box-manufacturer` | https://woodsat.com/wooden-speaker-box-manufacturer/ | `/woodsat-staging/wooden-speaker-box-manufacturer/` | YES | YES | noindex,nofollow |
| `wooden-speaker-cabinet-designs` | https://woodsat.com/wooden-speaker-cabinet-designs/ | `/woodsat-staging/wooden-speaker-cabinet-designs/` | YES | YES | noindex,nofollow |
| `wooden-speaker-enclosure-manufacturer` | https://woodsat.com/wooden-speaker-enclosure-manufacturer/ | `/woodsat-staging/wooden-speaker-enclosure-manufacturer/` | YES | YES | noindex,nofollow |
| `wooden-vs-mdf-speaker-cabinets` | https://woodsat.com/wooden-vs-mdf-speaker-cabinets/ | `/woodsat-staging/wooden-vs-mdf-speaker-cabinets/` | YES | YES | noindex,nofollow |

**Mapped:** 25 / 25. **Unmapped:** 0. **Ambiguous:** 0. **Duplicate keys:** 0.

## 4. Verified invariants

| Check | Result |
|---|---|
| Pages in build | 25 |
| Distinct production keys | 25 (no collisions) |
| Canonical points at production host | 25 / 25 |
| Canonical pointing at `github.io` | 0 |
| Sitemap URL count | 25 |
| Sitemap entries on a non-production host | 0 |
| Staging `meta robots` = `noindex,nofollow` | 25 / 25 (intentional, per 4.15 `_noindex_lock.json`) |

## 5. Legacy production URLs that have **no** counterpart in this mapping

While building the mapping, six additional production URLs were found to be referenced from page body copy but are **not** part of the 25-page build. They are therefore unmappable to any staging route and are recorded here as an addendum, not as mapping rows:

| Legacy production URL | Exists in Hugo build | Production behaviour (read-only probe) |
|---|---|---|
| `/custom-wooden-speaker-enclosures-manufacturer/` | NO | `301` → `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/custom-speaker-cabinet-builder/` | NO | `301` → `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/high-quality-speaker-enclosures/` | NO | `301` → `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/loudspeaker-cabinet-manufacturer/` | NO | `301` → `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/custom-speaker-and-subwoofer-cabinet-box-factory/` | NO | `301` → `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/most-durable-wood-for-speakers/` | NO | `301` → `/best-wood-for-speaker-boxes/` |

These are legacy WordPress routes that still resolve on production via 301. They matter for two reasons and are analysed in full in `internal_link_opportunities.md`:

1. If a future GSC export contains impressions for any of these six URLs, those rows **must** be folded into the redirect target before joining, or page-level metrics will be understated.
2. They are currently the destination of 28 in-body contextual links inside the Hugo build, which routes anchor equity through a redirect hop into a page that does not own the corresponding intent.

## 6. Instructions for re-joining once GSC access exists

```
1. Export Search Console → Performance → Pages (+ Queries) as CSV.
2. Normalize the `page` column with the five rules in §2.
3. Fold the six legacy URLs in §5 into their 301 targets.
4. LEFT JOIN onto gsc_url_mapping.json on the normalized production URL.
5. Any GSC page that fails to join is either (a) a legacy URL not listed in §5,
   (b) a paginated/parameter variant, or (c) a page removed since the export —
   report it, do not silently drop it.
```

## 7. Status

| Item | Value |
|---|---|
| §8 requirement (URL mapping JSON + MD) | **SATISFIED** |
| Evidence class | **DATA-BACKED** (build artefacts + read-only production probe) |
| GSC metrics in this report | none required; none fabricated |
