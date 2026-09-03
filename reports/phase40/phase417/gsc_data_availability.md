# PHASE 4.17 — GSC Data Availability

**Phase:** 4.17 — GSC Data + Search Performance Opportunity Analysis
**Baseline commit:** `366334a` (branch `main`, worktree clean at analysis time)
**Mode:** READ-ONLY (0 site modifications)

---

## VERDICT

```
GSC_DATA_AVAILABLE = false
```

**Scope of the verdict:** false **for the Woodsat property**. This is not a "we could not find a
file" conclusion — it is an **authenticated, API-level determination**.

| Field | Value |
| --- | --- |
| available | **false** |
| source | NOT_AVAILABLE (no Woodsat GSC dataset exists in this environment) |
| date range | `GSC_START_DATE` = NOT_AVAILABLE / `GSC_END_DATE` = NOT_AVAILABLE |
| rows | NOT_AVAILABLE (0 Woodsat rows obtainable) |
| dimensions | NOT_AVAILABLE |
| query dimension present | NOT_AVAILABLE |
| page dimension present | NOT_AVAILABLE |
| country / device / search appearance | NOT_AVAILABLE |
| data complete | NOT_AVAILABLE |

Consequently:

```
PHASE_4.17 = PARTIAL
```

Per §35, the phase is **not failed** for GSC unavailability. Every analysis that can be performed
without empirical search data has been completed, and every finding is explicitly labelled
`DATA-BACKED` or `STRUCTURAL / INFERRED`.

---

## 1. Discovery method (four independent passes)

### Pass 1 — filename search
Recursive search across the repository, the whole workspace, and all sibling
`D:\Workbuddy\*` session directories for:
`*gsc*`, `*search*console*`, `*searchconsole*`, `*search*performance*`, `*search*analytics*`,
`*quer*`, `*keyword*`, `*ranking*`, `*organic*`, `*impression*`, `*clicks*`,
plus every `*.csv`, `*.tsv`, `*.xlsx`, `*.xls`.

Inside `staging-build`, the **only** schema-matching hits were PHASE 4.15 derived artifacts
(`phase415_keyword_map.json`, `phase415_commercial_keyword_map.json`,
`phase415_top_commercial_keywords.json`). These are **not** GSC exports — they are the 4.15
structural keyword model, and every metric field in them is already `null` +
`"gsc_note": "GSC_NOT_AVAILABLE"`.

The only workspace `.tsv` (`reports/phase40/evidence/phase41c/phase41c_observations.tsv`) is an
HTTP redirect/status probe log, not search-performance data.

