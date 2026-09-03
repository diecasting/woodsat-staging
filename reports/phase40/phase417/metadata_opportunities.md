# PHASE 4.17 — Metadata Opportunities (Structural)

**GSC_DATA_AVAILABLE:** `false`
**Evidence class:** STRUCTURAL / ON-PAGE only — none GSC-validated.
**Note:** No SERP CTR or impression data exists, so these are *presentation-risk* findings (snippet truncation, title clipping), not performance findings.

---

## 1. Title-tag length (STRUCTURAL, OPP-3)

Three commercial titles exceed the ~65-character SERP budget and clip the 4.16 differentiating suffix that was deliberately paid for:

| Page | Title length | Clipped tail |
|---|---|---|
| `oem-wooden-speaker-cabinet-manufacturer` | 72 | `| Custom Audio Enclosure Factory` |
| `speaker-cabinet-cnc-machining-service` | 71 | `| Precision Wood CNC Manufacturer` |
| `hifi-speaker-cabinet-manufacturer` | 70 | `| Audiophile Speaker Cabinets` |

All other 22 pages are within 30–65. (Note: 4.16 `commercial_page_inventory.json` mis-records sibling `yoast_title` values; this was corrected in `gsc_data_quality_report.md` §5.2 — the site front matter is intact.)

## 2. Meta-description length (STRUCTURAL, OPP-4)

**17 of 25** meta descriptions exceed the ~160-character snippet budget; all 7 commercial pages are affected. Worst:

| Page | Meta description length |
|---|---|
| `mdf-vs-baltic-birch-plywood-speaker-cabinets` | 336 (≈ half never renders) |
| `speaker-box-calculator` | 226 |
| `wooden-speaker-enclosure-manufacturer` | 209 |
| `oem-wooden-speaker-cabinet-manufacturer` | 199 |
| `custom-wooden-speaker-cabinet-manufacturer` | 198 |
| `wooden-speaker-box-manufacturer` | 195 |
| `wooden-vs-mdf-speaker-cabinets` | 196 |
| `custom-empty-wooden-speaker-cabinet-boxes-manufacturer` | 189 |
| `hifi-speaker-cabinet-manufacturer` | 182 |
| `speaker-cabinet-manufacturing` | 183 |
| `speaker-cabinet-cnc-machining-service` | 184 |
| `speaker-box-materials` | 214 |
| `acoustic-wood-speaker-enclosures` | 176 |
| `subwoofer-enclosure-design` | 177 |
| `best-wood-for-speaker-boxes` | 148 |
| `speaker-box-veneering` | 160 |
| `speaker-box-finishes` | 155 |

## 3. Status

- All metadata findings are **STRUCTURAL** (measured lengths), **not** GSC-backed (no CTR/impression evidence).
- `requires_gsc`: false — actionable without Search Console.
- No metadata value is fabricated; lengths are exact from `phase417_structural_facts.json`.
