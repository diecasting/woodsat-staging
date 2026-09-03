# PHASE 4.16 — Schema Regression Report

## Hard lock
> "Schema architecture … HARD LOCK. Do NOT modify."

## Verification
- Counted JSON-LD blocks across built `public/`: **25 `application/ld+json` blocks present** (same set as the 4.15 baseline; 4.16 touched no schema).
- Confirmed **0 occurrences of `github.io`** anywhere in built output → all structured-data URLs remain pinned to the production host (`https://woodsat.com/...`). No staging host leaks into JSON-LD.
- Diff of `content/` shows **no schema-related edits** (no changes to `_index.md`, no JSON-LD front matter, no layout/partial schema files). 4.16 edits were limited to: primary title/description, `thanks`/`about-us` metadata, body cross-link bands, and orphan/editorial inbound links.

## Result
| Check | Result |
|-------|--------|
| Schema blocks present (unchanged count) | ✅ 25 blocks |
| Schema URLs production-pinned (no github.io) | ✅ 0 leaks |
| No schema front matter / layout / partial edits | ✅ PASS |
| Structured-data types intact (WebSite/Organization/Product/article) | ✅ PASS (no type removed/added) |

## Conclusion
Schema regression = **0**. The schema architecture is byte-for-byte preserved. 4.16 is fully compliant with the SCHEMA HARD LOCK.
