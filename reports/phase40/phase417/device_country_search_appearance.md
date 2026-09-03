# PHASE 4.17 — Device, Country & Search Appearance Analysis

**GSC_DATA_AVAILABLE:** `false`
**Status:** `NOT_AVAILABLE` — **fully blocked, no structural substitute exists**

---

## 1. Result

Section 23 requires three GSC dimension breakdowns:

| Dimension | Status | Substitutable offline? |
|---|---|---|
| Device (desktop / mobile / tablet) | `NOT_AVAILABLE` | **NO** |
| Country | `NOT_AVAILABLE` | **NO** |
| Search Appearance (rich results, etc.) | `NOT_AVAILABLE` | **NO** — partially, see §3 |

This is the one section of PHASE 4.17 with essentially **no offline substitute**. Device split, country split and search-appearance classification are Google-side observations. They cannot be derived, approximated or inferred from the codebase, from the rendered HTML, or from anything else available to this phase. No numbers appear in this report.

## 2. Why no substitute exists

- **Device** — the site is responsive and serves identical HTML to all devices. Nothing in the build indicates how visitors actually arrive.
- **Country** — the site has no hreflang, no locale variants and no geo-targeting configuration. It is a single-locale English site. There is no signal to inspect that would even hint at the observed country mix.
- **Search Appearance** — this is Google's own classification of *how* results were shown (rich result, FAQ, sitelink, etc.). Only Google reports it.

Stating any device or country figure here would be pure invention, which §32 prohibits.

## 3. Rich-result *eligibility* substrate (data-backed, NOT appearance data)

One narrow, honest thing can be reported: whether the markup that makes rich appearances *possible* is present. This is eligibility, not appearance, and the two must not be conflated — eligible markup frequently produces no rich result at all.

| Check | Result |
|---|---|
| Pages with ≥1 JSON-LD block | **25 / 25** |
| Pages with 0 JSON-LD | 0 |
| Pages with exactly 1 `<h1>` | 25 / 25 |
| Pages with a contact form (Formspree) | 22 / 25 |
| Formspree endpoint consistency | 22 / 22 identical (`xdaqjegz`) |
| Canonical pointing to production host | 25 / 25 |
| Sitemap entries | 25 |

Structured-data coverage is complete and uniform. If rich results are not appearing in production, the cause is not missing markup on these pages.

**No claim is made about which appearance types Google actually serves.**

## 4. Mobile-readiness note (build-side only)

The staging build ships a single responsive stylesheet and no device-conditional rendering. That means device performance differences, if any, would arise from layout behaviour rather than from divergent markup. This is a statement about the build, not about observed device traffic.

## 5. Analysis that will run once access is granted

```
DEVICE:
  export dimension=device × page  -> compare CTR and position desktop vs mobile
  flag any commercial page where mobile position lags desktop by >3
COUNTRY:
  export dimension=country -> rank by impressions
  business relevance test: are impressions arriving from the target
  OEM procurement markets (US / DE / UK / AU / CA) or elsewhere?
  IF a large non-target country share appears -> re-check keyword intent match
SEARCH APPEARANCE:
  export dimension=searchAppearance
  compare against the 25/25 JSON-LD coverage recorded in §3:
  full markup coverage + zero rich appearances => markup is valid but
  not being trusted or not eligible for the query types -> investigate type choice
```

The country breakdown is the highest-value of the three for this business: a contract manufacturer's entire commercial case depends on whether impressions come from procurement markets or from irrelevant regions. That test is currently impossible.

## 6. Status

| Item | Value |
|---|---|
| §23 device requirement | **NOT_AVAILABLE** |
| §23 country requirement | **NOT_AVAILABLE** |
| §23 search appearance requirement | **NOT_AVAILABLE** |
| Rich-result eligibility substrate | **DATA-BACKED — 25/25 pages carry JSON-LD** |
| Fabricated metrics | 0 |
| Offline substitute possible | **NO** — the only fully blocked section of this phase |
