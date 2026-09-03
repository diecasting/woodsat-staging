# PHASE 4.17 — Top 20 Search Opportunities

**GSC_DATA_AVAILABLE:** `false`
**Machine-readable twin:** `top_20_search_opportunities.json`
**Ranking basis:** **STRUCTURAL ONLY.** No clicks, impressions, CTR or position enter any score. This is not a ranking prediction and not a traffic forecast.

---

## 1. How to read this list

§26 asks for the top 20 search opportunities ranked by opportunity score, where that score is normally built from impressions x CTR gap x position proximity. **None of those inputs exists.** Producing a list with GSC-shaped scores would be fabrication.

Instead this list ranks opportunities by *measured structural deficit* — defects and gaps in the site that are known to suppress search performance and that were verified directly in the build. The value of each item is therefore stated as **what is provably wrong**, not as **how much traffic it would gain**.

Two score families are used and are never mixed:

- **Site-wide opportunities (OPP-1…OPP-6)** — defects spanning many pages, ranked by severity and instance count.
- **Page-level opportunities (P-01…P-14)** — per-page structural priority, scored as `commercial_role_weight(35) + authority_deficit(25) + serp_presentation_risk(25) + content_depth_headroom(15)`.

## 2. The Top 20

| # | ID | Opportunity | Severity | Evidence | Needs GSC to act? |
|---|---|---|---|---|---|
| 1 | OPP-1 | **25 contextual links carrying primary-hub / hifi / enclosure / CNC anchor text 301-redirect into the empty-box sibling.** Effective inbound: empty-box **36** vs primary hub **8** (4.5x inversion). | **P0** | 28 instances audited, 10 source pages | NO |
| 2 | OPP-2 | **Six legacy production URLs referenced from body copy have no page in the Hugo build.** They resolve today only because production WordPress 301s them. After a Hugo cutover they become 404s unless every redirect is carried across. | **P0** | 28 link instances; 6 URLs probed | NO |
| 3 | P-01 | `hifi-speaker-cabinet-manufacturer` — highest-margin segment, **lowest contextual inbound of any commercial page (4)**, title truncated at 70 chars. Structural score **72.0**. | **P1** | link graph + `<head>` audit | NO |
| 4 | P-02 | `oem-wooden-speaker-cabinet-manufacturer` — owns 4 high-value OEM/ODM queries; title **72 chars**, clipping `| Custom Audio Enclosure Factory`. Score **68.2**. | **P1** | `<head>` audit | NO |
| 5 | P-03 | `speaker-cabinet-cnc-machining-service` — title **71 chars**, clipping `| Precision Wood CNC Manufacturer`. Score **65.4**. | **P1** | `<head>` audit | NO |
| 6 | OPP-3 | Three commercial titles over the ~65-char SERP budget; in every case the clipped tail is the 4.16 differentiator. | **P1** | 25/25 pages measured | NO |
| 7 | OPP-4 | **17 of 25 meta descriptions exceed ~160 chars, including all 7 commercial pages.** Worst: `mdf-vs-baltic-birch-plywood-speaker-cabinets` at **336**. | **P1** | 25/25 pages measured | NO |
| 8 | P-04 | `custom-wooden-speaker-cabinet-manufacturer` — the designated **primary hub is out-linked 4.5:1 by its own sibling** (root cause OPP-1/ILO-1). Score **57.9**. | **P1** | link graph | NO |
| 9 | OPP-5 | **Five anchors promise a "3D Cabinet Builder" / "Custom Speaker Cabinet Builder Tool" / "3D veneer visualizer" that exists nowhere on the site.** Users are sent to an empty-box product page instead. | **P1** | 5 instances audited | NO |
| 10 | P-05 | `high-gloss-piano-lacquer-finishing-process-wood-speakers` — **lowest contextual inbound of any content page (1)** despite 1141 words of specialised finishing content. Near-orphan (see ILO-7). | **P2** | link graph | NO |
| 11 | P-06 | `wooden-vs-mdf-speaker-cabinets` — **2 contextual inbound**, second-lowest in the site. | **P2** | link graph | NO |
| 12 | OPP-6 | **Content gap: `bookshelf speaker cabinet` has no owner page**, although the topic already appears in a production asset name. | **P2** | 46-query universe + asset audit | NO |
| 13 | P-07 | `wooden-speaker-enclosure-manufacturer` — description **209 chars**; moderate support (6). Score **53.3**. | **P2** | `<head>` + link graph | NO |
| 14 | P-08 | `wooden-speaker-box-manufacturer` — description **195 chars**; moderate support (6). Score **52.8**. | **P2** | `<head>` + link graph | NO |
| 15 | P-09 | `custom-cnc-wood-routing-services` — **thinnest page owning a SERVICE query (619 words)** yet one of the best linked (11). Depth/support asymmetry. | **P2** | body + link graph | NO |
| 16 | P-10 | `speaker-cabinet-manufacturing` — **675 words** on a broad head topic, well linked (9). Depth deficit. | **P2** | body + link graph | NO |
| 17 | P-11 | Informational -> commercial handoff is largely misrouted: only **3 of ~11** info pages contain a working contextual link to the correct commercial owner; the rest attempt it through the legacy 301 URLs (see ILO-7). | **P2** | link graph | NO |
| 18 | P-12 | `about-us` — carries supplier-credibility intent on **772 words and 2 inbound links**; its one commercial outbound link is misrouted (OPP-1). | **P3** | body + link graph | NO |
| 19 | P-13 | `thanks` — `noindex,nofollow` yet present in `sitemap.xml`; also a 19-char title. Contradictory indexing signal, low impact. | **P3** | sitemap + `<head>` | NO |
| 20 | P-14 | `(home)` — **zero contextual inbound links** (navigation-only). Low risk for brand queries; recorded for completeness. | **P3** | link graph | NO |

