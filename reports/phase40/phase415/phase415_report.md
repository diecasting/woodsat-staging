# PHASE 4.15 — SEO Growth Opportunity Audit

**Status:** PHASE_4.15 = SEO_GROWTH_OPPORTUNITY_AUDIT_PARTIAL
**Generated:** 2026-09-03 11:41 UTC
**Site:** https://diecasting.github.io/woodsat-staging/ (canonical/OG pinned to production https://woodsat.com)
**Mode:** READ-ONLY. No content/layout/CSS/config/Title/Meta/H1/Schema/route/form changes were made.

## GSC Data Availability
- `GSC_DATA_AVAILABLE = false`
- No GSC export, no keyword/ranking CSV, no prior SEO dataset exists anywhere in the workspace.
- **Per the GSC DATA FAILURE RULE, the final state is PARTIAL**: ranking / CTR / impression opportunity sorting (Parts 7-9, 11, 26-28) cannot be done empirically. All non-empirical audits (technical, content-intent, commercial mapping, cannibalization, content gap, metadata, internal-link) are fully completed using verifiable on-page + internal-link evidence.
- **No fabrication**: every `clicks / impressions / ctr / position` field is set to `GSC_NOT_AVAILABLE`.

## Site Inventory (Part 1)
- Pages audited: **25** (from sitemap.xml + built HTML).
- Breakdown: about=1, commercial=9, contact=1, editorial=11, home=1, resource=1, system_thanks=1

## Part 47 — Answers to the 10 Required Questions

### 1. Top 10 keywords with most uplift potential
> Without GSC positions this is qualitative. The highest-leverage targets are the cannibalized 'wooden speaker cabinet/box/enclosure manufacturer' cluster and the highest commercial-value phrases:
`wooden speaker box manufacturer` (opp_score 78.7), `wooden speaker enclosure manufacturer` (opp_score 78.4), `wooden speaker cabinet manufacturer` (opp_score 78.2), `mdf vs baltic birch plywood speaker cabinets` (opp_score 77.9), `speaker cabinet cnc machining service` (opp_score 72.0), `custom cnc wood routing services` (opp_score 69.5)

### 2. Position 11-20 keywords to prioritise
> **CANNOT be answered empirically (no GSC).** The closest evidence-based proxy: phrases in the STRONG/LIKELY cannibalization clusters are the ones most likely stuck mid-pack because authority is split. See cannibalization report.

### 3. High-impression + low-CTR keywords
> **CANNOT be answered (no GSC impressions/CTR).** This is the single biggest gap that connecting GSC would close.

### 4. Keyword Cannibalization — YES
- **5 clusters identified.** Severity:
  - **STRONG** — `wooden speaker cabinet / box / enclosure manufacturer` across pages: custom-wooden-speaker-cabinet-manufacturer, oem-wooden-speaker-cabinet-manufacturer, hifi-speaker-cabinet-manufacturer, wooden-speaker-enclosure-manufacturer, wooden-speaker-box-manufacturer, custom-empty-wooden-speaker-cabinet-boxes-manufacturer. Likely primary: `custom-wooden-speaker-cabinet-manufacturer (broadest, most modifier-inclusive H1)`.
  - **LIKELY** — `CNC wood routing / machining for speaker cabinets` across pages: custom-cnc-wood-routing-services, speaker-cabinet-cnc-machining-service. Likely primary: `speaker-cabinet-cnc-machining-service (commercial, conversion-oriented)`.
  - **LIKELY** — `MDF vs wood / Baltic birch for speaker cabinets` across pages: wooden-vs-mdf-speaker-cabinets, mdf-vs-baltic-birch-plywood-speaker-cabinets. Likely primary: `wooden-vs-mdf-speaker-cabinets (clearer informational intent)`.
  - **POSSIBLE** — `best wood / materials for speaker boxes` across pages: best-wood-for-speaker-boxes, speaker-box-materials, acoustic-wood-speaker-enclosures. Likely primary: `best-wood-for-speaker-boxes (highest commercial-adjacent intent)`.
  - **POSSIBLE** — `speaker box finishing / veneering / lacquer` across pages: speaker-box-finishes, speaker-box-veneering, high-gloss-piano-lacquer-finishing-process-wood-speakers. Likely primary: `high-gloss-piano-lacquer-finishing-process-wood-speakers (commercial)`.
  - The STRONG cluster (6 'cabinet/box/enclosure manufacturer' pages) is the top priority.

