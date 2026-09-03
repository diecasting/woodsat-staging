# PHASE 4.17 — Wrong Landing Page Analysis

**GSC_DATA_AVAILABLE:** `false`
**GSC-observed landing-page mismatches:** `NOT_AVAILABLE`
**Site-side routing mismatches:** **DATA-BACKED — 28 instances found**

---

## 1. Result

§17 asks which queries land on a page other than the one 4.16 designated as owner. The *observed* answer requires the GSC `query × page` pairing and is `NOT_AVAILABLE` — no Woodsat property is reachable, so `actual_gsc_landing_page` is `NOT_AVAILABLE` for all 46 rows of `query_url_performance_map.csv`.

But "wrong landing page" has a second, entirely site-side form that needs no GSC at all: **a link whose anchor text declares one intent while the URL delivers the user to a page that owns a different intent.** That form was audited exhaustively across the build, and **28 instances were found.** This is the most consequential finding of PHASE 4.17.

## 2. The finding: 28 contextual links routed to non-existent pages via legacy 301s

Six absolute production URLs are used as link targets inside page body copy. **None of the six exists in the Hugo build.** Read-only HTTP probes against production establish where each actually resolves:

| Legacy URL referenced in body copy | In build | Production first hop | Final destination |
|---|---|---|---|
| `/custom-wooden-speaker-enclosures-manufacturer/` | NO | `301` | `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/custom-speaker-cabinet-builder/` | NO | `301` | `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/high-quality-speaker-enclosures/` | NO | `301` | `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/loudspeaker-cabinet-manufacturer/` | NO | `301` | `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/custom-speaker-and-subwoofer-cabinet-box-factory/` | NO | `301` | `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| `/most-durable-wood-for-speakers/` | NO | `301` | `/best-wood-for-speaker-boxes/` |

**25 of the 28 link instances terminate on `custom-empty-wooden-speaker-cabinet-boxes-manufacturer`.** 3 terminate on `best-wood-for-speaker-boxes`.

Evidence file: `_harness/legacy_absolute_link_evidence.json` (all 28 instances with source page, target, anchor text and resolved destination).

## 3. Why this is a wrong-landing-page problem, not merely a redirect problem

Per 4.16, `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` owns exactly one cluster: **empty / blank speaker boxes** (`empty speaker box`, `empty speaker cabinet manufacturer`, `blank speaker cabinet`). It is a sibling, not the hub.

Yet the anchor text arriving there declares completely different intents:

| Source page | Anchor text | Intent the anchor declares | Intent the destination owns |
|---|---|---|---|
| `about-us` | "custom wooden speaker enclosures manufacturer" | **primary hub** | empty boxes |
| `wooden-speaker-cabinet-designs` | "custom wooden speaker enclosures manufacturer" | **primary hub** | empty boxes |
| `best-wood-for-speaker-boxes` | "custom wooden speaker enclosures" | **primary hub** | empty boxes |
| `acoustic-wood-speaker-enclosures` | "acoustic enclosure manufacturers" | enclosure sibling | empty boxes |
| `acoustic-wood-speaker-enclosures` | "precision loudspeaker cabinets" | enclosure sibling | empty boxes |
| `speaker-box-veneering` | "professional cabinets" | enclosure / box sibling | empty boxes |
| `speaker-box-finishes` | "High-end home audio" | **hifi sibling** | empty boxes |
| `speaker-box-finishes` | "luxury speaker cabinets" | **hifi sibling** | empty boxes |
| `speaker-box-materials` | "hi-fi cabinets" | **hifi sibling** | empty boxes |
| `speaker-box-veneering` | "high-end speaker pairs" | **hifi sibling** | empty boxes |
| `subwoofer-enclosure-design` | "high-fidelity" | **hifi sibling** | empty boxes |
| `custom-cnc-wood-routing-services` | "CNC routers" | **CNC sibling** | empty boxes |
| `custom-cnc-wood-routing-services` | "custom speaker designs" | primary hub | empty boxes |
| `speaker-box-materials` | "Marine & Rugged Outdoor Enclosures" | no owner page exists | empty boxes |
| `subwoofer-enclosure-design` | "Home theater subwoofers" | subwoofer page | empty boxes |
| `speaker-box-veneering` | "complex cabinet shapes" | CNC sibling | empty boxes |
| `speaker-box-finishes` | "color-matched finishes" | finishes page (self-topic) | empty boxes |
| `speaker-box-finishes` | "custom builder" | tool that does not exist | empty boxes |
| `speaker-box-materials` | "Custom Speaker Cabinet Builder Tool" | tool that does not exist | empty boxes |
| `speaker-box-veneering` | "3D veneer visualizer" | tool that does not exist | empty boxes |
| `speaker-cabinet-manufacturing` | "3D cabinet builder" | tool that does not exist | empty boxes |
| `subwoofer-enclosure-design` | "3D Cabinet Builder interface" | tool that does not exist | empty boxes |
| `best-wood-for-speaker-boxes` | "speaker cabinet builders" | primary hub | empty boxes |
| `speaker-box-finishes` | "closed-grain woods" | materials page | `best-wood-for-speaker-boxes` ✓ |
| `speaker-box-materials` | "wood stability" | materials page | `best-wood-for-speaker-boxes` ✓ |
| `speaker-cabinet-manufacturing` | "hardwood construction" | materials page | `best-wood-for-speaker-boxes` ✓ |

Only the 3 links resolving to `best-wood-for-speaker-boxes` are semantically coherent. **The 25 links resolving to the empty-box page are all intent mismatches**, and 5 of them promise an interactive "3D cabinet builder" tool that exists nowhere on the site — a user-facing broken promise as well as an SEO defect.

## 4. Quantified consequence: authority inversion against the designated primary

Contextual inbound links, before and after accounting for the 301s:

| Page | 4.16 role | In-build contextual inbound | + legacy 301 inflow | **Effective total** |
|---|---|---|---|---|
| `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | empty-box sibling | 11 | **+25** | **36** |
| `custom-wooden-speaker-cabinet-manufacturer` | **PRIMARY HUB** | 8 | +0 | **8** |
| `oem-wooden-speaker-cabinet-manufacturer` | OEM/ODM | 7 | +0 | 7 |
| `speaker-cabinet-cnc-machining-service` | CNC | 7 | +0 | 7 |
| `wooden-speaker-enclosure-manufacturer` | enclosure | 6 | +0 | 6 |
| `wooden-speaker-box-manufacturer` | box | 6 | +0 | 6 |
| `hifi-speaker-cabinet-manufacturer` | audiophile | 4 | +0 | 4 |
| `best-wood-for-speaker-boxes` | informational | 6 | +3 | 9 |