## 3. Internal-link opportunities (contextual-only)

> **Evidence class: STRUCTURAL / INTERNAL-LINK only.** Every item below is derived from the build's link graph and the legacy-link audit. **None is GSC-validated.** No position, impression, CTR or traffic figure is implied. Anchors are re-pointed by *anchor semantics -> 4.16 commercial-intent owner*; the blank empty-box sibling is never a target.

### 3.1 Summary table

| ID | Target (4.16 owner) | Source pages | Instances | Anchor type | Status | GSC-validated |
|---|---|---|---|---|---|---|
| ILO-1 | custom-wooden-speaker-cabinet-manufacturer (primary hub) | 9 | 13 | contextual-commercial-descriptor (varied; no repeated exact-match) | NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY | NO |
| ILO-2 | wooden-speaker-enclosure-manufacturer (acoustic-enclosure sibling) | 5 | 8 | contextual-acoustic-enclosure-descriptor | NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY | NO |
| ILO-3 | speaker-cabinet-cnc-machining-service (CNC sibling) | 2 | 2 | contextual-cnc-descriptor | NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY | NO |
| ILO-4 | wooden-speaker-box-manufacturer (box sibling) | 2 | 2 | contextual-box-descriptor | NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY | NO |
| ILO-5 | best-wood-for-speaker-boxes (materials page) | 3 | 3 | contextual-material-descriptor | VERIFIED_CORRECT_NO_CHANGE | NO |
| ILO-6 | per-legacy-URL owner slug | 10 | 28 | n/a-server-redirect | NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY | NO |
| ILO-7 | 4.16 commercial owner per page | 6 | 6 | contextual-descriptive (single per page, varied) | NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY | NO |

### 3.2 Detail

### ILO-1 — REPOINT_LEGACY_TO_4_16_OWNER

