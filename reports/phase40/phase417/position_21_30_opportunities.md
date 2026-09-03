# PHASE 4.17 — Position 21–30 Opportunities (page 3 — "needs real work")

**GSC_DATA_AVAILABLE:** `false`
**Bucket status:** `NOT_AVAILABLE`

---

## 1. Result

**No queries can be placed in the 21–30 position bucket.** No Search Console property for Woodsat is reachable, so no position values exist. Zero rows are emitted; none are estimated.

## 2. Interpretation rules for this bucket (retained for future execution)

Positions 21–30 mean Google has indexed the page and considers it topically related, but ranks it behind roughly twenty better-supported competitors. Unlike 11–20, a couple of internal links will not usually close this gap. The diagnosis fork is:

| Observed pattern | Diagnosis | Correct response |
|---|---|---|
| Commercial query, correct owner page, thin content | depth deficit | expand the existing page substantially |
| Commercial query, **wrong** page ranking | intent mismatch | fix ownership + re-point anchors before touching content |
| Commercial query, no owner page | genuine content gap | create a dedicated page |
| Informational query | usually acceptable | deprioritise unless it feeds a commercial cluster |

## 3. Structural candidates that would most plausibly populate this bucket

Stated as structure, not as ranking. The pages combining commercial or semi-commercial intent with the weakest depth-and-support profile are the ones that, on general SEO mechanics, tend to sit deep on page 2–3:

| Page | Words | Contextual inbound | Structural weakness |
|---|---|---|---|
| `wooden-vs-mdf-speaker-cabinets` | 837 | **2** | second-lowest inbound in the whole site; comparison intent competes with a stronger sibling (`mdf-vs-baltic-birch…`, 1087 words) |
| `high-gloss-piano-lacquer-finishing-process-wood-speakers` | 1141 | **1** | **lowest inbound of any content page**; long-tail finishing topic with almost no internal support |
| `speaker-cabinet-manufacturing` | **675** | 9 | well linked but the thinnest body among process pages; broad head-term topic ("speaker cabinet construction") on a short page |
| `custom-cnc-wood-routing-services` | **619** | 11 | thinnest page carrying a SERVICE query (`cnc wood routing`) |
| `speaker-box-finishes` | 623 | 10 | thin body for a topic with wide query surface |

Note the pattern: `high-gloss-piano-lacquer…` and `wooden-vs-mdf…` have adequate content depth (1141 / 837 words) but almost no internal support (1 / 2 links), while `custom-cnc-wood-routing-services` and `speaker-cabinet-manufacturing` have strong support (11 / 9 links) but thin bodies (619 / 675 words). These are two different failure modes requiring two different fixes, and both are visible without any GSC data.

**No claim is made that any of these pages does or does not rank 21–30.**

## 4. Query classes that would land here if they surface

From the 46-query universe, the classes most likely to appear deep are the broad head terms whose owner page is comparatively thin:

- `speaker cabinet construction` → owner `speaker-cabinet-manufacturing` (675 words)
- `cnc wood routing` → owner `custom-cnc-wood-routing-services` (619 words)
- `speaker box finishes` → owner `speaker-box-finishes` (623 words)
- `mdf vs plywood speaker` → owner `wooden-vs-mdf-speaker-cabinets` (2 inbound links)
- `piano lacquer speaker finish` → owner `high-gloss-piano-lacquer…` (1 inbound link)

## 5. Status

| Item | Value |
|---|---|
| Rows in bucket | 0 (blocked) |
| Fabricated rows | 0 |
| §14 requirement | **NOT_AVAILABLE** — documented, not skipped |
| Blocking dependency | Search Console access to a Woodsat property |
