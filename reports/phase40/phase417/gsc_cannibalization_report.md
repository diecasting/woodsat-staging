# PHASE 4.17 — Cannibalization Analysis from GSC

**GSC_DATA_AVAILABLE:** `false`
**GSC-confirmed cannibalization:** `NOT_AVAILABLE`
**Structural cannibalization state:** **DATA-BACKED — 0 unresolved conflicts**

---

## 1. Result

§18 asks for cannibalization confirmed by GSC — that is, one query whose impressions are split across two or more URLs, with the ranking URL alternating between them. That test requires the `query × page` dimension pair from Search Console and is `NOT_AVAILABLE`.

The complementary structural test — do two pages target the same query with overlapping title, H1 and intent? — does not require GSC. It was run against all 25 pages and all 46 target queries.

## 2. Structural cannibalization state after 4.16 (data-backed)

From `query_url_performance_map.csv`, column `cannibalization_risk_structural`:

| State | Rows | Meaning |
|---|---|---|
| `RESOLVED_STRUCTURALLY_4.16` | 15 | previously contested; 4.16 assigned a single owner |
| `LOW` | 27 | single unambiguous owner from the outset |
| `N/A` | 4 | brand / navigational — cannibalization not applicable |
| `HIGH` or `MEDIUM` | **0** | — |
| **Total** | **46** | |

**No query in the universe has two competing claimant pages.** Verified by three independent checks:

1. **Title uniqueness** — 25 distinct `<title>` values across 25 pages; 0 duplicates.
2. **H1 uniqueness** — every page has exactly 1 `<h1>`; 0 pages with 0 or 2+; 0 duplicate H1 strings among the 7 commercial pages.
3. **Owner uniqueness** — every one of the 46 queries maps to exactly one `intended_owner_slug_phase416`.

## 3. The 4.16 sibling split held

The pre-4.16 risk was seven pages all reading as "wooden speaker cabinet manufacturer". 4.16 differentiated them by segment, and the differentiation is present in the built HTML:

| Page | Segment claimed | Distinct owned queries |
|---|---|---|
| `custom-wooden-speaker-cabinet-manufacturer` | primary hub — custom / supplier / factory | 6 |
| `oem-wooden-speaker-cabinet-manufacturer` | OEM / ODM programmes | 4 |
| `hifi-speaker-cabinet-manufacturer` | audiophile / hi-fi | 3 |
| `wooden-speaker-enclosure-manufacturer` | enclosure terminology | 2 |
| `wooden-speaker-box-manufacturer` | box terminology | 3 |
| `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | empty / blank boxes | 3 |
| `speaker-cabinet-cnc-machining-service` | CNC machining service | 3 |

Each owns a disjoint query set. On-page signals do not contest each other.

## 4. However — a *link-level* cannibalization vector is active

Structural title/H1/intent separation is clean, but **anchor text is not aligned with it.** As documented in `wrong_landing_page_analysis.md`, 25 contextual links carrying primary-hub, hifi, enclosure and CNC anchor text 301-redirect into the empty-box sibling. Effective internal support becomes:

- `custom-empty-wooden-speaker-cabinet-boxes-manufacturer`: **36** contextual inbound
- `custom-wooden-speaker-cabinet-manufacturer` (primary hub): **8**
- `hifi-speaker-cabinet-manufacturer`: **4**

Anchor text is one of the strongest relevance signals a site controls. Feeding "custom wooden speaker enclosures manufacturer" and "luxury speaker cabinets" anchors into the empty-box page teaches search engines that this page is the site's answer for primary and audiophile intent — competing directly with the pages 4.16 assigned to those intents.

So the accurate statement is:

> **On-page cannibalization: resolved (0 conflicts).**
> **Anchor-text cannibalization: active, affecting 25 links, undetected before this phase.**

This does not contradict 4.16 — 4.16's changes are intact and verified. It identifies a legacy vector 4.16 did not cover, on evidence 4.16 did not have.

## 5. What GSC would add

| Question | Answerable now? |
|---|---|
| Do two URLs actually split impressions on one query? | NO — needs GSC |
| Does the ranking URL alternate over time? | NO — needs GSC + trend |
| Is the empty-box page ranking for primary-hub queries? | NO — needs GSC (**the decisive test for §4**) |
| Do two pages target the same query on-page? | YES — answered: no |
| Is anchor text misaligned with the ownership model? | YES — answered: 25 links misaligned |

The third row is the specific empirical test that would confirm or refute §4. It is the single highest-value query to run once access exists.

## 6. Recommendations

| ID | Priority | Recommendation |
|---|---|---|
| CAN-1 | **P0** | Re-align the 25 misrouted anchors to their 4.16 owners (same action as WLP-1). This is anchor-text cannibalization remediation, not a link-count exercise. |
| CAN-2 | **P1** | Once GSC access exists, run `query × page` for the 6 primary-hub queries and check whether the empty-box URL appears. If it does, this report's structural inference is confirmed empirically. |
| CAN-3 | **P2** | Keep the 4.16 sibling architecture unchanged. Nothing found here justifies revisiting it; the evidence points at legacy links, not at the page model. |

## 7. Status

| Item | Value |
|---|---|
| §18 GSC requirement | **NOT_AVAILABLE** |
| Structural cannibalization conflicts | **0** |
| Anchor-text cannibalization instances | **25 (DATA-BACKED)** |
| 4.16 architecture contradicted? | **NO** — extended, not contradicted |
