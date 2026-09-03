# PHASE 4.17 — Commercial Page GSC Performance

**GSC_DATA_AVAILABLE:** `false`
**Performance metrics:** `NOT_AVAILABLE`
**Structural readiness profile:** **DATA-BACKED — 7 / 7 commercial pages**

---

## 1. Result

§20 asks for per-page clicks, impressions, CTR and average position for each commercial page defined in 4.16. All four metrics are `NOT_AVAILABLE`; no Woodsat Search Console property is reachable.

What is delivered instead is a complete, measured **readiness profile** for all seven commercial pages: the on-page and link-graph attributes that determine whether a page can convert a ranking into traffic. These are the inputs that will be joined to performance data the moment it exists.

## 2. Commercial page performance table (metrics blocked)

| Page | 4.16 role | Clicks | Impr. | CTR | Position |
|---|---|---|---|---|---|
| `custom-wooden-speaker-cabinet-manufacturer` | PRIMARY HUB | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE |
| `oem-wooden-speaker-cabinet-manufacturer` | OEM / ODM | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE |
| `hifi-speaker-cabinet-manufacturer` | audiophile | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE |
| `wooden-speaker-enclosure-manufacturer` | enclosure | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE |
| `wooden-speaker-box-manufacturer` | box | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE |
| `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | empty / blank | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE |
| `speaker-cabinet-cnc-machining-service` | CNC service | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE | NOT_AVAILABLE |

## 3. Structural readiness profile (fully data-backed)

| Page | Owned queries | Words | H2 | Contextual inbound | Effective inbound after legacy 301s | Title len | Desc len | JSON-LD | Contact form |
|---|---|---|---|---|---|---|---|---|---|
| `custom-wooden-speaker-cabinet-manufacturer` | 6 | 1239 | 16 | 8 | **8** | 45 ✓ | 198 ✗ | 1 | YES |
| `oem-wooden-speaker-cabinet-manufacturer` | 4 | 1224 | 18 | 7 | 7 | **72 ✗** | 199 ✗ | 1 | YES |
| `hifi-speaker-cabinet-manufacturer` | 3 | 1270 | 16 | **4** | **4** | **70 ✗** | 182 ✗ | 1 | YES |
| `wooden-speaker-enclosure-manufacturer` | 2 | 1220 | 17 | 6 | 6 | 64 ✓ | 209 ✗ | 1 | YES |
| `wooden-speaker-box-manufacturer` | 3 | 1272 | 18 | 6 | 6 | 64 ✓ | 195 ✗ | 1 | YES |
| `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | 3 | 1441 | 18 | 11 | **36** | 55 ✓ | 189 ✗ | 1 | YES |
| `speaker-cabinet-cnc-machining-service` | 3 | 1298 | 19 | 7 | 7 | **71 ✗** | 184 ✗ | 1 | YES |

Technical hygiene is uniform and clean: every commercial page has exactly 1 `<h1>`, 1 JSON-LD block, a Formspree contact form, a production canonical, 16–19 `<h2>` sections and 1220–1441 words. There is no thin or malformed commercial page.

## 4. Three data-backed conclusions

**C1 — Content depth is not the constraint.**
All seven pages sit in a tight 1220–1441 word band with 16–19 H2 sections. No commercial page is under-built. Any future ranking deficit on these pages will not be explained by content volume, which removes the most commonly proposed and most expensive remedy from consideration.

**C2 — Authority distribution is inverted against commercial value.**
Ranking pages by internal support gives the exact reverse of the 4.16 value hierarchy:

```
effective contextual inbound:
  empty-box     36   <- sibling, narrowest commercial segment
  primary hub    8   <- designated hub
  oem            7
  cnc            7
  enclosure      6
  box            6
  hifi           4   <- highest-margin segment, weakest support
```

The empty-box page receives 4.5× the primary hub's support and 9× the audiophile page's, entirely because of 25 legacy links whose anchor text belongs to the primary and hifi pages (see `wrong_landing_page_analysis.md`). This is the dominant structural defect on the commercial layer.

**C3 — SERP presentation is degraded on all seven, severely on three.**
All 7 descriptions exceed the ~160-character snippet budget. 3 titles exceed the ~65-character budget — `oem` (72), `cnc` (71), `hifi` (70) — and in each case the clipped tail is the 4.16 differentiating suffix. The differentiation is being paid for and then discarded before the user sees it.

## 5. Priority order for the commercial layer (structural basis, position-free)

| Rank | Page | Structural score | Dominant deficit |
|---|---|---|---|
| 1 | `hifi-speaker-cabinet-manufacturer` | **72.0** | lowest inbound (4) + title truncated + highest-margin segment |
| 2 | `oem-wooden-speaker-cabinet-manufacturer` | **68.2** | title truncated at 72 chars + 4 high-value OEM queries |
| 3 | `speaker-cabinet-cnc-machining-service` | **65.4** | title truncated at 71 chars |
| 4 | `custom-wooden-speaker-cabinet-manufacturer` | **57.9** | hub starved relative to its own sibling (8 vs 36) |
| 5 | `wooden-speaker-enclosure-manufacturer` | **53.3** | description 209 chars; moderate support |
| 6 | `wooden-speaker-box-manufacturer` | **52.8** | description 195 chars; moderate support |
| 7 | `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | **38.7** | over-supported; receiving anchors it should not own |

Scores from `top_20_search_opportunities.json`; formula = `commercial_role_weight(35) + authority_deficit(25) + serp_presentation_risk(25) + content_depth_headroom(15)`. **Contains no clicks, impressions, CTR or position input and is not a ranking prediction.**

## 6. What remains blocked

Per-page click and impression volume; observed CTR; average position; page-level trend; device and country splits; which of the seven pages actually earns the site's commercial traffic today. None of these is estimated anywhere in this report.

## 7. Status

| Item | Value |
|---|---|
| §20 GSC requirement | **NOT_AVAILABLE** |
| §20 structural requirement | **DATA-BACKED — 7/7 pages profiled** |
| Commercial pages with technical defects | 0 |
| Commercial pages with SERP presentation defects | 7 (3 severe) |
| Commercial pages with authority deficits | 2 (`hifi`, primary hub relative to `empty`) |
