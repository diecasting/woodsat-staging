# PHASE 4.17 — Content Gap vs Existing Page Decision

**GSC_DATA_AVAILABLE:** `false`
**GSC-confirmed gaps:** `NOT_AVAILABLE`
**Structurally confirmed gaps:** **DATA-BACKED — 1 confirmed, 2 candidates**

---

## 1. The decision this report exists to make

§28 requires that, for every gap, the phase decides between two options and does not conflate them:

| Option | When it is correct |
|---|---|
| **STRENGTHEN EXISTING PAGE** | a page already covers the intent, but lacks depth, links or presentation quality |
| **CREATE NEW PAGE** | no page owns the intent, and the intent is distinct enough that folding it into an existing page would dilute that page |

New pages are the expensive option and the default answer is *strengthen*. The bar for *create* is that no existing page can own the intent without damage.

Note that the strongest evidence for a gap — an unintended page ranking deep for a query nothing on the site serves — requires GSC and is unavailable. The gaps below are confirmed by architecture, not observation.

## 2. Gap 1 — `bookshelf speaker cabinet` → **CREATE NEW PAGE**

| Attribute | Value |
|---|---|
| Query class | PRODUCT_APPLICATION |
| Cluster | `bookshelf speaker cabinet` (1 query) |
| Owner page in 4.16 | **NONE** |
| Any page covering the intent | **NO** |
| Decision | **CREATE NEW PAGE** |

**Why this is a real gap and not an out-of-scope term.** The topic is already part of the business's marketing output — a production image asset is named
`https://woodsat.com/wp-content/uploads/2025/03/high-gloss-piano-lacquer-bookshelf-speaker-cabinet.png`
and is referenced from `best-wood-for-speaker-boxes`. The company photographs and sells bookshelf cabinets; it simply has no page that can rank for them.

**Why not fold it into an existing page.** The three candidate hosts each fail:

| Candidate host | Why folding fails |
|---|---|
| `wooden-speaker-cabinet-designs` | design-process page, not a product-format page; adding a format section would blur its owned intent (`speaker cabinet design`) |
| `hifi-speaker-cabinet-manufacturer` | bookshelf is a *format*, hi-fi is a *market segment*; the page already carries 3 audiophile queries on only 4 inbound links and cannot absorb a fourth intent |
| `custom-wooden-speaker-cabinet-manufacturer` | primary hub; adding format-specific content weakens hub generality, and the hub is already under-supported (8 links vs its sibling's 36) |

Bookshelf, floorstanding and subwoofer are the three cabinet formats. The site already has a dedicated format page for subwoofer (`subwoofer-enclosure-design`, 12 inbound links — the best-linked content page in the site). **The precedent is set: formats get their own pages.** Bookshelf is the missing member of that set, and floorstanding is absent too.

**Cross-check:** `phase415_content_gap.json` does not list this gap as previously rejected, so this is a new finding, not a re-opened decision.

## 3. Gap 2 — `loudspeaker cabinet manufacturer` → **CANDIDATE, decision deferred**

| Attribute | Value |
|---|---|
| Discovered via | legacy production URL `/loudspeaker-cabinet-manufacturer/` referenced by 3 in-body links |
| Present in the 46-query universe | **NO** |
| Current production behaviour | `301` → `/custom-empty-wooden-speaker-cabinet-boxes-manufacturer/` |
| Any page owning the term | **NO** |
| Decision | **DEFER** — needs GSC to justify |

"Loudspeaker" is standard professional and European terminology, distinct from the "speaker" vocabulary the site uses throughout. A dedicated URL for it existed historically, which suggests it was once considered commercially important. It now 301s to a page about empty boxes.

**Why deferred rather than decided.** Terminology variants are exactly the case where a new page risks cannibalizing the primary hub — `loudspeaker cabinet manufacturer` and `wooden speaker cabinet manufacturer` may well be the same intent expressed in two vocabularies, in which case the correct action is a strengthened hub, not a new page. A single GSC query (`loudspeaker` impressions and their landing pages) settles this decisively. Guessing risks re-creating the very cannibalization 4.16 removed.

**Interim recommendation:** re-point the 3 existing links from the legacy URL to `wooden-speaker-enclosure-manufacturer` (the closest owned intent), and revisit once data exists.

## 4. Gap 3 — "3D Cabinet Builder" tool → **NOT A CONTENT GAP — a broken promise**

Five separate anchors across four pages promise an interactive tool:

| Source page | Anchor text |
|---|---|
| `speaker-box-materials` | "Custom Speaker Cabinet Builder Tool" |
| `speaker-box-veneering` | "3D veneer visualizer" |
| `speaker-cabinet-manufacturing` | "3D cabinet builder" |
| `subwoofer-enclosure-design` | "3D Cabinet Builder interface" |
| `speaker-box-finishes` | "custom builder" |

No such page or tool exists anywhere in the build. All five links 301 into the empty-box product page.

**Decision: NOT a keyword content gap.** No commercial query in the universe targets a builder tool. This is a UX and credibility defect: the copy advertises a capability the site does not have, and every visitor who clicks lands somewhere unrelated. The correct fix is either to build the tool or to re-word the copy — a content-integrity decision, not an SEO one. The site does have `speaker-box-calculator` (931 words, 10 inbound links), which may be what the copy intended to reference; if so, all five anchors should point there.

## 5. Gaps explicitly NOT found

The following were checked and are **not** gaps — every one has an existing owner page of adequate depth. No new page is justified for any of them:

`speaker cabinet manufacturer`, `custom speaker cabinet manufacturer`, `speaker cabinet supplier`, `speaker cabinet factory`, all 4 OEM/ODM queries, all 3 hi-fi queries, all 4 CNC queries, all enclosure and box variants, all 3 empty-box queries, both subwoofer queries, all 3 materials queries, all 11 informational queries.

**44 of 46 queries need no new page.** The architecture 4.16 built is close to complete.

## 6. Summary of decisions

| Gap | Decision | Priority | Blocked on GSC? |
|---|---|---|---|
| `bookshelf speaker cabinet` | **CREATE NEW PAGE** | P2 | NO |
| `loudspeaker cabinet manufacturer` | **DEFER** — re-point links now, decide later | P2 | YES |
| "3D Cabinet Builder" tool | **NOT an SEO gap** — fix copy or build the tool | P1 | NO |
| Everything else (44 queries) | **STRENGTHEN EXISTING** — no new pages | — | NO |

## 7. Status

| Item | Value |
|---|---|
| §28 requirement | **PARTIAL** — decisions made where structure suffices |
| New pages recommended | **1** (`bookshelf speaker cabinet`) |
| New pages deferred | 1 |
| Existing-page-strengthening decisions | 44 queries |
| Fabricated metrics | 0 |