### Pass 2 — content-schema search
Searched file **contents** for GSC schema signatures (`impressions`, `average position`,
`avg. pos`, `search console`). Per §4 ("Do NOT assume a file is GSC data merely because it
contains keywords"), every hit was opened and its schema validated. All in-repo hits resolved to
4.15/4.16 report prose or the 4.15 harness scripts.

### Pass 3 — cross-session + local export locations
Found GSC-related artifacts **outside** this project (details in §2). Also checked
`Downloads`, `Desktop`, `Documents` (read-only listing).

### Pass 4 — live Google Search Console API (authoritative)
A read-only service-account credential exists in the wider workspace from unrelated prior work:

- identity: `gsc-api-reader@gsc-api-integration-506213.iam.gserviceaccount.com`
- project: `gsc-api-integration-506213`
- scope used: `https://www.googleapis.com/auth/webmasters.readonly`

**`sites.list` result — HTTP 200:**

```
accessible_property_count: 1
  - https://alumcasting.com/   | permission: siteFullUser
WOODSAT_PROPERTIES_FOUND: 0
```

**Direct `searchAnalytics.query` probe of every plausible Woodsat property form:**

| Candidate property | HTTP | API message |
| --- | --- | --- |
| `https://woodsat.com/` | **403** | User does not have sufficient permission for site |
| `https://www.woodsat.com/` | **403** | User does not have sufficient permission for site |
| `http://woodsat.com/` | **403** | User does not have sufficient permission for site |
| `sc-domain:woodsat.com` | **403** | User does not have sufficient permission for site |
| `https://blog.woodsat.com/` | **403** | User does not have sufficient permission for site |
| `https://diecasting.github.io/woodsat-staging/` | **403** | User does not have sufficient permission for site |

```
any_woodsat_property_accessible: False
```

This is conclusive: **no Woodsat Search Console data is reachable in this environment.**

---

## 2. GSC data that DOES exist — and why it was REJECTED

A genuine, schema-valid GSC export is present in the wider workspace. It was examined and
**rejected as out-of-property**.

| Attribute | Value |
| --- | --- |
| File | `D:\Workbuddy\_gsc_artifact_readonly\phase_2_11_gsc_query_page.csv` |
| Duplicate copy | `C:\Users\anson\Downloads\gsc-live-query-page.zip` (same 2 files) |
| Declared property | **`https://alumcasting.com/`** |
| Date range | 2026-05-23 → 2026-08-20 |
| Rows | 3,051 |
| Schema | `query,page,clicks,impressions,ctr,position` — **valid GSC query×page export** |
| Source | Google Search Console (live) |
| Distinct hosts inside file | `https://alumcasting.com` (3,051 / 3,051 rows) |
| Rows mentioning `woodsat` | **0** |

### Rejection rationale (binding)

`alumcasting.com` is a **different business and a different website** (aluminium die casting) from
`woodsat.com` (wooden speaker cabinets). Its queries — `adc12`, `zamak 3 vs zamak 5`,
`aluminum die casting factory` — have no relationship to Woodsat's commercial architecture.

Using it as a proxy would constitute **fabrication of Woodsat search metrics** and is prohibited
by §32. It is therefore **excluded from every downstream calculation in this phase**. It is
documented here only to prove the discovery pass was thorough and the rejection deliberate.

The related prior-session assets (`PHASE_2.9_GSC_OPPORTUNITY_INTELLIGENCE_REPORT.md`,
`_2_9_gsc_read.py`, `_3_4_gsc_read.py`, `alumcasting-serp-sniper/.env` with
`GSC_SITE_URL=https://alumcasting.com/`) all belong to the same alumcasting property and are
likewise excluded.

---

## 3. Why Woodsat has no Search Console data here — structural explanation

Two independent, verified facts explain the absence:

1. **The Hugo site under analysis is a pre-cutover staging rebuild and is deliberately
   de-indexed.** All 25 built pages carry `<meta name="robots" content="noindex,nofollow">`,
   emitted by `layouts/_default/baseof.html` under the `isStaging` flag in `hugo.toml`.
   Confirmed by 4.15's `_noindex_lock.json` (`pages_with_noindex: 26`, gate PASS).
   A `noindex,nofollow` host cannot accrue Search Console performance data — **by design**.

2. **Production `woodsat.com` is still the live WordPress site.** A read-only header probe
   returns `HTTP 200`, `Server: cloudflare`, and a WordPress REST link header
   (`<https://woodsat.com/wp-json/>; rel="https://api.w.org/"`, page id 180).
   Any real Woodsat search history therefore belongs to that **WordPress production property**,
   for which this environment holds **no GSC authorisation**.

This is a **permissions/ownership gap, not a data-existence gap**. Woodsat GSC data may well
exist in the owner's Search Console account; it is simply not reachable from here.

---

## 4. Date window

| Item | Value |
| --- | --- |
| Preferred window (per §6) | most recent continuous ~3 months |
| `GSC_START_DATE` | **NOT_AVAILABLE** |
| `GSC_END_DATE` | **NOT_AVAILABLE** |
| Datasets combined | none (§6 compliance: no incompatible datasets merged) |

For reference only, the intended window had access existed would have been
**2026-06-05 → 2026-09-02** (the trailing ~3 months to the analysis date, used solely as the
probe payload above). **No data was returned for it.**

---

## 5. What is required to make this phase `PASS`

Grant the Woodsat Search Console property read access, then re-run 4.17. Either:

- **Option A (API, preferred):** in Search Console for the Woodsat property →
  *Settings → Users and permissions → Add user* →
  `gsc-api-reader@gsc-api-integration-506213.iam.gserviceaccount.com`, permission **Full** or
  **Restricted**. The mapping table in `gsc_url_mapping.json` is already built and will accept
  live rows immediately.
- **Option B (manual export):** export **Search results → Queries + Pages** for the most recent
  full 3 months as CSV (with the `page` dimension included, not queries-only) and place it in
  the workspace.

Also confirm which property form is verified (`https://woodsat.com/` vs `sc-domain:woodsat.com`),
as that determines whether `www`/`http` variants are consolidated.

---

## 6. Impact on this phase's deliverables

| Analysis | Status |
| --- | --- |
| Query normalization (§7) | NOT_AVAILABLE — 0 rows to normalize (rules documented + ready) |
| URL normalization (§8) | **COMPLETE** — site-side mapping is DATA-BACKED, 25/25 mapped, 0 unmappable |
| Query classification (§9) | **COMPLETE** — taxonomy applied to the 4.15/4.16 target-query universe (STRUCTURAL) |
| Query→URL performance map (§11) | Structure complete; all metrics NOT_AVAILABLE |
| Position 4–10 / 11–20 / 21–30 / 31–50 (§12–15) | NOT_AVAILABLE — cannot exist without position data |
| High impression / low CTR (§16) | Empirically NOT_AVAILABLE; structural SERP-presentation risk delivered instead |
| Wrong landing page (§17) | Empirically NOT_AVAILABLE; structural intent-overlap review delivered |
| GSC cannibalization (§18) | NOT_AVAILABLE; 4.16 structural resolution restated, not re-litigated |
| Commercial page performance (§20) | Metrics NOT_AVAILABLE; site-side authority/depth table DATA-BACKED |
| Brand vs non-brand (§22) | NOT_AVAILABLE; brand-term inventory delivered |
| Device / country / appearance (§23) | NOT_AVAILABLE |
| Trend analysis (§24) | `TREND_ANALYSIS = NOT_AVAILABLE` |
| Internal link opportunities (§29) | **DATA-BACKED** from the measured contextual link graph |
| Metadata opportunities (§30) | **DATA-BACKED** from measured title/description lengths |

**No metric anywhere in this phase is estimated, modelled, or inferred from third-party tools.**