### 5. Commercial pages with ranking potential but weak authority
- `mdf-vs-baltic-birch-plywood-speaker-cabinets`: **0 inbound internal links** (orphaned).
- `wooden-vs-mdf-speaker-cabinets`: only **2 inbound** (very weak).
- Several commercial pages link to only **1 editorial** (thin topical support). See internal-link opportunities.

### 6. Editorial pages that can further support Commercial
- High-value but weakly-linked editorials: `best-wood-for-speaker-boxes`, `acoustic-wood-speaker-enclosures`, `wooden-speaker-cabinet-designs`, `speaker-box-veneering`, `speaker-box-materials`, `subwoofer-enclosure-design` (inbound 6-12).
- Strengthening commercial->editorial links from the 9 commercial pages would build their authority.

### 7. Pages where ranking page ≠ search intent
- `mdf-vs-baltic-birch-plywood-speaker-cabinets`: commercial-classified but H1 is an informational 'deep dive' comparison (intent ambiguity vs `wooden-vs-mdf-speaker-cabinets`).
- `thanks` page: title is a manufacturer keyword but the page is a thank-you (title/content mismatch).

### 8. Titles / Meta most worth changing next phase
- **[P1]** `thanks`: Title 'Sub-woofer Wooden Box manufacturer' does NOT match page content (a thank-you page, H1 empty). Misleading for users and SERPs.
- **[P2]** `about-us`: Title 'Custom Woodworking Manufacturer | Precision Craftsmanship' is generic: omits the core term 'speaker cabinet' and the brand 'Woodsat'.
- **[P3]** `multiple commercial`: Six manufacturer pages share near-duplicate title suffix templates, reducing differentiation of the unique modifier (custom/oem/hifi/empty/box/enclosure).
- **[P2]** `mdf-vs-baltic-birch-plywood-speaker-cabinets`: Page is commercial-classified but its H1 is an informational 'deep dive' comparison; title/template vs content intent is ambiguous.
- **[P3]** `site-wide`: No missing meta descriptions detected. Some commercial meta descriptions may be templated; recommend a light uniqueness pass.

### 9. Genuinely worth-adding Content Gaps
- 6 inferred gaps (no GSC volume, inferred from topic coverage):
  - **[P2]** Bookshelf / studio monitor speaker cabinet manufacturer — existing support: acoustic-wood-speaker-enclosures, custom-wooden-speaker-cabinet-manufacturer.
  - **[P2]** Floorstanding speaker cabinet manufacturer — existing support: custom-wooden-speaker-cabinet-manufacturer.
  - **[P2]** Subwoofer enclosure manufacturer (commercial) — existing support: subwoofer-enclosure-design.
  - **[P2]** Speaker cabinet prototyping / low-volume / rapid prototype service — existing support: contact, speaker-cabinet-cnc-machining-service.
  - **[P3]** Speaker cabinet damping / bracing / isolation engineering — existing support: speaker-box-materials, wooden-speaker-cabinet-designs.
  - **[P3]** Powered / active wooden speaker cabinet OEM — existing support: wooden-speaker-enclosure-manufacturer.

### 10. If next phase could do only 10 SEO modifications
See the **Executive Decision Matrix** below (ranked, with evidence / expected impact / risk / next action).

## PHASE_4.15_EXECUTIVE_DECISION_MATRIX

