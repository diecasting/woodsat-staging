# PHASE 4.17 — Brand vs Non-Brand Analysis

**GSC_DATA_AVAILABLE:** `false`
**Brand / non-brand traffic split:** `NOT_AVAILABLE`
**Brand / non-brand target-universe split:** **DATA-BACKED**

---

## 1. Result

§22 asks how search demand divides between brand and non-brand queries. The *traffic* split requires Search Console and is `NOT_AVAILABLE`. The *targeting* split — how the site's own keyword architecture is weighted — is fully measurable and is reported below.

These answer different questions and must not be confused:

- **Traffic split** = what the market currently sends. Diagnostic of dependency and reach. Blocked.
- **Targeting split** = what the site is built to capture. Diagnostic of strategic intent. Available.

## 2. Brand classification rule applied

A query is BRAND if it contains the token `woodsat` (case-insensitive), alone or in combination. Everything else is non-brand. `contact woodsat` is classified NAVIGATIONAL rather than BRAND because its intent is a site destination, not brand discovery — it is counted as brand-adjacent in the aggregate below and the effect of either treatment is stated.

## 3. Target universe split (data-backed, 46 queries)

| Group | Classes included | Queries | Share |
|---|---|---|---|
| **Brand** | BRAND | 3 | 6.5% |
| Brand-adjacent | NAVIGATIONAL (`contact woodsat`) | 1 | 2.2% |
| **Non-brand** | COMMERCIAL, OEM_ODM, SERVICE, PRODUCT_APPLICATION, MATERIALS, INFORMATIONAL | 42 | 91.3% |
| **Total** | | 46 | 100% |

Treating `contact woodsat` as brand: brand = 4 / 46 = **8.7%**, non-brand = **91.3%**.

Non-brand breakdown:

| Class | Queries | Share of non-brand | Funnel stage |
|---|---|---|---|
| COMMERCIAL | 11 | 26.2% | money |
| INFORMATIONAL | 11 | 26.2% | research |
| PRODUCT_APPLICATION | 9 | 21.4% | consideration |
| OEM_ODM | 4 | 9.5% | money (high value) |
| SERVICE | 4 | 9.5% | money |
| MATERIALS | 3 | 7.1% | research |
| **Total non-brand** | **42** | **100%** | |

Commercial-intent non-brand (COMMERCIAL + OEM_ODM + SERVICE + PRODUCT_APPLICATION) = 28 / 42 = **66.7%** of non-brand, **60.9%** of the whole universe.

## 4. Brand-side structural support (data-backed)

| Brand query | Intended owner | Owner words | Contextual inbound |
|---|---|---|---|
| `woodsat` | `(home)` | 1130 | **0** |
| `woodsat speaker cabinet` | `(home)` | 1130 | **0** |
| `woodsat manufacturer` | `about-us` | 772 | 2 |
| `contact woodsat` (nav) | `contact` | 371 | 6 |

**Finding B1 — the home page has zero contextual inbound links.** Every page links to it through global navigation (chrome), but no page links to it from body copy. For brand queries this is low-risk: brand searches resolve to the home page on external signals, not internal ones. It is noted for completeness rather than flagged as a defect.

**Finding B2 — `about-us` carries brand-authority intent on 2 contextual inbound links and 772 words.** It is the thinnest non-utility page in the trust layer, and it is the page a "who is this supplier" query resolves to. For a B2B manufacturer where supplier credibility is a purchase gate, 772 words with 2 internal links is light. It also contains one of the 28 misrouted legacy links (anchor "custom wooden speaker enclosures manufacturer" → 301 → empty-box page), so its single outbound commercial signal points at the wrong sibling.

## 5. Strategic reading

The architecture is deliberately and heavily non-brand weighted (91.3%), which is the correct posture for a contract manufacturer with low brand recognition seeking new OEM enquiries. Two observations follow:

1. **Brand dependency risk is architecturally low but empirically unknown.** A site can target 91% non-brand and still receive 90% brand traffic. Only GSC can distinguish these, and this is the single most valuable diagnostic the missing data would provide — it determines whether the whole 4.16 commercial build is reaching the market at all.
2. **If brand traffic turns out to dominate, the remedy is already identified.** It would be the authority-inversion defect in `wrong_landing_page_analysis.md`: 25 non-brand commercial anchors misrouted to a narrow sibling, starving the primary hub and the audiophile page. That would explain non-brand under-reach without requiring any change to the 4.16 architecture.

## 6. What remains blocked

Brand vs non-brand clicks and impressions; brand CTR vs non-brand CTR; brand dependency ratio; whether non-brand commercial queries generate any impressions at all; brand query growth trend. Not estimated.

## 7. Status

| Item | Value |
|---|---|
| §22 GSC requirement | **NOT_AVAILABLE** |
| §22 targeting-split requirement | **DATA-BACKED** |
| Brand share of target universe | 6.5% (8.7% including navigational) |
| Non-brand share | 91.3% |
| Commercial-intent share of universe | 60.9% |
