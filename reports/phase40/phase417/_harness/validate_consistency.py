#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 4.17 consistency validation: top_20_search_opportunities.json <-> .md
and internal-link model integrity. No GSC dependency; structural checks only."""
import json, os, re, sys

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQ_FIELDS = ["id","internal_link_opportunity","scope","target_url","target_owner_4_16",
              "source_pages","instance_count","anchor_type","contextual_reason",
              "implementation_status","evidence_type","evidence","relates_to",
              "gsc_validated","requires_gsc"]

tp_json = os.path.join(OUT, "top_20_search_opportunities.json")
tp_md = os.path.join(OUT, "top_20_search_opportunities.md")
intl_md = os.path.join(OUT, "internal_link_opportunities.md")

errors = []
warnings = []

data = json.load(open(tp_json, encoding="utf-8"))
ilos = data.get("internal_link_opportunities", [])
if not ilos:
    errors.append("JSON: internal_link_opportunities array missing/empty")

# 1) per-ILO field integrity
for x in ilos:
    for f in REQ_FIELDS:
        if f not in x:
            errors.append("ILO %s: missing field %s" % (x.get("id","?"), f))
    if x.get("evidence_type") != "STRUCTURAL_INTERNAL_LINK":
        errors.append("ILO %s: evidence_type not STRUCTURAL_INTERNAL_LINK (%s)" % (x.get("id"), x.get("evidence_type")))
    if x.get("gsc_validated") is not False:
        errors.append("ILO %s: gsc_validated must be False" % x.get("id"))
    if not x.get("source_pages"):
        errors.append("ILO %s: source_pages empty" % x.get("id"))
    if x.get("instance_count", 0) <= 0:
        errors.append("ILO %s: instance_count must be >0" % x.get("id"))

# 2) re-pointing totals reconcile. The legacy body-copy link set is exactly
#    ILO-1..5 = 13+8+2+2+3 = 28. ILO-6 (28) is the SAME set served as a
#    server-side redirect safety net (not additive); ILO-7 (6) is a SEPARATE
#    handoff-gap set. So do not sum all seven.
legacy_repoint = sum(x["instance_count"] for x in ilos if x["id"] in ("ILO-1","ILO-2","ILO-3","ILO-4","ILO-5"))
misrouted = sum(x["instance_count"] for x in ilos if x["id"] in ("ILO-1","ILO-2","ILO-3","ILO-4"))
correct = sum(x["instance_count"] for x in ilos if x["id"]=="ILO-5")
ilo6 = next(x["instance_count"] for x in ilos if x["id"]=="ILO-6")
ilo7 = next(x["instance_count"] for x in ilos if x["id"]=="ILO-7")
if legacy_repoint != 28:
    errors.append("Legacy re-point set (ILO-1..5)=%d, expected 28" % legacy_repoint)
if misrouted != 25:
    errors.append("Misrouted (ILO-1..4)=%d, expected 25" % misrouted)
if correct != 3:
    errors.append("Already-correct (ILO-5)=%d, expected 3" % correct)
if ilo6 != 28:
    errors.append("ILO-6 server-net count=%d, expected 28 (same set as legacy)" % ilo6)
if ilo7 != 6:
    errors.append("ILO-7 handoff-gap count=%d, expected 6" % ilo7)

# 3) OPP-1/OPP-2 linked to ILO refs
for opp in data.get("site_wide_structural_opportunities", []):
    if opp["id"] == "OPP-1" and "internal_link_opportunity_refs" not in opp:
        errors.append("OPP-1 missing internal_link_opportunity_refs")
    if opp["id"] == "OPP-2" and "internal_link_opportunity_refs" not in opp:
        errors.append("OPP-2 missing internal_link_opportunity_refs")

# 4) JSON <-> MD field match
md = open(tp_md, encoding="utf-8").read()
md2 = open(intl_md, encoding="utf-8").read()
for x in ilos:
    iid = x["id"]
    if iid not in md:
        errors.append("MD(top20): %s absent" % iid)
    if iid not in md2:
        errors.append("MD(internal_link): %s absent" % iid)
    # target url (strip trailing note for ILO-6/7)
    tgt = x["target_url"]
    if tgt.startswith("see") or tgt.startswith("per"):
        pass
    else:
        if tgt not in md:
            errors.append("MD(top20): %s target_url %s absent" % (iid, tgt))
    # anchor_type must appear verbatim
    if x["anchor_type"] not in md:
        errors.append("MD(top20): %s anchor_type %r absent" % (iid, x["anchor_type"]))
    # implementation_status verbatim
    if x["implementation_status"] not in md:
        errors.append("MD(top20): %s implementation_status %r absent" % (iid, x["implementation_status"]))
    # instance_count numeric present
    if str(x["instance_count"]) not in md:
        errors.append("MD(top20): %s instance_count %d absent" % (iid, x["instance_count"]))

# 5) banner that nothing is GSC-validated
if "none GSC-validated" not in md and "None is GSC-validated" not in md and "not GSC-validated" not in md:
    warnings.append("MD(top20): GSC-non-validation banner not detected")

# 6) contextual-only principles present in MD
for principle_kw in ["sitewide","exact-match","4.16 commercial intent ownership","never a target","empty-box"]:
    if principle_kw.lower() not in md.lower():
        warnings.append("MD(top20): contextual-only principle keyword %r not present" % principle_kw)

print("=== VALIDATION RESULT ===")
print("ILO count:", len(ilos))
print("Legacy re-point set (ILO-1..5):", legacy_repoint, "| misrouted (ILO-1..4):", misrouted, "| correct (ILO-5):", correct)
print("ILO-6 server-net:", ilo6, "| ILO-7 handoff gaps:", ilo7)
print("Errors:", len(errors))
for e in errors:
    print("  ERROR:", e)
print("Warnings:", len(warnings))
for w in warnings:
    print("  WARN:", w)
ok = (len(errors) == 0)
print("CONSISTENCY:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
