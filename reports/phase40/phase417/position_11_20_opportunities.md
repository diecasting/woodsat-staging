# PHASE 4.17 — Position 11–20 Opportunities (**MOST IMPORTANT BUCKET**)

**GSC_DATA_AVAILABLE:** `false`
**Machine-readable twin:** `position_11_20_opportunities.csv` — header + 1 explicit `NOT_AVAILABLE` status row, **0 fabricated data rows**
**Bucket status:** `NOT_AVAILABLE`

---

## 1. Result

**No queries can be placed in the 11–20 position bucket.** Section 13 designates this bucket the single most important output of the phase, and it is the one output that is completely dependent on Search Console. With no reachable Woodsat property, the bucket is empty by refusal, not by measurement.

Emitting invented rows here would be the most damaging possible fabrication in this entire phase, because this bucket is the one a human would act on first. It is left empty on purpose.

## 2. Why 11–20 is the highest-leverage bucket

Positions 11–20 are page 2. They earn effectively no clicks — but they carry proof of relevance: Google already considers the page a candidate for the query and has indexed and evaluated it. The gap to page 1 is usually a matter of authority distribution and topical depth, not of existence.

Consequences for prioritisation:

- A 4–10 query needs snippet and intent tuning → small, fast gains.
- An 11–20 query needs a few internal links and modest depth → **step-change** gains (0 clicks → meaningful clicks).
- A 21–50 query usually needs new content → slow, expensive.

That is why 11–20 is where a fixed budget of internal links and editorial effort produces the largest realised traffic delta. Losing this bucket is the most material consequence of `GSC_DATA_AVAILABLE=false`, and it is the reason this phase closes as `PARTIAL` rather than `PASS`.

## 3. Exact analysis that will run once access is granted

```
FILTER: position >= 11 AND position <= 20 AND impressions >= 10
RANK BY: impressions DESC within commercial classes
         (COMMERCIAL, OEM_ODM, SERVICE, PRODUCT_APPLICATION first)
FLAG:   correct_owner == false            → route/ownership problem, fix first
        contextual_inbound_count < 6      → internal-link starvation
        owner_word_count < 900            → depth deficit
        title_tag_len > 65                → snippet clipped
ACTION TIERS:
  T1  correct owner + starved links       → add contextual internal links only
  T2  correct owner + shallow content     → deepen existing page
  T3  wrong owner ranking                 → consolidate intent, re-point links
  T4  no owner page exists                → new page (last resort)
```

## 4. What the site-side substrate already tells us (data-backed, position-free)

Even with the bucket blocked, the two conditions that most often *cause* an 11–20 plateau were measured directly and both are present on the highest-value pages:

**(a) Internal-link starvation on the highest-margin commercial page.**

| Commercial page (4.16 role) | Contextual inbound | Rank within commercial set |
|---|---|---|
| `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` (empty) | 11 | 1 |
| `custom-wooden-speaker-cabinet-manufacturer` (**primary hub**) | 8 | 2 |
| `oem-wooden-speaker-cabinet-manufacturer` (OEM/ODM) | 7 | 3 |
| `speaker-cabinet-cnc-machining-service` (CNC) | 7 | 3 |
| `wooden-speaker-enclosure-manufacturer` (enclosure) | 6 | 5 |
| `wooden-speaker-box-manufacturer` (box) | 6 | 5 |
| `hifi-speaker-cabinet-manufacturer` (**audiophile**) | **4** | **7 / last** |

The audiophile page — the highest-margin segment in the 4.16 commercial model — is last in internal support. If any Woodsat commercial query is currently stuck on page 2, `hifi` is the structurally most likely candidate and the cheapest to move.

**(b) A far larger link-equity misallocation, discovered in this phase.**

28 in-body contextual links across 10 pages point at **six legacy production URLs that do not exist in the Hugo build**. Read-only probes confirm that 25 of those 28 links 301-redirect into `custom-empty-wooden-speaker-cabinet-boxes-manufacturer`. Post-redirect, the empty-box sibling effectively receives **36** contextual inbound links against the primary hub's **8** — a 4.5× inversion against the page 4.16 designated as primary. Anchor text on those links reads *"custom wooden speaker enclosures manufacturer"*, *"loudspeaker cabinet manufacturer"*, *"speaker cabinet builders"* — primary-hub and enclosure intent, delivered to the empty-box page.

This is precisely the kind of defect that pins a primary commercial page at 11–20 while a secondary sibling outranks it. It is fully documented in `internal_link_opportunities.md` and is the phase's top P0 recommendation. **It was found without GSC data and is actionable without GSC data.**

## 5. Status

| Item | Value |
|---|---|
| Rows in bucket | 0 (blocked) |
| Fabricated rows | 0 |
| §13 requirement | **NOT_AVAILABLE** — the phase's primary gap |
| Compensating data-backed finding | 28 legacy contextual links → 25 misrouted to the wrong sibling |
| Blocking dependency | Search Console access to a Woodsat property |