The empty-box sibling ends up with **4.5× the internal support of the page 4.16 designated as primary**, and **9× that of the audiophile page** — driven entirely by links whose anchor text belongs to the primary and hifi pages.

This is the classic mechanism by which a secondary page outranks its own hub for the hub's head terms. It cannot be confirmed as *actually happening* without GSC — but the structural cause is present, measured, and fixable independently of GSC.

## 5. Cross-check against PHASE 4.14

4.14 performed "P0/P1 link-route fixes" and reported zero broken internal links. That result is not contradicted: these 28 links are written as **absolute production URLs** (`https://woodsat.com/...`), so a relative-route validator correctly classifies them as external and skips them. They are simultaneously (a) invisible to internal-link validation, (b) live and redirecting on production, and (c) pointing at pages absent from the Hugo build. The gap is in validator scope, not in 4.14's execution.

Secondary observation: on the staging deployment these links navigate the user off staging and onto production — harmless for analysis, but it means staging cannot be used to verify these particular journeys.

## 6. What remains blocked

- Which queries actually land on a page other than the intended owner.
- Whether the empty-box page is in fact absorbing primary-hub or hifi queries.
- Impression/click volume attached to each mismatch, hence the true cost.

## 7. Recommendations (analysis only — nothing was changed)

| ID | Priority | Recommendation |
|---|---|---|
| WLP-1 | **P0** | Re-point the 22 primary/hifi/enclosure/CNC-intent anchors from the legacy empty-box-redirecting URLs to their correct 4.16 owner pages, using relative Hugo routes rather than absolute production URLs. |
| WLP-2 | **P0** | Convert the 3 coherent `best-wood-for-speaker-boxes` links from the legacy `/most-durable-wood-for-speakers/` URL to the direct route, removing the redirect hop. |
| WLP-3 | **P1** | Resolve the 5 anchors promising a "3D Cabinet Builder" tool: either build the tool, or re-word the anchors. Currently they mislead users and waste anchor text. |
| WLP-4 | **P1** | Extend the link validator to flag absolute `https://woodsat.com/...` links in body copy whose path has no matching Hugo route — the exact class 4.14 could not see. |
| WLP-5 | **P2** | Evaluate `loudspeaker cabinet manufacturer` as a head term with no owner page; a legacy URL for it existed, so historical relevance is plausible. |

## 8. Status

| Item | Value |
|---|---|
| §17 GSC requirement | **NOT_AVAILABLE** |
| §17 structural requirement | **DATA-BACKED — 28 mismatches, 25 material** |
| Site modifications made | **0** (read-only phase) |
| Highest-severity finding of PHASE 4.17 | authority inversion: empty-box 36 vs primary hub 8 |