- **Target owner (4.16):** custom-wooden-speaker-cabinet-manufacturer (primary hub)
- **Target URL:** `https://woodsat.com/custom-wooden-speaker-cabinet-manufacturer/`
- **Source pages (9):** `about-us`, `best-wood-for-speaker-boxes`, `custom-cnc-wood-routing-services`, `speaker-box-finishes`, `speaker-box-materials`, `speaker-box-veneering`, `speaker-cabinet-manufacturing`, `subwoofer-enclosure-design`, `wooden-speaker-cabinet-designs`
- **Instances:** 13
- **Anchor type:** contextual-commercial-descriptor (varied; no repeated exact-match)
- **Anchor examples:** "custom wooden speaker enclosures manufacturer"; "speaker cabinet builders"; "custom wooden speaker enclosures"; "custom speaker designs"; "luxury speaker cabinets"; "color-matched finishes"; "custom builder"; "Custom Speaker Cabinet Builder Tool"; "multi-cabinet audio systems"; "3D veneer visualizer"; "3D cabinet builder"; "3D Cabinet Builder interface"; "custom wooden speaker enclosures manufacturer"
- **Contextual reason:** Every source page discusses a stage of cabinet manufacturing (materials, finishes, veneering, design, CNC routing, acoustic enclosures) and naturally names a manufacturer. The current legacy absolute URL 301-redirects to the blank empty-box placeholder, which cannot satisfy the commercial intent and drains authority from the 4.16 primary hub.
- **Evidence type:** STRUCTURAL_INTERNAL_LINK
- **Evidence:** _harness/legacy_absolute_link_evidence.json
- **Implementation status:** NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY
- **GSC-validated:** NO
- **Relates to:** OPP-1, OPP-2

### ILO-2 — REPOINT_LEGACY_TO_4_16_OWNER

- **Target owner (4.16):** wooden-speaker-enclosure-manufacturer (acoustic-enclosure sibling)
- **Target URL:** `https://woodsat.com/wooden-speaker-enclosure-manufacturer/`
- **Source pages (5):** `acoustic-wood-speaker-enclosures`, `speaker-box-finishes`, `speaker-box-materials`, `speaker-box-veneering`, `subwoofer-enclosure-design`
- **Instances:** 8
- **Anchor type:** contextual-acoustic-enclosure-descriptor
- **Anchor examples:** "acoustic enclosure manufacturers"; "reference monitor enclosures"; "precision loudspeaker cabinets"; "High-end home audio"; "hi-fi cabinets"; "high-end speaker pairs"; "professional cabinets"; "high-fidelity"
- **Contextual reason:** Anchors explicitly describe acoustic / reference-monitor / hi-fi / professional enclosures. Per 4.16 the acoustic-enclosure intent is owned by wooden-speaker-enclosure-manufacturer, not the blank empty-box sibling the legacy URL redirects to.
- **Evidence type:** STRUCTURAL_INTERNAL_LINK
- **Evidence:** _harness/legacy_absolute_link_evidence.json
- **Implementation status:** NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY
- **GSC-validated:** NO
- **Relates to:** OPP-1, OPP-2

### ILO-3 — REPOINT_LEGACY_TO_4_16_OWNER

- **Target owner (4.16):** speaker-cabinet-cnc-machining-service (CNC sibling)
- **Target URL:** `https://woodsat.com/speaker-cabinet-cnc-machining-service/`
- **Source pages (2):** `custom-cnc-wood-routing-services`, `speaker-box-veneering`
- **Instances:** 2
- **Anchor type:** contextual-cnc-descriptor
- **Anchor examples:** "CNC routers"; "complex cabinet shapes"
- **Contextual reason:** Anchors describe CNC routing and complex cabinet shapes; 4.16 ownership of the CNC-service intent is speaker-cabinet-cnc-machining-service.
- **Evidence type:** STRUCTURAL_INTERNAL_LINK
- **Evidence:** _harness/legacy_absolute_link_evidence.json
- **Implementation status:** NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY
- **GSC-validated:** NO
- **Relates to:** OPP-1, OPP-2

### ILO-4 — REPOINT_LEGACY_TO_4_16_OWNER

- **Target owner (4.16):** wooden-speaker-box-manufacturer (box sibling)
- **Target URL:** `https://woodsat.com/wooden-speaker-box-manufacturer/`
- **Source pages (2):** `speaker-box-materials`, `subwoofer-enclosure-design`
- **Instances:** 2
- **Anchor type:** contextual-box-descriptor
- **Anchor examples:** "Marine & Rugged Outdoor Enclosures"; "Home theater subwoofers"
- **Contextual reason:** Anchors describe rugged/marine and subwoofer boxes; per 4.16 these map to wooden-speaker-box-manufacturer.
- **Evidence type:** STRUCTURAL_INTERNAL_LINK
- **Evidence:** _harness/legacy_absolute_link_evidence.json
- **Implementation status:** NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY
- **GSC-validated:** NO
- **Relates to:** OPP-1, OPP-2

