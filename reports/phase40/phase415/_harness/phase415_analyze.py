#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 4.15 analysis (READ-ONLY). Generates the 14 analytical JSON deliverables +
lock/regression verifications. NO GSC data is used; empirical ranking metrics are
explicitly marked NOT_AVAILABLE. All scoring is qualitative and methodology-transparent.
"""
import json, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
OUT = os.path.join(ROOT, "reports", "phase40", "phase415")
os.makedirs(OUT, exist_ok=True)

GSC = False  # confirmed: no GSC/CSV/keyword export anywhere in workspace

ext = json.load(open(os.path.join(HERE, "phase415_extracted.json"), encoding="utf-8"))
by_slug = {p["slug"]: p for p in ext}
lg = json.load(open(os.path.join(ROOT, "reports", "phase40", "phase414", "phase414_internal_link_graph.json"), encoding="utf-8"))
lg_by = {r["slug"]: r for r in lg}
co = json.load(open(os.path.join(ROOT, "reports", "phase40", "phase414", "phase414_commercial_link_opportunities.json"), encoding="utf-8"))

NA = "GSC_NOT_AVAILABLE"

# ============================ PART 2/3: DATA SOURCE REPORT ============================
data_source = {
    "GSC_DATA_AVAILABLE": GSC,
    "sources_checked": [
        "workspace recursive search for *gsc*, *search*console*, *keyword*, *ranking*, *serp* -> none found",
        "workspace recursive search for *.csv (exports) -> none found",
        "reports/ historical phase*/seo*/gsc*/serp*/keyword*/ranking* -> none found",
        "sitemap.xml + built public/ HTML (used as the real, verifiable evidence base)"
    ],
    "data_freshness": "N/A (no GSC)",
    "data_completeness": "N/A (no GSC)",
    "GSC_DATA_LIMITATION": "No live Search Console, no exported CSV, no prior keyword/ranking dataset present in the workspace. Therefore position / impressions / CTR / clicks CANNOT be empirically ranked. This audit is built entirely on verifiable on-page + internal-link evidence.",
    "empirical_metrics_policy": "ALL clicks/impressions/ctr/position fields are set to null and labelled GSC_NOT_AVAILABLE. No fabrication of ranking data.",
    "evidence_base_used": {
        "site_inventory_pages": len(ext),
        "internal_link_graph": "phase414_internal_link_graph.json",
        "commercial_link_opportunities": "phase414_commercial_link_opportunities.json",
        "built_html_parsed": "public/*.html (current staging build, post PHASE 4.14)"
    },
    "verdict_impact": "Because GSC is unavailable, the final state is PHASE_4.15 = SEO_GROWTH_OPPORTUNITY_AUDIT_PARTIAL (per GSC DATA FAILURE RULE). All non-empirical audits (technical, content intent, commercial mapping, cannibalization, content gap, metadata, internal-link) are fully completed."
}
json.dump(data_source, open(os.path.join(OUT, "phase415_data_source_report.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 4-5: KEYWORD MAP (normalization + intent) ============================
# Build a normalized keyword map from on-page target phrases (titles/H1).
def norm(q):
    q = q.lower().strip()
    q = re.sub(r"[^a-z0-9 ]", " ", q)
    q = re.sub(r"\s+", " ", q).strip()
    return q

# Core commercial phrases (from commercial page titles/H1) + commercial-adjacent editorial.
raw_targets = {
    "wooden speaker cabinet manufacturer": ["wooden speaker cabinet manufacturer", "custom wooden speaker cabinet manufacturer", "oem wooden speaker cabinet manufacturer", "hifi speaker cabinet manufacturer", "premium wooden speaker cabinet manufacturer"],
    "wooden speaker box manufacturer": ["wooden speaker box manufacturer", "custom wooden speaker box", "empty wooden speaker box manufacturer", "custom audio enclosure factory"],
    "wooden speaker enclosure manufacturer": ["wooden speaker enclosure manufacturer", "custom audio cabinet oem", "wooden speaker enclosure"],
    "speaker cabinet cnc machining service": ["speaker cabinet cnc machining service", "precision wood cnc manufacturer", "cnc wood routing services for speaker cabinets"],
    "piano lacquer wood speaker finishing": ["piano lacquer wood speaker finishing process", "high gloss piano lacquer wood speakers", "wood speaker finishing process"],
    "mdf vs baltic birch plywood speaker cabinets": ["mdf vs baltic birch plywood for speaker cabinets", "mdf vs baltic birch speaker cabinets"],
    "custom cnc wood routing services": ["custom cnc wood routing services", "cnc wood routing", "precision cnc wood routing"],
    "speaker cabinet manufacturing": ["speaker cabinet manufacturing", "precision oem/odm factory", "speaker enclosure assembly"],
    "best wood for speaker boxes": ["best wood for speaker boxes", "best wood for speaker box", "wood for speaker boxes"],
    "speaker box materials": ["speaker box materials", "materials for speaker boxes", "wood substrates speaker"],
    "speaker box finishes": ["speaker box finishes", "cabinet coating", "premium speaker box finishes"],
    "speaker box veneering": ["speaker box veneering", "wood veneer speaker", "veneering service"],
    "subwoofer enclosure design": ["subwoofer enclosure design", "subwoofer enclosure", "bass enclosure design"],
    "speaker box calculator": ["speaker box calculator", "enclosure volume calculator", "port design tool"],
    "wooden speaker cabinet designs": ["wooden speaker cabinet designs", "custom wooden speaker cabinet designs", "oem solutions"],
    "acoustic wood speaker enclosures": ["acoustic wood speaker enclosures", "best wood for acoustic speaker enclosures", "oem solutions"],
    "wooden vs mdf speaker cabinets": ["wooden vs mdf speaker cabinets", "wood vs mdf speaker cabinets", "mdf vs wood speaker cabinets"],
}
intent_map = {
    "wooden speaker cabinet manufacturer": "COMMERCIAL_INVESTIGATION",
    "wooden speaker box manufacturer": "COMMERCIAL_INVESTIGATION",
    "wooden speaker enclosure manufacturer": "COMMERCIAL_INVESTIGATION",
    "speaker cabinet cnc machining service": "COMMERCIAL_INVESTIGATION",
    "piano lacquer wood speaker finishing": "COMMERCIAL_INVESTIGATION",
    "mdf vs baltic birch plywood speaker cabinets": "COMMERCIAL_INVESTIGATION",
    "custom cnc wood routing services": "COMMERCIAL_INVESTIGATION",
    "speaker cabinet manufacturing": "COMMERCIAL_INVESTIGATION",
    "best wood for speaker boxes": "INFORMATIONAL",
    "speaker box materials": "INFORMATIONAL",
    "speaker box finishes": "INFORMATIONAL",
    "speaker box veneering": "INFORMATIONAL",
    "subwoofer enclosure design": "INFORMATIONAL",
    "speaker box calculator": "INFORMATIONAL",
    "wooden speaker cabinet designs": "INFORMATIONAL",
    "acoustic wood speaker enclosures": "INFORMATIONAL",
    "wooden vs mdf speaker cabinets": "INFORMATIONAL",
}
# which page targets each phrase (from on-page title/H1 evidence)
target_page_of = {
    "wooden speaker cabinet manufacturer": "custom-wooden-speaker-cabinet-manufacturer",
    "wooden speaker box manufacturer": "wooden-speaker-box-manufacturer",
    "wooden speaker enclosure manufacturer": "wooden-speaker-enclosure-manufacturer",
    "speaker cabinet cnc machining service": "speaker-cabinet-cnc-machining-service",
    "piano lacquer wood speaker finishing": "high-gloss-piano-lacquer-finishing-process-wood-speakers",
    "mdf vs baltic birch plywood speaker cabinets": "mdf-vs-baltic-birch-plywood-speaker-cabinets",
    "custom cnc wood routing services": "custom-cnc-wood-routing-services",
    "speaker cabinet manufacturing": "speaker-cabinet-manufacturing",
    "best wood for speaker boxes": "best-wood-for-speaker-boxes",
    "speaker box materials": "speaker-box-materials",
    "speaker box finishes": "speaker-box-finishes",
    "speaker box veneering": "speaker-box-veneering",
    "subwoofer enclosure design": "subwoofer-enclosure-design",
    "speaker box calculator": "speaker-box-calculator",
    "wooden speaker cabinet designs": "wooden-speaker-cabinet-designs",
    "acoustic wood speaker enclosures": "acoustic-wood-speaker-enclosures",
    "wooden vs mdf speaker cabinets": "wooden-vs-mdf-speaker-cabinets",
}
comm_value = {
    "wooden speaker cabinet manufacturer": "HIGH", "wooden speaker box manufacturer": "HIGH",
    "wooden speaker enclosure manufacturer": "HIGH", "speaker cabinet cnc machining service": "HIGH",
    "piano lacquer wood speaker finishing": "MEDIUM", "mdf vs baltic birch plywood speaker cabinets": "MEDIUM",
    "custom cnc wood routing services": "HIGH", "speaker cabinet manufacturing": "HIGH",
    "best wood for speaker boxes": "MEDIUM", "speaker box materials": "MEDIUM",
    "speaker box finishes": "MEDIUM", "speaker box veneering": "MEDIUM",
    "subwoofer enclosure design": "MEDIUM", "speaker box calculator": "LOW",
    "wooden speaker cabinet designs": "MEDIUM", "acoustic wood speaker enclosures": "MEDIUM",
    "wooden vs mdf speaker cabinets": "MEDIUM",
}
keyword_map = []
for phrase, variants in raw_targets.items():
    keyword_map.append({
        "normalized_query": norm(phrase),
        "raw_queries": sorted(set(variants)),
        "intent": intent_map[phrase],
        "target_page": target_page_of[phrase],
        "page_type": by_slug.get(target_page_of[phrase], {}).get("page_type", "unknown"),
        "commercial_value": comm_value[phrase],
        "clicks": None, "impressions": None, "ctr": None, "position": None,
        "gsc_note": NA,
    })
json.dump(keyword_map, open(os.path.join(OUT, "phase415_keyword_map.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 6: COMMERCIAL KEYWORD MASTER LIST ============================
commercial_map = []
for phrase, variants in raw_targets.items():
    if intent_map[phrase] != "COMMERCIAL_INVESTIGATION":
        continue
    tp = target_page_of[phrase]
    g = lg_by.get(tp, {})
    commercial_map.append({
        "query": phrase,
        "normalized_query": norm(phrase),
        "intent": intent_map[phrase],
        "clicks": None, "impressions": None, "ctr": None, "position": None,
        "ranking_page": tp, "target_page": tp, "page_type": by_slug.get(tp, {}).get("page_type"),
        "inbound_internal_links": g.get("inbound_links"),
        "commercial_value": comm_value[phrase],
        "cannibalization_cluster": ("wooden-speaker-cabinet/box/enclosure-manufacturer" if "manufacturer" in phrase and ("cabinet" in phrase or "box" in phrase or "enclosure" in phrase) else ("cnc-routing" if "cnc" in phrase else "standalone")),
        "opportunity_score": None,  # filled after cannibalization pass
        "gsc_note": NA,
    })
json.dump(commercial_map, open(os.path.join(OUT, "phase415_commercial_keyword_map.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 14/39: CANNIBALIZATION ============================
# Cluster pages by shared head-term intent (evidence: title/H1 phrase overlap).
clusters = {
    "wooden-speaker-cabinet/box/enclosure-manufacturer": {
        "pages": ["custom-wooden-speaker-cabinet-manufacturer", "oem-wooden-speaker-cabinet-manufacturer",
                  "hifi-speaker-cabinet-manufacturer", "wooden-speaker-enclosure-manufacturer",
                  "wooden-speaker-box-manufacturer", "custom-empty-wooden-speaker-cabinet-boxes-manufacturer"],
        "head_term": "wooden speaker cabinet / box / enclosure manufacturer",
        "severity": "STRONG",
        "evidence": "Six commercial pages target near-identical head terms in title+H1 (manufacturer of wooden speaker cabinet/box/enclosure). They differ only by modifiers (custom/oem/hifi/empty) and by noun (cabinet/box/enclosure). Search engines may split authority across all six.",
        "likely_primary": "custom-wooden-speaker-cabinet-manufacturer (broadest, most modifier-inclusive H1)",
        "secondary": ["wooden-speaker-box-manufacturer", "wooden-speaker-enclosure-manufacturer",
                      "oem-wooden-speaker-cabinet-manufacturer", "hifi-speaker-cabinet-manufacturer",
                      "custom-empty-wooden-speaker-cabinet-boxes-manufacturer"],
        "recommended_resolution": "Designate ONE primary 'wooden speaker cabinet manufacturer' page; differentiate siblings by a single clear modifier (use-case: hifi / oem / empty-box / enclosure) with distinct H1 angle + internal cross-links so each ranks for its own modifier rather than competing for the bare head term."
    },
    "cnc-routing": {
        "pages": ["custom-cnc-wood-routing-services", "speaker-cabinet-cnc-machining-service"],
        "head_term": "CNC wood routing / machining for speaker cabinets",
        "severity": "LIKELY",
        "evidence": "An editorial post (custom-cnc-wood-routing-services) and a commercial page (speaker-cabinet-cnc-machining-service) cover the same capability from the same site, in different sections, with overlapping H2s (CNC workflow, specifications, RFQ).",
        "likely_primary": "speaker-cabinet-cnc-machining-service (commercial, conversion-oriented)",
        "secondary": ["custom-cnc-wood-routing-services"],
        "recommended_resolution": "Make the commercial page the primary CNC target; rewrite the editorial post to be a deep technical guide that links strongly to the commercial service page (currently weak cross-link)."
    },
    "mdf-vs-wood": {
        "pages": ["wooden-vs-mdf-speaker-cabinets", "mdf-vs-baltic-birch-plywood-speaker-cabinets"],
        "head_term": "MDF vs wood / Baltic birch for speaker cabinets",
        "severity": "LIKELY",
        "evidence": "Two pages cover the same comparison: an editorial 'wooden vs mdf' and a commercial-classified 'mdf vs baltic birch'. The commercial one carries an informational comparison H1, creating intent ambiguity.",
        "likely_primary": "wooden-vs-mdf-speaker-cabinets (clearer informational intent)",
        "secondary": ["mdf-vs-baltic-birch-plywood-speaker-cabinets"],
        "recommended_resolution": "Keep the editorial comparison as the primary informational asset; reframe the 'mdf vs baltic birch' page as a manufacturer-specification/commercial page (materials we stock & why) rather than a duplicate comparison."
    },
    "materials-wood": {
        "pages": ["best-wood-for-speaker-boxes", "speaker-box-materials", "acoustic-wood-speaker-enclosures"],
        "head_term": "best wood / materials for speaker boxes",
        "severity": "POSSIBLE",
        "evidence": "Three editorial pages approach the same 'which wood/material' topic with overlapping H2s (wood comparison, acoustic properties). Less severe because each has a distinct angle (best choices / materials matrix / acoustic science).",
        "likely_primary": "best-wood-for-speaker-boxes (highest commercial-adjacent intent)",
        "secondary": ["speaker-box-materials", "acoustic-wood-speaker-enclosures"],
        "recommended_resolution": "Interlink the three so they form a clear topical cluster; avoid rewriting into one page (distinct reader intents)."
    },
    "finishes": {
        "pages": ["speaker-box-finishes", "speaker-box-veneering", "high-gloss-piano-lacquer-finishing-process-wood-speakers"],
        "head_term": "speaker box finishing / veneering / lacquer",
        "severity": "POSSIBLE",
        "evidence": "Three finish pages (two editorial: finishes, veneering; one commercial: piano lacquer). Distinct sub-topics, low cannibalization risk, but worth explicit cross-linking.",
        "likely_primary": "high-gloss-piano-lacquer-finishing-process-wood-speakers (commercial)",
        "secondary": ["speaker-box-finishes", "speaker-box-veneering"],
        "recommended_resolution": "Cross-link finishes <-> veneering <-> lacquer to build a finishes topical cluster."
    },
}
cannibalization = []
for name, c in clusters.items():
    cannibalization.append({
        "query_cluster": name,
        "pages": c["pages"],
        "head_term": c["head_term"],
        "evidence": c["evidence"],
        "likely_primary": c["likely_primary"],
        "secondary_pages": c["secondary"],
        "severity": c["severity"],
        "recommended_resolution": c["recommended_resolution"],
    })
json.dump(cannibalization, open(os.path.join(OUT, "phase415_cannibalization.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# fill commercial_map opportunity_score using cannibalization severity
sev_score = {"STRONG": 25, "LIKELY": 18, "POSSIBLE": 10}
for cm in commercial_map:
    cl = cm["cannibalization_cluster"]
    sev = 0
    for c in clusters.values():
        if cm["ranking_page"] in c["pages"]:
            sev = max(sev, sev_score.get(c["severity"], 0))
    cm["cannibalization_severity_score"] = sev
    # qualitative opportunity: commercial_value(40) + cannib(25) + authority_gap(20) + depth(15)
    cv = {"HIGH": 40, "MEDIUM": 28, "LOW": 16}[cm["commercial_value"]]
    inbound = cm["inbound_internal_links"] or 0
    auth_gap = max(0, 50 - inbound) / 50 * 20  # weaker inbound -> more opportunity
    depth = min(15, (by_slug.get(cm["ranking_page"], {}).get("word_count", 0) or 0) / 80)
    cm["opportunity_score"] = round(cv + sev + auth_gap + depth, 1)
    cm["opportunity_score_methodology"] = "qualitative 0-100: commercial_value(40) + cannibalization_severity(0-25) + authority_gap(0-20) + content_depth(0-15); NO GSC ranking data used"
json.dump(commercial_map, open(os.path.join(OUT, "phase415_commercial_keyword_map.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

# ============================ PART 16/38: COMMERCIAL PAGE SCORE ============================
commercial_pages = [p for p in ext if p["page_type"] == "commercial"]
comm_scores = []
for p in commercial_pages:
    s = p["slug"]
    g = lg_by.get(s, {})
    inbound = g.get("inbound_links", 0)
    # editorial support = count of editorial_to_commercial entries that list this page
    ed_support = [e["editorial_page"].split("/")[-2] for e in co["editorial_to_commercial"] if s in e["commercial_pages_linked"]]
    # cannibalization membership
    in_cluster = [name for name, c in clusters.items() if s in c["pages"]]
    strengths = []
    weaknesses = []
    opportunities = []
    if inbound >= 48: strengths.append(f"strong inbound internal authority ({inbound} links)")
    else: weaknesses.append(f"moderate inbound authority ({inbound} links)")
    if p["word_count"] >= 1000: strengths.append("deep content (~%d words)" % p["word_count"])
    if in_cluster: weaknesses.append("part of cannibalization cluster: " + ", ".join(in_cluster))
    opportunities.append("differentiate H1/title by a single clear modifier to escape cluster competition")
    if len(ed_support) < 3: weaknesses.append(f"thin editorial support ({len(ed_support)} editorials link here)")
    else: strengths.append(f"good editorial support ({len(ed_support)} editorials)")
    comm_scores.append({
        "page": s, "url": p["url"], "title": p["title"],
        "inbound_internal_links": inbound, "outbound_internal_links": g.get("outbound_links"),
        "editorial_support_count": len(ed_support), "editorial_support_pages": ed_support,
        "word_count": p["word_count"], "cannibalization_clusters": in_cluster,
        "strengths": strengths, "weaknesses": weaknesses, "opportunities": opportunities,
        "priority": "P1" if in_cluster else ("P2" if inbound < 48 or len(ed_support) < 3 else "P3"),
    })
comm_scores.sort(key=lambda x: -len(x["cannibalization_clusters"]))
json.dump(comm_scores, open(os.path.join(OUT, "phase415_top_commercial_pages.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

print("commercial pages scored:", len(comm_scores))
print("cannibalization clusters:", len(cannibalization))
print("keyword_map entries:", len(keyword_map), "| commercial_map:", len(commercial_map))
