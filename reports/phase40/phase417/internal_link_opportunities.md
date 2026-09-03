# PHASE 4.17 — Internal-Link Opportunities (Contextual-Only)

**GSC_DATA_AVAILABLE:** `false`
**Evidence class:** STRUCTURAL / INTERNAL-LINK only — none GSC-validated.
**Machine-readable twin:** `top_20_search_opportunities.json` (`internal_link_opportunities` array).
**Read-only phase:** no links are modified here; these are recommendations for a future implementation phase.

---

## 1. Method

The contextual link graph was extracted from the built HTML by separating `<main>` body copy links from header/footer navigation. Body-copy links were then classified as either (a) working links to the correct 4.16 owner, (b) misrouted legacy absolute URLs that 301-redirect to the blank empty-box sibling, or (c) absent where content justifies a commercial handoff.

Every re-pointing opportunity below obeys the contextual-only refinement rule:

- Keep only links semantically justified by source content AND target intent.
- Do not add sitewide / navigation links.
- Do not add artificial exact-match anchor repetition.
- Do not create links solely to increase link counts.
- Preserve PHASE 4.16 commercial intent ownership (each commercial query maps to its 4.16 owner page).
- The blank empty-box sibling is never a re-pointing target; it is the placeholder the legacy 301s wrongly credit.

## 2. Re-pointing totals

- Legacy body-copy absolute links audited: **28**
- Misrouted to the blank empty-box placeholder: **25** (ILO-1..4)
- Already correct (best-wood-for-speaker-boxes): **3** (ILO-5, no change)
- Per-owner re-point: primary **13**, enclosure **8**, CNC **2**, box **2**, best-wood-correct **3**
- Server-side safety net: **6** legacy URLs -> owner slug 301s (ILO-6)
- Informational->commercial handoff gaps identified: **6** per-page proposals (ILO-7)

## 3. Opportunity catalogue

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


## 4. What this is NOT

- It is **not** a GSC-validated link-equity analysis. No ranking, impression, CTR or traffic figure is attached to any of these opportunities.
- It is **not** a recommendation to add sitewide footer/nav links, to repeat exact-match anchors across pages, or to add links purely to inflate counts.
- The blank empty-box sibling (`custom-empty-wooden-speaker-cabinet-boxes-manufacturer`) is **never** a re-pointing target; it is the placeholder the legacy 301s wrongly credit, and ILO-1..4 redirect authority back to the proper 4.16 owners.

## 5. Evidence files

- `_harness/legacy_absolute_link_evidence.json` — 28 audited legacy link instances (source, anchor, legacy target, 301 destination).
- `_harness/phase417_structural_facts.json` — contextual inbound/outbound graph per page.
- `top_20_search_opportunities.json` — machine-readable twin of this report.
