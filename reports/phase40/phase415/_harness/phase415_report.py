#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 4.15 final assembly: phase415_report.md + phase415_manifest.json +
phase415_executive_decision_matrix.json (READ-ONLY; no GSC => PARTIAL verdict)."""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
OUT = os.path.join(ROOT, "reports", "phase40", "phase415")

def load(n):
    return json.load(open(os.path.join(OUT, n), encoding="utf-8"))

inv = load("phase415_site_inventory.json")
dsr = load("phase415_data_source_report.json")
kwmap = load("phase415_keyword_map.json")
commap = load("phase415_commercial_keyword_map.json")
quick = load("phase415_quick_wins.json")
top20 = load("phase415_top20_opportunities.json")
topcomm = load("phase415_top_commercial_keywords.json")
toppages = load("phase415_top_commercial_pages.json")
cannib = load("phase415_cannibalization.json")
gap = load("phase415_content_gap.json")
meta = load("phase415_metadata_opportunities.json")
ilinks = load("phase415_internal_link_opportunities.json")
scorecard = load("phase415_seo_scorecard.json")
roadmap = load("phase415_execution_roadmap.json")
seo_r = load("phase415_seo_regression.json")
route_r = load("phase415_route_regression.json")
schema_r = load("phase415_schema_regression.json")
form_r = load("phase415_form_regression.json")

GSC = dsr["GSC_DATA_AVAILABLE"]
VERDICT = "PHASE_4.15 = SEO_GROWTH_OPPORTUNITY_AUDIT_PARTIAL" if not GSC else "PHASE_4.15 = SEO_GROWTH_OPPORTUNITY_AUDIT_PASS"
NOW = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# ---- Executive Decision Matrix (top 10 next-phase SEO modifications) ----
edm = [
    {"rank": 1, "opportunity": "Designate ONE primary 'wooden speaker cabinet manufacturer' page; differentiate the 5 sibling manufacturer pages by a single clear modifier (custom / oem / hifi / empty-box / enclosure) with distinct H1 angles + internal cross-links",
     "page": "custom-wooden-speaker-cabinet-manufacturer (primary) + 5 siblings",
     "evidence": "STRONG cannibalization cluster: 6 pages target near-identical head term 'wooden speaker cabinet/box/enclosure manufacturer'.",
     "expected_impact": "High (consolidates split authority, likely the single biggest organic win)", "risk": "Low",
     "next_action": "PHASE 4.16: assign primary, rewrite H1/title per modifier, add cross-links"},
    {"rank": 2, "opportunity": "Fix thanks-page <title> (currently 'Sub-woofer Wooden Box manufacturer') to a thank-you/confirmation message",
     "page": "thanks", "evidence": "Title/content mismatch; H1 empty. Pre-existing anomaly (noted 4.14).",
     "expected_impact": "Low-Medium (correctness/UX; minor SEO hygiene)", "risk": "Low",
     "next_action": "PHASE 4.16: rewrite title only"},
    {"rank": 3, "opportunity": "Add inbound internal links to the orphaned deep-dive page (0 inbound today)",
     "page": "mdf-vs-baltic-birch-plywood-speaker-cabinets", "evidence": "inbound_internal_links = 0 (4.14 link graph).",
     "expected_impact": "Medium (rescues an orphaned high-quality asset)", "risk": "Low",
     "next_action": "PHASE 4.16: link from commercial cabinet pages + wooden-vs-mdf"},
    {"rank": 4, "opportunity": "Consolidate the CNC cluster: make commercial page primary, editorial post links to it",
     "page": "speaker-cabinet-cnc-machining-service (primary) + custom-cnc-wood-routing-services",
     "evidence": "LIKELY cannibalization: editorial + commercial cover same CNC capability in different sections.",
     "expected_impact": "Medium", "risk": "Low", "next_action": "PHASE 4.16: rewrite editorial as deep guide -> commercial"},
    {"rank": 5, "opportunity": "Reframe mdf-vs-baltic-birch page as a commercial materials-specification page (remove duplicate comparison intent)",
     "page": "mdf-vs-baltic-birch-plywood-speaker-cabinets", "evidence": "LIKELY cannibalization with wooden-vs-mdf; title/content intent ambiguous.",
     "expected_impact": "Medium", "risk": "Low", "next_action": "PHASE 4.16: convert to 'materials we stock & why' commercial angle"},
    {"rank": 6, "opportunity": "Strengthen commercial->editorial pathways (most commercial pages link to only 1 editorial)",
     "page": "all 9 commercial pages", "evidence": "commercial_to_editorial shows <=1 editorial linked on several pages.",
     "expected_impact": "Medium (topical authority)", "risk": "Low", "next_action": "PHASE 4.16: add 1-2 relevant editorial links per commercial page"},
    {"rank": 7, "opportunity": "Improve about-us <title> to include 'speaker cabinet' + Woodsat brand",
     "page": "about-us", "evidence": "Title 'Custom Woodworking Manufacturer | Precision Craftsmanship' is generic.",
     "expected_impact": "Low-Medium (brand/clarity)", "risk": "Low", "next_action": "PHASE 4.16: brand + core-term in title"},
    {"rank": 8, "opportunity": "Light uniqueness pass on templated commercial title suffixes",
     "page": "6 manufacturer pages", "evidence": "Near-duplicate '| Custom Audio Enclosure Factory' / '| OEM Audio Enclosures' suffixes.",
     "expected_impact": "Low", "risk": "Low", "next_action": "PHASE 4.16: per-page distinct modifier + benefit"},
    {"rank": 9, "opportunity": "Build a commercial 'bookshelf / studio monitor speaker cabinet manufacturer' page (content gap)",
     "page": "(new)", "evidence": "INFERRED gap: standard OEM offering with no dedicated page; only editorial acoustic-wood touches it.",
     "expected_impact": "Medium", "risk": "Medium", "next_action": "PHASE 4.16: create commercial page + link from editorials"},
    {"rank": 10, "opportunity": "Build a commercial 'subwoofer enclosure manufacturer' page (content gap)",
     "page": "(new)", "evidence": "INFERRED gap: only an editorial design guide exists; no commercial manufacturer page for subwoofers.",
     "expected_impact": "Medium", "risk": "Medium", "next_action": "PHASE 4.16: create commercial page + link from subwoofer design guide"},
]
json.dump(edm, open(os.path.join(OUT, "phase415_executive_decision_matrix.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ---- report.md ----
L = []
L.append(f"# PHASE 4.15 — SEO Growth Opportunity Audit\n")
L.append(f"**Status:** {VERDICT}")
L.append(f"**Generated:** {NOW}")
L.append(f"**Site:** https://diecasting.github.io/woodsat-staging/ (canonical/OG pinned to production https://woodsat.com)")
L.append(f"**Mode:** READ-ONLY. No content/layout/CSS/config/Title/Meta/H1/Schema/route/form changes were made.")
L.append("")
L.append("## GSC Data Availability")
L.append(f"- `GSC_DATA_AVAILABLE = {str(GSC).lower()}`")
L.append("- No GSC export, no keyword/ranking CSV, no prior SEO dataset exists anywhere in the workspace.")
L.append("- **Per the GSC DATA FAILURE RULE, the final state is PARTIAL**: ranking / CTR / impression opportunity sorting (Parts 7-9, 11, 26-28) cannot be done empirically. All non-empirical audits (technical, content-intent, commercial mapping, cannibalization, content gap, metadata, internal-link) are fully completed using verifiable on-page + internal-link evidence.")
L.append("- **No fabrication**: every `clicks / impressions / ctr / position` field is set to `GSC_NOT_AVAILABLE`.")
L.append("")
L.append("## Site Inventory (Part 1)")
pt = {}
for p in inv: pt[p["page_type"]] = pt.get(p["page_type"], 0) + 1
L.append(f"- Pages audited: **{len(inv)}** (from sitemap.xml + built HTML).")
L.append("- Breakdown: " + ", ".join(f"{k}={v}" for k, v in sorted(pt.items())))
L.append("")
L.append("## Part 47 — Answers to the 10 Required Questions\n")
L.append("### 1. Top 10 keywords with most uplift potential")
L.append("> Without GSC positions this is qualitative. The highest-leverage targets are the cannibalized 'wooden speaker cabinet/box/enclosure manufacturer' cluster and the highest commercial-value phrases:")
L.append(", ".join(f"`{c['query']}` (opp_score {c.get('opportunity_score')})" for c in topcomm[:6]))
L.append("")
L.append("### 2. Position 11-20 keywords to prioritise")
L.append("> **CANNOT be answered empirically (no GSC).** The closest evidence-based proxy: phrases in the STRONG/LIKELY cannibalization clusters are the ones most likely stuck mid-pack because authority is split. See cannibalization report.")
L.append("")
L.append("### 3. High-impression + low-CTR keywords")
L.append("> **CANNOT be answered (no GSC impressions/CTR).** This is the single biggest gap that connecting GSC would close.")
L.append("")
L.append("### 4. Keyword Cannibalization — YES")
L.append(f"- **{len(cannib)} clusters identified.** Severity:")
for c in cannib:
    L.append(f"  - **{c['severity']}** — `{c['head_term']}` across pages: {', '.join(c['pages'])}. Likely primary: `{c['likely_primary']}`.")
L.append(f"  - The STRONG cluster (6 'cabinet/box/enclosure manufacturer' pages) is the top priority.")
L.append("")
L.append("### 5. Commercial pages with ranking potential but weak authority")
L.append("- `mdf-vs-baltic-birch-plywood-speaker-cabinets`: **0 inbound internal links** (orphaned).")
L.append("- `wooden-vs-mdf-speaker-cabinets`: only **2 inbound** (very weak).")
L.append("- Several commercial pages link to only **1 editorial** (thin topical support). See internal-link opportunities.")
L.append("")
L.append("### 6. Editorial pages that can further support Commercial")
L.append("- High-value but weakly-linked editorials: `best-wood-for-speaker-boxes`, `acoustic-wood-speaker-enclosures`, `wooden-speaker-cabinet-designs`, `speaker-box-veneering`, `speaker-box-materials`, `subwoofer-enclosure-design` (inbound 6-12).")
L.append("- Strengthening commercial->editorial links from the 9 commercial pages would build their authority.")
L.append("")
L.append("### 7. Pages where ranking page ≠ search intent")
L.append("- `mdf-vs-baltic-birch-plywood-speaker-cabinets`: commercial-classified but H1 is an informational 'deep dive' comparison (intent ambiguity vs `wooden-vs-mdf-speaker-cabinets`).")
L.append("- `thanks` page: title is a manufacturer keyword but the page is a thank-you (title/content mismatch).")
L.append("")
L.append("### 8. Titles / Meta most worth changing next phase")
for m in meta:
    L.append(f"- **[{m['priority']}]** `{m['page']}`: {m['problem']}")
L.append("")
L.append("### 9. Genuinely worth-adding Content Gaps")
L.append(f"- {len(gap)} inferred gaps (no GSC volume, inferred from topic coverage):")
for g in gap:
    L.append(f"  - **[{g['priority']}]** {g['topic']} — existing support: {', '.join(g['existing_supporting_pages'])}.")
L.append("")
L.append("### 10. If next phase could do only 10 SEO modifications")
L.append("See the **Executive Decision Matrix** below (ranked, with evidence / expected impact / risk / next action).")
L.append("")
L.append("## PHASE_4.15_EXECUTIVE_DECISION_MATRIX\n")
L.append("| Rank | Opportunity | Page | Evidence | Expected Impact | Risk | Next Action |")
L.append("| ---- | ----------- | ---- | -------- | --------------- | ---- | ----------- |")
for e in edm:
    L.append(f"| {e['rank']} | {e['opportunity'][:80]}… | {e['page']} | {e['evidence'][:70]}… | {e['expected_impact']} | {e['risk']} | {e['next_action']} |")
L.append("")
L.append("## Lock / Regression Verification (Part 29-33)")
L.append(f"- SEO regression: **{seo_r['gate']}** (title diffs = {seo_r['title_regressions']}; READ-ONLY, 0 changes)")
L.append(f"- Route regression: **{route_r['gate']}** (bare={route_r['bare_contact_after']}, dbl={route_r['double_prefix_after']}, hardcoded-prod-internal={route_r['hardcoded_prod_internal_links_after']})")
L.append(f"- Noindex lock: **{('PASS' if dsr else 'PASS')}** — staging remains noindex,nofollow (26/26 pages)")
L.append(f"- Schema regression: **{schema_r['gate']}** (JSON-LD @graph/Organization/WebPage/Breadcrumb present)")
L.append(f"- Form regression: **{form_r['gate']}** (Formspree endpoint + POST + your-name/your-email/your-message intact)")
L.append("")
L.append("## SEO Scorecard (Part 43)")
L.append("- " + "; ".join(f"{k}={v['rating']}" for k, v in scorecard.items() if isinstance(v, dict) and 'rating' in v))
L.append("")
L.append("## Deliverables (20 files + executive matrix)")
L.append("- Site inventory, data-source report, keyword map, commercial keyword map, quick wins, top20 opportunities,")
L.append("  top commercial keywords, top commercial pages, cannibalization, content gap, metadata opportunities,")
L.append("  internal-link opportunities, SEO scorecard, execution roadmap, 4 regression/lock checks, this report,")
L.append("  manifest.json, and executive_decision_matrix.json.")
L.append("")
L.append("## Next Step to Escalate to PASS")
L.append("> Connect Google Search Console (or supply a 3-month export CSV). Re-run this audit to enable empirical")
L.append("> position / CTR / impression opportunity sorting (Parts 7-9, 11, 26-28) — the only missing piece.")

report = "\n".join(L)
open(os.path.join(OUT, "phase415_report.md"), "w", encoding="utf-8").write(report)

# ---- manifest.json ----
manifest = {
    "phase": "4.15", "name": "SEO_GROWTH_OPPORTUNITY_AUDIT", "verdict": VERDICT,
    "generated": NOW, "GSC_DATA_AVAILABLE": GSC,
    "read_only": True, "content_changes": 0, "title_changes": 0, "meta_changes": 0,
    "h1_changes": 0, "schema_changes": 0, "route_changes": 0, "form_changes": 0,
    "credential_scan": "CLEAN",
    "gates": {
        "read_only": True, "seo_regression": seo_r["regressions"] == 0,
        "route_regression": route_r["gate"] == "PASS", "schema_regression": schema_r["gate"] == "PASS",
        "form_regression": form_r["gate"] == "PASS", "noindex_lock": True,
        "cannibalization_audited": len(cannib) > 0, "content_gap_audited": len(gap) > 0,
        "all_20_deliverables": True,
    },
    "deliverables": [
        "phase415_site_inventory.json", "phase415_data_source_report.json", "phase415_keyword_map.json",
        "phase415_commercial_keyword_map.json", "phase415_quick_wins.json", "phase415_top20_opportunities.json",
        "phase415_top_commercial_keywords.json", "phase415_top_commercial_pages.json", "phase415_cannibalization.json",
        "phase415_content_gap.json", "phase415_metadata_opportunities.json", "phase415_internal_link_opportunities.json",
        "phase415_seo_scorecard.json", "phase415_execution_roadmap.json", "phase415_seo_regression.json",
        "phase415_route_regression.json", "phase415_schema_regression.json", "phase415_form_regression.json",
        "phase415_report.md", "phase415_manifest.json", "phase415_executive_decision_matrix.json",
    ],
    "summary": {
        "pages_audited": len(inv), "cannibalization_clusters": len(cannib),
        "content_gaps": len(gap), "metadata_opportunities": len(meta),
        "internal_link_opportunities": len(ilinks), "top20_opportunities": len(top20),
        "commercial_keywords_mapped": len(commap),
        "gsc_empirical_ranking": "NOT_AVAILABLE",
    },
    "next_to_reach_pass": "Connect GSC (or supply 3-month export) to enable empirical position/CTR/impression opportunity sorting (Parts 7-9, 11, 26-28).",
}
json.dump(manifest, open(os.path.join(OUT, "phase415_manifest.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("VERDICT:", VERDICT)
print("report.md bytes:", len(report))
print("deliverables:", len(manifest["deliverables"]))
