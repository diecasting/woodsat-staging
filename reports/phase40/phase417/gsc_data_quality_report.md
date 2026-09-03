# PHASE 4.17 — GSC Data Quality Report

**Baseline:** `366334a` · **Mode:** READ-ONLY · `GSC_DATA_AVAILABLE = false`

---

## 1. Headline

There is **no Woodsat GSC dataset to validate**. Every §31 quality gate is therefore reported as
`NOT_AVAILABLE (no rows)` rather than `PASS`, because claiming `PASS` on an empty dataset would
misrepresent the evidence base.

The quality checks were nevertheless **executed against the one GSC dataset present in the
environment** (the alumcasting export) in order to (a) prove the validator works and (b) document
precisely why that dataset is inadmissible for Woodsat.

---

## 2. §31 quality gates — Woodsat dataset

| # | Check | Result | Note |
| --- | --- | --- | --- |
| 1 | No duplicate rows | `NOT_AVAILABLE` | 0 rows |
| 2 | Valid numeric values | `NOT_AVAILABLE` | 0 rows |
| 3 | CTR range valid (0–1) | `NOT_AVAILABLE` | 0 rows |
| 4 | Position values valid (>= 1) | `NOT_AVAILABLE` | 0 rows |
| 5 | URLs normalized | **PASS (site-side)** | 25/25 site URLs normalized + mapped; see `gsc_url_mapping.json` |
| 6 | Dates valid | `NOT_AVAILABLE` | no date-dimension rows |
| 7 | Query strings not empty | `NOT_AVAILABLE` | 0 rows |
| 8 | `clicks <= impressions` | `NOT_AVAILABLE` | 0 rows |
| 9 | No aggregation double-counting | **PASS (by construction)** | no aggregation performed; nothing to double-count |
| 10 | No staging URL treated as separate production URL | **PASS** | `/woodsat-staging/<slug>/` explicitly aliased to `https://woodsat.com/<slug>/`; 1:1, 0 collisions |

---

## 3. Validation of the rejected (out-of-property) dataset

Executed to demonstrate validator correctness. **These numbers describe `alumcasting.com`, not
Woodsat, and are excluded from every Woodsat analysis in this phase.**

| Attribute | Finding |
| --- | --- |
| File | `D:\Workbuddy\_gsc_artifact_readonly\phase_2_11_gsc_query_page.csv` |
| Header | `query,page,clicks,impressions,ctr,position` |
| Schema verdict | **VALID** GSC query×page export shape |
| Declared property (sidecar `.meta.json`) | `https://alumcasting.com/` |
| Declared range | 2026-05-23 → 2026-08-20 (89 days, ~3 months — would have satisfied §6) |
| Declared rows | 3,051 · file lines 3,052 (1 header) → **row count consistent** |
| Distinct hosts in `page` column | 1 (`https://alumcasting.com`) |
| Rows referencing any Woodsat host | **0** |
| Dimensions present | `query`, `page` |
| Dimensions absent | `date`, `country`, `device`, `search appearance` |

### Admissibility decision

| Gate | Result |
| --- | --- |
| Schema valid | PASS |
| Property matches Woodsat | **FAIL** |
| Any Woodsat rows | **FAIL (0)** |
| **Admissible as Woodsat data** | **NO — REJECTED** |

Rejection is mandated by §32. Substituting another property's metrics for Woodsat's would be
fabrication. Note also its dimension set (`query`,`page` only) means it could not have satisfied
§23 (device/country/appearance) or §24 (trend) even if the property had matched.

---

## 4. Live-API integrity checks

| Check | Result |
| --- | --- |
| Credential loads and parses | PASS (`type: service_account`) |
| OAuth token acquisition | PASS (`token_acquired: True`) |
| `sites.list` transport | PASS (HTTP 200) |
| Accessible properties | 1 (`https://alumcasting.com/`, `siteFullUser`) |
| Woodsat properties accessible | **0** |
| Woodsat probes (6 property forms) | all **HTTP 403 — insufficient permission** |
| Silent-failure risk | **none** — 403 is an explicit authorisation denial, not an empty-result ambiguity |

This distinction matters: an empty `200` response could mean "property exists but has no data",
which might tempt an "assume zero traffic" reading. A `403` proves the query was **never
authorised**, so **no inference about Woodsat traffic volume is permissible** — including the
inference that it is zero.

---

## 5. Site-side data quality (the substrate actually used)

Measured from the current build at `366334a` — this **is** DATA-BACKED.

| Check | Result |
| --- | --- |
| Pages parsed from `public/` | 25 |
| Sitemap `<loc>` entries | 25 |
| Sitemap hosts | 1 — `https://woodsat.com` (production-pinned) |
| Pages with exactly one `<h1>` | 25/25 |
| Pages with a canonical | 25/25, all `https://woodsat.com/...`, 0 `github.io` |
| JSON-LD blocks | 25 |
| Pages with contact form | 22, all → `https://formspree.io/f/xdaqjegz` |
| URL collisions after normalization | 0 |
| Unmappable URLs | 0 |

### Two data-integrity observations (recorded, not actioned)

1. **`thanks` is `noindex,nofollow` yet appears in `sitemap.xml`**
   (`<loc>https://woodsat.com/thanks/</loc>`). A sitemap should generally list only indexable
   URLs. Low severity, pre-existing, and **out of scope for this READ-ONLY phase** — logged for a
   future phase. (Note: on staging *every* page is `noindex` by design, so this only becomes a
   live issue after production cutover.)

2. **`reports/phase40/phase416/commercial_page_inventory.json` misstates sibling `yoast_title`
   values.** It records e.g. `"Hi-Fi Speaker Cabinet Manufacturer | Woodsat"`, but the actual
   front matter is `"Hi-Fi Speaker Cabinet Manufacturer | Premium Wooden Speaker Enclosures"`
   (likewise OEM and CNC). PHASE 4.16's `metadata_changes.md` is **correct** — it states sibling
   metadata was *not* changed — so this is a **reporting inaccuracy in one 4.16 JSON, not a site
   defect**. The site itself is intact. Recorded per §3 (do not contradict 4.16 without evidence);
   here the evidence is the front matter and the built `<title>` tags, which agree with each other.

---

## 6. Conclusion

- Woodsat GSC dataset: **absent and unreachable** → all metric gates `NOT_AVAILABLE`.
- The one available GSC dataset is **schema-valid but wrong-property** → formally **REJECTED**.
- Site-side substrate: **clean and fully validated** → structural analysis proceeds on solid ground.
- **Zero fabricated values** appear anywhere in PHASE 4.17.
