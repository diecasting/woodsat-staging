#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 4.15 READ-ONLY extraction over the built public/ HTML.

Produces:
  phase415_site_inventory.json  (per-page inventory, Part 1 fields)
  phase415_extracted.json       (richer intermediate: full h1/h2/h3 text, meta, links)
No source files are read for writing; this only parses the already-built site.
"""
import json, os, re
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
PUBLIC = os.path.join(ROOT, "public")
OUT = os.path.join(ROOT, "reports", "phase40", "phase415")
os.makedirs(OUT, exist_ok=True)

# ---- 4.14 link graph for inbound/outbound (already computed) ----
lg_path = os.path.join(ROOT, "reports", "phase40", "phase414", "phase414_internal_link_graph.json")
link_graph = {}
if os.path.isfile(lg_path):
    for rec in json.load(open(lg_path, encoding="utf-8")):
        link_graph[rec["slug"]] = rec

# ---- sitemap -> slug -> built file ----
sm = open(os.path.join(PUBLIC, "sitemap.xml"), encoding="utf-8").read()
urls = re.findall(r"<loc>([^<]+)</loc>", sm)

def classify(slug, content_file):
    if slug == "":
        return "home"
    if "about-us" in slug: return "about"
    if slug == "contact": return "contact"
    if slug == "thanks": return "system_thanks"
    if slug == "resource": return "resource"
    if slug.startswith("posts/") or "/posts/" in content_file or content_file.endswith("posts"):
        return "editorial"
    return "commercial"

COMM_KW = ["manufacturer","supplier","factory","oem","odm","custom","wholesale",
           "production","manufacturing","cnc","service","quote","buy","cabinet",
           "enclosure","box","hifi","wooden speaker","wooden-speaker"]
INFO_KW = ["best","vs","guide","how","material","finish","veneering","design","calculator",
           "what","why","types","wood","mdf","baltic","birch","acoustic","subwoofer"]

def intent_score(text):
    t = text.lower()
    c = sum(t.count(k) for k in COMM_KW)
    i = sum(t.count(k) for k in INFO_KW)
    return c, i

inventory = []
extracted = []
for u in urls:
    slug = u.replace("https://woodsat.com/", "").strip("/")
    if slug == "":
        fpath = os.path.join(PUBLIC, "index.html")
        content_file = "content/_index.md"
    else:
        fpath = os.path.join(PUBLIC, slug, "index.html")
        # map slug -> content file best-effort
        content_file = f"content/pages/{slug}.md" if os.path.isfile(os.path.join(ROOT, "content", "pages", f"{slug}.md")) else f"content/posts/{slug}.md"
    if not os.path.isfile(fpath):
        continue
    html = open(fpath, encoding="utf-8", errors="replace").read()
    soup = BeautifulSoup(html, "lxml")
    # title
    title = (soup.title.string.strip() if soup.title and soup.title.string else "")
    # meta description
    mdesc = ""
    m = soup.find("meta", attrs={"name": "description"})
    if m: mdesc = m.get("content", "")
    # canonical
    canon = ""
    c = soup.find("link", attrs={"rel": "canonical"})
    if c: canon = c.get("href", "")
    # robots
    robots = ""
    r = soup.find("meta", attrs={"name": "robots"})
    if r: robots = r.get("content", "")
    # headings
    h1 = [h.get_text(strip=True) for h in soup.find_all("h1")]
    h2 = [h.get_text(strip=True) for h in soup.find_all("h2")]
    h3 = [h.get_text(strip=True) for h in soup.find_all("h3")]
    # body text word count (main content only to avoid nav/footer noise)
    body = soup.body or soup
    for tag in body.select("nav, footer, header, script, style"):
        tag.extract()
    text = body.get_text(" ", strip=True)
    word_count = len(text.split())
    # images
    imgs = soup.find_all("img")
    image_count = len(imgs)
    # internal links (same origin: /woodsat-staging/ or localhost staging)
    base = "/woodsat-staging/"
    internal_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if base in href or href.startswith("/woodsat-staging/") or href.startswith(base):
            internal_links.append(href)
    internal_link_count = len(internal_links)
    # page type + intent
    ptype = classify(slug, content_file)
    cscore, iscore = intent_score(title + " " + " ".join(h1+h2) + " " + mdesc)
    if ptype in ("commercial", "contact", "resource"):
        commercial_intent = "HIGH" if cscore >= 2 else "MEDIUM"
        informational_intent = "MEDIUM" if iscore >= 2 else "LOW"
    elif ptype == "editorial":
        informational_intent = "HIGH" if iscore >= 1 else "MEDIUM"
        commercial_intent = "MEDIUM" if cscore >= 3 else "LOW"
    else:
        commercial_intent = "LOW"; informational_intent = "LOW"
    # inbound/outbound from 4.14 graph
    g = link_graph.get(slug, {})
    inbound = g.get("inbound_links", None)
    outbound = g.get("outbound_links", None)
    rec = {
        "url": u, "slug": slug, "content_file": content_file, "page_type": ptype,
        "title": title, "meta_description": mdesc, "canonical": canon, "robots": robots,
        "h1": h1, "h2": h2, "h3": h3,
        "h1_count": len(h1), "h2_count": len(h2), "h3_count": len(h3),
        "word_count": word_count, "image_count": image_count,
        "internal_link_count": internal_link_count,
        "inbound_internal_links": inbound, "outbound_internal_links": outbound,
        "commercial_intent": commercial_intent, "informational_intent": informational_intent,
    }
    inventory.append(rec)
    extracted.append(rec)

with open(os.path.join(OUT, "phase415_site_inventory.json"), "w", encoding="utf-8") as f:
    json.dump(inventory, f, indent=2, ensure_ascii=False)
with open(os.path.join(HERE, "phase415_extracted.json"), "w", encoding="utf-8") as f:
    json.dump(extracted, f, indent=2, ensure_ascii=False)
print("site_inventory pages:", len(inventory))
print("page types:", {p["page_type"]: sum(1 for x in inventory if x["page_type"]==p["page_type"]) for p in inventory})
