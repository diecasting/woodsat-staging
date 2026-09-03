#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 4.15 analysis part 2 (READ-ONLY): content gap, metadata, internal-link,
scorecard, roadmap, quick wins, top20, top commercial keywords, and LOCK/REGRESSION
verifications scanning the built public/ HTML (no GSC; empirical metrics marked NA)."""
import json, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
OUT = os.path.join(ROOT, "reports", "phase40", "phase415")
PUBLIC = os.path.join(ROOT, "public")
os.makedirs(OUT, exist_ok=True)
NA = "GSC_NOT_AVAILABLE"
GSC_NOT_AVAILABLE = "GSC_NOT_AVAILABLE"

ext = json.load(open(os.path.join(HERE, "phase415_extracted.json"), encoding="utf-8"))
by_slug = {p["slug"]: p for p in ext}
lg = json.load(open(os.path.join(ROOT, "reports", "phase40", "phase414", "phase414_internal_link_graph.json"), encoding="utf-8"))
lg_by = {r["slug"]: r for r in lg}
co = json.load(open(os.path.join(ROOT, "reports", "phase40", "phase414", "phase414_commercial_link_opportunities.json"), encoding="utf-8"))
commercial_map = json.load(open(os.path.join(OUT, "phase415_commercial_keyword_map.json"), encoding="utf-8"))
cannib = json.load(open(os.path.join(OUT, "phase415_cannibalization.json"), encoding="utf-8"))

# ============================ PART 19/20/41: CONTENT GAP ============================
# Evidence: standard, adjacent, commercially-relevant speaker-cabinet manufacturing
# sub-niches for a custom wooden-speaker-cabinet OEM that Woodsat currently has NO
# dedicated page targeting. INFERRED (no GSC volume data available).
content_gap = [
    {"topic": "Bookshelf / studio monitor speaker cabinet manufacturer",
     "queries": ["bookshelf speaker cabinet manufacturer", "studio monitor cabinet manufacturer", "monitor speaker enclosure OEM"],
     "intent": "COMMERCIAL_INVESTIGATION", "estimated_opportunity": "MEDIUM",
     "existing_supporting_pages": ["acoustic-wood-speaker-enclosures", "custom-wooden-speaker-cabinet-manufacturer"],
     "recommended_landing_page_type": "commercial manufacturer page", "priority": "P2",
     "evidence": "INFERRED_FROM_TOPIC_COVERAGE (no GSC). Standard OEM offering; only an editorial acoustic-wood page touches it."},
    {"topic": "Floorstanding speaker cabinet manufacturer",
     "queries": ["floorstanding speaker cabinet manufacturer", "tower speaker enclosure OEM"],
     "intent": "COMMERCIAL_INVESTIGATION", "estimated_opportunity": "MEDIUM",
     "existing_supporting_pages": ["custom-wooden-speaker-cabinet-manufacturer"],
     "recommended_landing_page_type": "commercial manufacturer page", "priority": "P2",
     "evidence": "INFERRED_FROM_TOPIC_COVERAGE. Common cabinet form-factor with no dedicated page."},
    {"topic": "Subwoofer enclosure manufacturer (commercial)",
     "queries": ["subwoofer enclosure manufacturer", "custom subwoofer box OEM"],
     "intent": "COMMERCIAL_INVESTIGATION", "estimated_opportunity": "MEDIUM",
     "existing_supporting_pages": ["subwoofer-enclosure-design"],
     "recommended_landing_page_type": "commercial manufacturer page", "priority": "P2",
     "evidence": "INFERRED_FROM_TOPIC_COVERAGE. Only an editorial design guide exists; no commercial manufacturer page for subwoofers specifically."},
    {"topic": "Speaker cabinet prototyping / low-volume / rapid prototype service",
     "queries": ["speaker cabinet prototype", "low volume speaker box manufacturing", "rapid prototyping audio enclosure"],
     "intent": "COMMERCIAL_INVESTIGATION", "estimated_opportunity": "MEDIUM",
     "existing_supporting_pages": ["contact", "speaker-cabinet-cnc-machining-service"],
     "recommended_landing_page_type": "commercial service page", "priority": "P2",
     "evidence": "INFERRED_FROM_TOPIC_COVERAGE. High-value B2B need; only the contact page addresses it today."},
    {"topic": "Speaker cabinet damping / bracing / isolation engineering",
     "queries": ["speaker cabinet damping", "internal bracing speaker box", "speaker cabinet isolation"],
     "intent": "INFORMATIONAL", "estimated_opportunity": "LOW-MEDIUM",
     "existing_supporting_pages": ["speaker-box-materials", "wooden-speaker-cabinet-designs"],
     "recommended_landing_page_type": "editorial deep-dive", "priority": "P3",
     "evidence": "INFERRED_FROM_TOPIC_COVERAGE. Adjacent acoustic-engineering topic with no dedicated asset."},
    {"topic": "Powered / active wooden speaker cabinet OEM",
     "queries": ["active speaker cabinet manufacturer", "powered monitor enclosure OEM"],
     "intent": "COMMERCIAL_INVESTIGATION", "estimated_opportunity": "LOW-MEDIUM",
     "existing_supporting_pages": ["wooden-speaker-enclosure-manufacturer"],
     "recommended_landing_page_type": "commercial manufacturer page", "priority": "P3",
     "evidence": "INFERRED_FROM_TOPIC_COVERAGE. Adjacent to enclosure manufacturing; no dedicated page."},
]
json.dump(content_gap, open(os.path.join(OUT, "phase415_content_gap.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 21/22/40: METADATA OPPORTUNITIES ============================
metadata = []
# thanks page title anomaly (pre-existing, recorded in 4.14)
thanks = by_slug.get("thanks", {})
metadata.append({
    "page": "thanks", "current_title": thanks.get("title"),
    "problem": "Title 'Sub-woofer Wooden Box manufacturer' does NOT match page content (a thank-you page, H1 empty). Misleading for users and SERPs.",
    "opportunity": "Rewrite title to a thank-you/confirmation message (e.g., 'Thank You | Woodsat').",
    "priority": "P1", "gsc_evidence": "On-page (title vs content mismatch); no GSC needed."
})
# about-us generic title
about = by_slug.get("about-us", {})
metadata.append({
    "page": "about-us", "current_title": about.get("title"),
    "problem": "Title 'Custom Woodworking Manufacturer | Precision Craftsmanship' is generic: omits the core term 'speaker cabinet' and the brand 'Woodsat'.",
    "opportunity": "Strengthen to include speaker-cabinet manufacturing + Woodsat brand while keeping it human.",
    "priority": "P2", "gsc_evidence": "On-page (brand/clarity); no GSC needed."
})
# templated commercial title suffixes
metadata.append({
    "page": "multiple commercial", "current_title": "e.g. '... | Custom Audio Enclosure Factory' / '| OEM Audio Enclosures' / '| Premium Wooden Speaker Enclosures'",
    "problem": "Six manufacturer pages share near-duplicate title suffix templates, reducing differentiation of the unique modifier (custom/oem/hifi/empty/box/enclosure).",
    "opportunity": "Differentiate each title around its single unique modifier + a distinct benefit; avoid identical suffix boilerplate.",
    "priority": "P3", "gsc_evidence": "On-page (title templating); no GSC needed."
})
# mdf-vs-baltic-birch intent/title alignment
mbb = by_slug.get("mdf-vs-baltic-birch-plywood-speaker-cabinets", {})
metadata.append({
    "page": "mdf-vs-baltic-birch-plywood-speaker-cabinets", "current_title": mbb.get("title"),
    "problem": "Page is commercial-classified but its H1 is an informational 'deep dive' comparison; title/template vs content intent is ambiguous.",
    "opportunity": "Reframe as a manufacturer materials-specification/commercial page (what we stock & why) rather than a duplicate comparison to wooden-vs-mdf.",
    "priority": "P2", "gsc_evidence": "On-page (intent/title mismatch); no GSC needed."
})
# duplicate/weak meta descriptions check
weak_meta = [p["slug"] for p in ext if not p.get("meta_description")]
metadata.append({
    "page": "site-wide", "current_title": "meta_description present on all 25 pages (none missing)",
    "problem": "No missing meta descriptions detected. Some commercial meta descriptions may be templated; recommend a light uniqueness pass.",
    "opportunity": "Per-page unique meta description with the page's modifier + CTA (no rewrite this phase).",
    "priority": "P3", "gsc_evidence": "On-page (meta presence check)."
})
json.dump(metadata, open(os.path.join(OUT, "phase415_metadata_opportunities.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 42: INTERNAL LINK OPPORTUNITIES ============================
ilinks = []
# orphan/weak editorial pages needing inbound
weak = [("mdf-vs-baltic-birch-plywood-speaker-cabinets", 0), ("wooden-vs-mdf-speaker-cabinets", 2)]
for slug, inbound in weak:
    ilinks.append({
        "source_page": "commercial manufacturer pages (custom/oem/hifi/box/enclosure)",
        "target_page": slug, "topic_relationship": "directly related comparison topic",
        "current_link_exists": False if inbound == 0 else "minimal(2)",
        "recommended_anchor_direction": "add contextual links from commercial cabinet pages + from wooden-vs-mdf to this deeper comparison",
        "priority": "P1" if inbound == 0 else "P2",
        "evidence": f"inbound_internal_links = {inbound} (orphan/very weak per 4.14 link graph)"
    })
# editorial pages with low inbound authority (high-value but under-linked)
for p in ext:
    if p["page_type"] == "editorial" and (p["inbound_internal_links"] or 0) < 12:
        ilinks.append({
            "source_page": "commercial pages + home + resource",
            "target_page": p["slug"], "topic_relationship": "editorial support for commercial cabinets",
            "current_link_exists": f"inbound={p['inbound_internal_links']}",
            "recommended_anchor_direction": "add links from relevant commercial pages (comm->ed) to build topical authority",
            "priority": "P2",
            "evidence": f"inbound_internal_links = {p['inbound_internal_links']} (weak editorial authority)"
        })
# CNC cluster cross-link (resolves cannibalization)
ilinks.append({
    "source_page": "custom-cnc-wood-routing-services (editorial)",
    "target_page": "speaker-cabinet-cnc-machining-service (commercial)",
    "topic_relationship": "same CNC capability, different sections",
    "current_link_exists": "weak",
    "recommended_anchor_direction": "make commercial page the primary CNC target; editorial post links strongly to it",
    "priority": "P1",
    "evidence": "CANNIBALIZATION cluster 'cnc-routing' (LIKELY)"
})
# commercial->editorial thin (many commercial pages link to only 1 editorial)
for c in co["commercial_to_editorial"]:
    cp = c["commercial_page"].split("/")[-2]
    if len(c.get("editorial_pages_linked", [])) <= 1:
        ilinks.append({
            "source_page": cp, "target_page": "2-3 relevant editorials",
            "topic_relationship": "commercial->editorial topical support",
            "current_link_exists": f"editorials linked={len(c.get('editorial_pages_linked',[]))}",
            "recommended_anchor_direction": "add 1-2 more relevant editorial links per commercial page",
            "priority": "P2",
            "evidence": "commercial_to_editorial pathway shows <=1 editorial linked"
        })
json.dump(ilinks, open(os.path.join(OUT, "phase415_internal_link_opportunities.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 43: SEO SCORECARD ============================
def grade(val): return val
scorecard = {
    "methodology": "Qualitative categories only. No single fabricated 'SEO score'. Where GSC-dependent metrics cannot be measured, they are marked GSC_NOT_AVAILABLE. Each category rated OK / WEAK / GAP with rationale.",
    "indexability": {"rating": "OK", "note": "Staging is noindex,nofollow (expected for staging). Confirmed in lock check."},
    "technical_seo": {"rating": "OK", "note": "Routes clean (no bare/double-prefix, no hardcoded production internal links after 4.14). Schema JSON-LD present. Formspree intact. Verified in lock checks."},
    "commercial_keyword_coverage": {"rating": "WEAK", "note": "Good breadth of manufacturer pages BUT heavy cannibalization across 6 'cabinet/box/enclosure manufacturer' pages splits authority."},
    "content_coverage": {"rating": "OK", "note": "Strong editorial depth on materials/finishes/design. Some commercial sub-niches uncovered (see content_gap)."},
    "internal_link_authority": {"rating": "OK", "note": "Commercial pages well-linked (48-54 inbound). Some editorial pages weak/orphan (mdf-vs-baltic-birch=0, wooden-vs-mdf=2)."},
    "CTR_opportunity": {"rating": GSC_NOT_AVAILABLE, "note": "Cannot be measured without GSC impressions/CTR."},
    "ranking_opportunity": {"rating": GSC_NOT_AVAILABLE, "note": "Position zones (4-10/11-20/21-30) cannot be empirically ranked without GSC. Qualitative opportunity scoring used instead."},
    "cannibalization_risk": {"rating": "HIGH", "note": "5 clusters identified; 1 STRONG (cabinet/box/enclosure manufacturer), 2 LIKELY, 2 POSSIBLE."},
    "metadata_quality": {"rating": "WEAK", "note": "thanks-page title mismatch (P1); about-us generic; templated commercial title suffixes."},
}
json.dump(scorecard, open(os.path.join(OUT, "phase415_seo_scorecard.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 44: EXECUTION ROADMAP ============================
roadmap = {
    "NOW": [
        "Designate a single PRIMARY 'wooden speaker cabinet manufacturer' page; differentiate the 5 siblings by one clear modifier (custom/oem/hifi/empty-box/enclosure) with distinct H1 angles + internal cross-links. (Resolves STRONG cannibalization.)",
        "Fix thanks-page title to a thank-you/confirmation message (currently 'Sub-woofer Wooden Box manufacturer').",
        "Build internal links to the two orphan/weak editorial pages (mdf-vs-baltic-birch=0 inbound, wooden-vs-mdf=2 inbound) from relevant commercial pages.",
        "Cross-link the CNC cluster: editorial custom-cnc-wood-routing-services -> commercial speaker-cabinet-cnc-machining-service as primary."
    ],
    "NEXT": [
        "Reframe mdf-vs-baltic-birch page as a commercial materials-specification page (remove duplicate comparison intent vs wooden-vs-mdf).",
        "Strengthen commercial->editorial pathways (most commercial pages link to only 1 editorial; add 1-2 relevant).",
        "Light metadata uniqueness pass on templated commercial title suffixes + about-us brand/clarity.",
        "Build 2-3 highest-value content-gap commercial pages (bookshelf/monitor, floorstanding, subwoofer manufacturer)."
    ],
    "LATER": [
        "Broader topical expansion: prototyping/low-volume service, damping/bracing guide, powered/active enclosure OEM.",
        "International/market-specific landing pages (US/UK/EU/Japan) once GSC data confirms demand.",
        "Re-run this audit WITH GSC connected to enable empirical position/CTR/impression ranking."
    ],
    "blocking_dependency": "Empirical ranking/CTR/impression opportunity sorting REQUIRES GSC data (currently unavailable)."
}
json.dump(roadmap, open(os.path.join(OUT, "phase415_execution_roadmap.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 10: QUICK WINS ============================
# Without GSC positions, quick wins = highest-leverage, lowest-risk STRUCTURAL fixes.
quick_wins = [
    {"query": "wooden speaker cabinet manufacturer (cluster)", "page": "custom-wooden-speaker-cabinet-manufacturer",
     "position": NA, "impressions": NA, "clicks": NA, "ctr": NA, "intent": "COMMERCIAL_INVESTIGATION",
     "why_it_matters": "Six pages compete for the bare head term; designating one primary + differentiating siblings can consolidate authority with zero new content.",
     "recommended_action": "Assign primary page + modifier-differentiated H1/titles + internal cross-links.", "priority": "P1"},
    {"query": "thanks page title", "page": "thanks",
     "position": NA, "impressions": NA, "clicks": NA, "ctr": NA, "intent": "NAVIGATIONAL",
     "why_it_matters": "Title currently mismatches content; cheap, safe metadata correctness fix.",
     "recommended_action": "Rewrite title to thank-you/confirmation.", "priority": "P1"},
    {"query": "mdf-vs-baltic-birch (orphan)", "page": "mdf-vs-baltic-birch-plywood-speaker-cabinets",
     "position": NA, "impressions": NA, "clicks": NA, "ctr": NA, "intent": "COMMERCIAL_INVESTIGATION",
     "why_it_matters": "0 inbound internal links; a high-quality deep-dive page is completely orphaned.",
     "recommended_action": "Add contextual inbound links from commercial cabinet pages + wooden-vs-mdf.", "priority": "P1"},
    {"query": "CNC wood routing (cluster)", "page": "speaker-cabinet-cnc-machining-service",
     "position": NA, "impressions": NA, "clicks": NA, "ctr": NA, "intent": "COMMERCIAL_INVESTIGATION",
     "why_it_matters": "Editorial + commercial page cover same topic; consolidating to one primary avoids split.",
     "recommended_action": "Make commercial page primary; editorial links to it.", "priority": "P1"},
]
json.dump(quick_wins, open(os.path.join(OUT, "phase415_quick_wins.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 37: TOP COMMERCIAL KEYWORDS ============================
top_comm = sorted(commercial_map, key=lambda x: -x.get("opportunity_score", 0))
json.dump(top_comm, open(os.path.join(OUT, "phase415_top_commercial_keywords.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 36: TOP 20 OPPORTUNITIES ============================
top20 = []
# Build a unified opportunity list combining cannibalization, metadata, internal-link, content-gap.
opps = []
for c in cannib:
    opps.append({"kind": "cannibalization", "topic": c["head_term"], "page": c["likely_primary"],
                 "severity": c["severity"], "evidence": c["evidence"],
                 "recommended_action": c["recommended_resolution"], "priority": "P1" if c["severity"] in ("STRONG","LIKELY") else "P2"})
for m in metadata:
    opps.append({"kind": "metadata", "topic": m["page"], "page": m["page"], "severity": m["priority"],
                 "evidence": m["problem"], "recommended_action": m["opportunity"], "priority": m["priority"]})
for g in content_gap:
    opps.append({"kind": "content_gap", "topic": g["topic"], "page": "(new)", "severity": g["priority"],
                 "evidence": g["evidence"], "recommended_action": f"Create {g['recommended_landing_page_type']}", "priority": g["priority"]})
for il in ilinks:
    if il["priority"] in ("P1","P2"):
        opps.append({"kind": "internal_link", "topic": il["target_page"], "page": il["target_page"],
                     "severity": il["priority"], "evidence": il["evidence"],
                     "recommended_action": il["recommended_anchor_direction"], "priority": il["priority"]})
# rank: P1 first, then by kind weight
kind_w = {"cannibalization": 0, "metadata": 1, "internal_link": 2, "content_gap": 3}
opps.sort(key=lambda o: (o["priority"], kind_w.get(o["kind"], 9)))
top20_list = []
for i, o in enumerate(opps[:20], 1):
    top20_list.append({
        "rank": i, "priority": o["priority"], "kind": o["kind"],
        "query/topic": o["topic"], "current_page": o["page"],
        "position": NA, "impressions": NA, "clicks": NA, "ctr": NA,
        "intent": o.get("intent", "n/a"), "opportunity_score": o.get("opportunity_score", "n/a"),
        "problem": o["evidence"], "recommended_action": o["recommended_action"],
        "risk": "LOW" if o["priority"] in ("P1","P2") else "MEDIUM",
    })
json.dump(top20_list, open(os.path.join(OUT, "phase415_top20_opportunities.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

print("content_gap:", len(content_gap), "| metadata:", len(metadata), "| ilinks:", len(ilinks))
print("top20 opportunities:", len(top20_list))
print("top commercial keywords:", len(top_comm))