### ILO-5 — VERIFIED_CORRECT_NO_CHANGE

- **Target owner (4.16):** best-wood-for-speaker-boxes (materials page)
- **Target URL:** `https://woodsat.com/best-wood-for-speaker-boxes/`
- **Source pages (3):** `speaker-box-finishes`, `speaker-box-materials`, `speaker-cabinet-manufacturing`
- **Instances:** 3
- **Anchor type:** contextual-material-descriptor
- **Anchor examples:** "closed-grain woods"; "wood stability"; "hardwood construction"
- **Contextual reason:** These 3 legacy links already 301-redirect to the correct owner (best-wood-for-speaker-boxes). Recorded to prove the methodology preserves correct routing and that only the 25 mis-routed links are in scope for ILO-1..4.
- **Evidence type:** STRUCTURAL_INTERNAL_LINK
- **Evidence:** _harness/legacy_absolute_link_evidence.json
- **Implementation status:** VERIFIED_CORRECT_NO_CHANGE
- **GSC-validated:** NO
- **Relates to:** OPP-1

### ILO-6 — SERVER_SIDE_REDIRECT_SAFETY_NET

- **Target owner (4.16):** per-legacy-URL owner slug
- **Target URL:** `see target_map (one 301 per legacy URL to its 4.16 owner slug)`
- **Source pages (10):** `about-us`, `acoustic-wood-speaker-enclosures`, `best-wood-for-speaker-boxes`, `custom-cnc-wood-routing-services`, `speaker-box-finishes`, `speaker-box-materials`, `speaker-box-veneering`, `speaker-cabinet-manufacturing`, `subwoofer-enclosure-design`, `wooden-speaker-cabinet-designs`
- **Instances:** 28
- **Anchor type:** n/a-server-redirect
- **Contextual reason:** These 6 legacy production URLs are referenced from 28 body-copy links; after the WordPress->Hugo cutover they will 404 unless each is 301-redirected to its correct 4.16 owner slug. Server-side redirect is the safety net; ILO-1..4 fix the source markup so equity passes directly without a redirect hop.
- **Server redirect map (legacy -> owner slug):**
  - `custom-wooden-speaker-enclosures-manufacturer` -> `https://woodsat.com/custom-wooden-speaker-cabinet-manufacturer/`
  - `custom-speaker-cabinet-builder` -> `https://woodsat.com/custom-wooden-speaker-cabinet-manufacturer/`
  - `high-quality-speaker-enclosures` -> `https://woodsat.com/wooden-speaker-enclosure-manufacturer/`
  - `loudspeaker-cabinet-manufacturer` -> `https://woodsat.com/wooden-speaker-enclosure-manufacturer/`
  - `custom-speaker-and-subwoofer-cabinet-box-factory` -> `https://woodsat.com/wooden-speaker-box-manufacturer/`
  - `most-durable-wood-for-speakers` -> `https://woodsat.com/best-wood-for-speaker-boxes/`
- **Evidence type:** STRUCTURAL_INTERNAL_LINK
- **Evidence:** _harness/legacy_absolute_link_evidence.json
- **Implementation status:** NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY
- **GSC-validated:** NO
- **Relates to:** OPP-2

### ILO-7 — INFORMATIONAL_TO_COMMERCIAL_HANDOFF