| Rank | Opportunity | Page | Evidence | Expected Impact | Risk | Next Action |
| ---- | ----------- | ---- | -------- | --------------- | ---- | ----------- |
| 1 | Designate ONE primary 'wooden speaker cabinet manufacturer' page; differentiate … | custom-wooden-speaker-cabinet-manufacturer (primary) + 5 siblings | STRONG cannibalization cluster: 6 pages target near-identical head ter… | High (consolidates split authority, likely the single biggest organic win) | Low | PHASE 4.16: assign primary, rewrite H1/title per modifier, add cross-links |
| 2 | Fix thanks-page <title> (currently 'Sub-woofer Wooden Box manufacturer') to a th… | thanks | Title/content mismatch; H1 empty. Pre-existing anomaly (noted 4.14).… | Low-Medium (correctness/UX; minor SEO hygiene) | Low | PHASE 4.16: rewrite title only |
| 3 | Add inbound internal links to the orphaned deep-dive page (0 inbound today)… | mdf-vs-baltic-birch-plywood-speaker-cabinets | inbound_internal_links = 0 (4.14 link graph).… | Medium (rescues an orphaned high-quality asset) | Low | PHASE 4.16: link from commercial cabinet pages + wooden-vs-mdf |
| 4 | Consolidate the CNC cluster: make commercial page primary, editorial post links … | speaker-cabinet-cnc-machining-service (primary) + custom-cnc-wood-routing-services | LIKELY cannibalization: editorial + commercial cover same CNC capabili… | Medium | Low | PHASE 4.16: rewrite editorial as deep guide -> commercial |
| 5 | Reframe mdf-vs-baltic-birch page as a commercial materials-specification page (r… | mdf-vs-baltic-birch-plywood-speaker-cabinets | LIKELY cannibalization with wooden-vs-mdf; title/content intent ambigu… | Medium | Low | PHASE 4.16: convert to 'materials we stock & why' commercial angle |
| 6 | Strengthen commercial->editorial pathways (most commercial pages link to only 1 … | all 9 commercial pages | commercial_to_editorial shows <=1 editorial linked on several pages.… | Medium (topical authority) | Low | PHASE 4.16: add 1-2 relevant editorial links per commercial page |
| 7 | Improve about-us <title> to include 'speaker cabinet' + Woodsat brand… | about-us | Title 'Custom Woodworking Manufacturer | Precision Craftsmanship' is g… | Low-Medium (brand/clarity) | Low | PHASE 4.16: brand + core-term in title |
| 8 | Light uniqueness pass on templated commercial title suffixes… | 6 manufacturer pages | Near-duplicate '| Custom Audio Enclosure Factory' / '| OEM Audio Enclo… | Low | Low | PHASE 4.16: per-page distinct modifier + benefit |
| 9 | Build a commercial 'bookshelf / studio monitor speaker cabinet manufacturer' pag… | (new) | INFERRED gap: standard OEM offering with no dedicated page; only edito… | Medium | Medium | PHASE 4.16: create commercial page + link from editorials |
| 10 | Build a commercial 'subwoofer enclosure manufacturer' page (content gap)… | (new) | INFERRED gap: only an editorial design guide exists; no commercial man… | Medium | Medium | PHASE 4.16: create commercial page + link from subwoofer design guide |

## Lock / Regression Verification (Part 29-33)
- SEO regression: **PASS** (title diffs = 0; READ-ONLY, 0 changes)
- Route regression: **PASS** (bare=0, dbl=0, hardcoded-prod-internal=0)
- Noindex lock: **PASS** — staging remains noindex,nofollow (26/26 pages)
- Schema regression: **PASS** (JSON-LD @graph/Organization/WebPage/Breadcrumb present)
- Form regression: **PASS** (Formspree endpoint + POST + your-name/your-email/your-message intact)

## SEO Scorecard (Part 43)
- indexability=OK; technical_seo=OK; commercial_keyword_coverage=WEAK; content_coverage=OK; internal_link_authority=OK; CTR_opportunity=GSC_NOT_AVAILABLE; ranking_opportunity=GSC_NOT_AVAILABLE; cannibalization_risk=HIGH; metadata_quality=WEAK

## Deliverables (20 files + executive matrix)
- Site inventory, data-source report, keyword map, commercial keyword map, quick wins, top20 opportunities,
  top commercial keywords, top commercial pages, cannibalization, content gap, metadata opportunities,
  internal-link opportunities, SEO scorecard, execution roadmap, 4 regression/lock checks, this report,
  manifest.json, and executive_decision_matrix.json.

## Next Step to Escalate to PASS
> Connect Google Search Console (or supply a 3-month export CSV). Re-run this audit to enable empirical
> position / CTR / impression opportunity sorting (Parts 7-9, 11, 26-28) — the only missing piece.