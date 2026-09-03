# PHASE 4.17 — Trend Analysis

**GSC_DATA_AVAILABLE:** `false`
**Status:** `NOT_AVAILABLE` — blocked twice over

---

## 1. Result

Section 24 requires period-over-period comparison of clicks, impressions, CTR and position — typically last 28 days vs previous 28 days, or last 90 vs previous 90. This is `NOT_AVAILABLE` for two independent and compounding reasons:

**Reason 1 — no data.** No Woodsat Search Console property is reachable. All six Woodsat property forms returned `HTTP 403 — User does not have sufficient permission`. There is no single period to measure, let alone two.

**Reason 2 — no comparable baseline even if access were granted today.** Trend analysis requires two windows of the *same* site state. The Woodsat property has never been measured in any prior phase of this programme:

- 4.15 recorded no GSC baseline (the audit was PARTIAL for the same access reason).
- 4.16 implemented the commercial keyword architecture with no before-measurement.

So the earliest date from which a genuine 4.16 impact trend can be computed is the date access is first granted — and even then the "before" side will be missing. **The measurement opportunity for 4.16's impact has already been lost and cannot be recovered retroactively**, because Search Console only retains ~16 months of data and only for properties that were verified during that window. If no Woodsat property was ever verified, no history exists to recover at all.

This is the single most time-sensitive finding in PHASE 4.17.

## 2. Consequence: what cannot be answered, now or later

| Question | Status |
|---|---|
| Did impressions rise after 4.16 shipped? | **permanently unanswerable** without a pre-4.16 baseline |
| Did the sibling split gain or lose aggregate visibility? | **permanently unanswerable** |
| Is the site trending up or down overall? | answerable only from the first verified date forward |
| Did any query move between position buckets? | answerable only forward |
| Seasonality of speaker-cabinet demand | answerable forward, after ~12 months |

## 3. The one recoverable action, and its deadline

Verifying a Woodsat property in Search Console starts data collection **from the verification date forward**. Every day without verification is a day of permanently lost history. The cost of delay is linear and irreversible.

Recommended immediate action (outside this read-only phase):

```
1. Verify https://woodsat.com/ (or sc-domain:woodsat.com) in Search Console.
   - The GA4 property already exists (G-D5SVS3K8B0 in head.html), so the
     Google Analytics verification method is likely available immediately.
2. Grant the existing service account read access:
     gsc-api-reader@gsc-api-integration-506213.iam.gserviceaccount.com
   Search Console -> Settings -> Users and permissions -> Add user -> Restricted
3. Re-run the probe in _harness/ to confirm the property appears in sites.list.
4. From that date, a real trend baseline begins accumulating.
```

Note: the service account currently has `siteFullUser` access to exactly one property — `https://alumcasting.com/` — which proves the credential works and the wiring is correct. The only missing element is a Woodsat property grant.

## 4. Why the available alumcasting data cannot supply a trend

The one GSC dataset found on this machine covers `https://alumcasting.com/` (2026-05-23 → 2026-08-20, 3051 rows, 0 rows mentioning woodsat). It is a different property, a different industry (aluminium die-casting) and a different domain. It was schema-validated and then formally **REJECTED** as a Woodsat proxy in `gsc_data_availability.md`. Using it to construct a Woodsat trend would be fabrication of the most misleading kind — real-looking numbers from the wrong business.

## 5. Analysis that will run once two comparable windows exist

```
WINDOW A := most recent 28 complete days
WINDOW B := the 28 days immediately preceding A
FOR each page and each query:
    delta_clicks, delta_impressions, delta_ctr, delta_position
CLASSIFY:
    impressions up + position up      -> genuine gain
    impressions up + position down    -> broader matching, weaker relevance
    impressions flat + CTR up         -> snippet improvement working
    impressions down + position flat  -> demand-side seasonality, not a site issue
    position crossing 10 -> 11        -> page-1 loss, P0 alert
GUARD: exclude the first 3 days of each window (GSC data settles late).
```

## 6. Status

| Item | Value |
|---|---|
| §24 requirement | **NOT_AVAILABLE** |
| Blocking reason 1 | no reachable Woodsat property (403 on all forms) |
| Blocking reason 2 | no historical baseline was ever captured (4.15, 4.16) |
| Recoverable? | forward-only, from the verification date |
| Time sensitivity | **HIGH — history is being lost daily** |
| Fabricated metrics | 0 |