- **Target owner (4.16):** 4.16 commercial owner per page
- **Target URL:** `per handoff target (single per page)`
- **Source pages (6):** `high-gloss-piano-lacquer-finishing-process-wood-speakers`, `mdf-vs-baltic-birch-plywood-speaker-cabinets`, `best-wood-for-speaker-boxes`, `subwoofer-enclosure-design`, `wooden-speaker-cabinet-designs`, `acoustic-wood-speaker-enclosures`
- **Instances:** 6
- **Anchor type:** contextual-descriptive (single per page, varied)
- **Contextual reason:** Six information pages whose content is adjacent to a commercial purchase currently have no working contextual link to the correct 4.16 owner (they link to the blank empty-box sibling or nowhere). Each proposal below is a single, semantically justified, per-page link -- not a sitewide nav addition and not repeated exact-match anchor text.
- **Per-page handoff targets:**
  - `high-gloss-piano-lacquer-finishing-process-wood-speakers` -> `https://woodsat.com/custom-wooden-speaker-cabinet-manufacturer/` — Premium-finish buyers are in-market for custom cabinets; the page's only commercial link currently points to the blank empty-box sibling. A single contextual link to the primary hub closes the loop.
  - `mdf-vs-baltic-birch-plywood-speaker-cabinets` -> `https://woodsat.com/custom-wooden-speaker-cabinet-manufacturer/` — Material-comparison readers are pre-purchase; the only commercial link today goes to the empty-box placeholder. Add one contextual link to the primary hub.
  - `best-wood-for-speaker-boxes` -> `https://woodsat.com/wooden-speaker-box-manufacturer/` — Material-selection page; add one contextual link to the box hub so the material->product handoff is direct (today its commercial references are misrouted legacy 301s).
  - `subwoofer-enclosure-design` -> `https://woodsat.com/wooden-speaker-box-manufacturer/` — Subwoofer-design readers; add one contextual link to the box hub.
  - `wooden-speaker-cabinet-designs` -> `https://woodsat.com/custom-wooden-speaker-cabinet-manufacturer/` — Design gallery; add one contextual link to the primary hub.
  - `acoustic-wood-speaker-enclosures` -> `https://woodsat.com/wooden-speaker-enclosure-manufacturer/` — Acoustic-enclosure page; add one contextual link to the enclosure hub.
- **Evidence type:** STRUCTURAL_INTERNAL_LINK
- **Evidence:** _harness/phase417_structural_facts.json (contextual_outbound graph)
- **Implementation status:** NOT_IMPLEMENTED_PROPOSED_ANALYSIS_ONLY
- **GSC-validated:** NO
- **Relates to:** P-11


### 3.3 Refinement principles applied (constraint 4)

- Keep only links semantically justified by source content AND target intent.
- Do not add sitewide / navigation links.
- Do not add artificial exact-match anchor repetition.
- Do not create links solely to increase link counts.
- Preserve PHASE 4.16 commercial intent ownership (each commercial query maps to its 4.16 owner page).
- The blank empty-box sibling is never a re-pointing target; it is the placeholder the legacy 301s wrongly credit.

**Re-pointing totals:** 28 legacy body-copy links total — 25 misrouted to the empty-box placeholder, 3 already correct (best-wood). Per-owner re-point: primary 13, enclosure 8, CNC 2, box 2, best-wood-correct 3.

## 4. The most important property of this list

**Every one of the 20 items is actionable without Search Console access.** Not one depends on a metric that is missing. The phase lost its performance layer, but the structural layer it recovered is independently sufficient to drive a full remediation programme.

What GSC would change is **ordering by realised value**, not the content of the list. Specifically it would tell us which of these defects is currently costing traffic and which is merely theoretical.

## 5. What is deliberately absent

- No opportunity is assigned an estimated traffic gain.
- No query is assigned a position, impression or CTR figure.
- No item is ranked by predicted click uplift.
- The three highest-value GSC-only opportunity classes — page-2 queries in striking distance, high-impression/low-CTR pages, and empirically confirmed cannibalization — are **absent from this list entirely** because they cannot be identified without data. Their absence is the concrete cost of `GSC_DATA_AVAILABLE=false`.

## 6. Status

| Item | Value |
|---|---|
| §26 requirement | **PARTIAL** — 20 opportunities delivered, all structural |
| Items requiring GSC to act on | **0 of 20** |
| Fabricated metrics | 0 |
| P0 items | 2 |
| P1 items | 7 |
| P2 items | 8 |
| P3 items | 3 |
| Internal-link opportunities (ILO-1..7) | 7 (all STRUCTURAL, gsc_validated=false) |
