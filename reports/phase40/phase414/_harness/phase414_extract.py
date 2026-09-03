#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 4.14 extraction + validation harness.

Maps sitemap.xml (production canonical URLs) -> built HTML files under public/,
parses per-page metadata / images / links / content fingerprint / SEO / schema /
form, validates images (local file existence + ranged GET for externals via proxy),
and writes reports/phase40/phase414/_harness/extracted.json.

Run:  PYTHON <this>   (expects CWD = repo root, public/ already built)
"""
import os, re, json, sys, subprocess, shutil
from bs4 import BeautifulSoup

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
PUBLIC = os.path.join(REPO, "public")
SITEMAP = os.path.join(PUBLIC, "sitemap.xml")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extracted.json")
PROXY = "http://localhost:1080"
STAGING_PREFIX = "/woodsat-staging/"

def staging_url_to_file(url):
    # url like https://woodsat.com/<slug>/ or https://woodsat.com/
    m = re.match(r"https://woodsat\.com/(.*)$", url)
    if not m:
        return None
    slug = m.group(1).strip("/")
    if slug == "":
        return os.path.join(PUBLIC, "index.html")
    return os.path.join(PUBLIC, slug, "index.html")

def load_sitemap_urls():
    with open(SITEMAP, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "lxml-xml")
    return [loc.get_text(strip=True) for loc in soup.find_all("loc")]

def resolve_local(src):
    """Return (local_path_or_None, kind) for an image src."""
    if not src:
        return None, "empty"
    if src.startswith("//"):
        src = "https:" + src
    if src.startswith("http://") or src.startswith("https://"):
        return src, "external"
    if src.startswith(STAGING_PREFIX):
        rel = src[len(STAGING_PREFIX):]
        return os.path.join(PUBLIC, rel), "local"
    if src.startswith("/"):
        # bare absolute path (e.g. /images/foo.jpg) - wrong staging prefix
        rel = src.lstrip("/")
        return os.path.join(PUBLIC, rel), "bare_local"
    # relative to page
    return os.path.join(PUBLIC, src), "relative"

def local_exists(p):
    return p and os.path.isfile(p)

def ranged_get(url):
    """Return HTTP status via ranged GET through proxy (HEAD returns 000 via proxy)."""
    try:
        out = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
             "-x", PROXY, "-r", "0-1024", "--max-time", "20", url],
            capture_output=True, text=True, timeout=40)
        return out.stdout.strip() or "000"
    except Exception as e:
        return "ERR:" + str(e)[:40]

def extract_images(soup, page_url):
    imgs = []
    # <img>
    for img in soup.find_all("img"):
        src = img.get("src") or ""
        resolved, kind = resolve_local(src)
        broken = False
        status = None
        if kind == "external":
            if os.environ.get("SKIP_EXTERNAL_IMG"):
                status = "200(skip-verify)"
                broken = False
            else:
                status = ranged_get(src)
                broken = status not in ("200", "206")
        elif kind in ("local", "bare_local", "relative"):
            exists = local_exists(resolved)
            broken = not exists
            status = "200" if exists else "404"
        else:
            broken = True
            status = "EMPTY"
        alt = img.get("alt")
        if alt is None:
            alt_cat = "MISSING"
        else:
            alt = alt.strip()
            alt_cat = "PRESENT"
        imgs.append({
            "page": page_url,
            "src": src,
            "resolved_url": resolved if isinstance(resolved, str) else "",
            "local_asset": isinstance(resolved, str) and kind != "external",
            "filename": os.path.basename(src) if src else "",
            "alt": alt if alt_cat == "PRESENT" else None,
            "alt_category": alt_cat,
            "width": img.get("width"),
            "height": img.get("height"),
            "loading": img.get("loading") or img.get("data-loading"),
            "decoding": img.get("decoding"),
            "kind": kind,
            "broken": broken,
            "status": status,
        })
    # <picture><source srcset>
    for pic in soup.find_all("picture"):
        for src in pic.find_all("source"):
            ss = src.get("srcset") or ""
            for part in re.split(r",\s*", ss):
                u = part.strip().split(" ")[0]
                if not u:
                    continue
                resolved, kind = resolve_local(u)
                broken = False
                status = None
                if kind == "external":
                    status = ranged_get(u); broken = status not in ("200", "206")
                elif kind in ("local", "bare_local", "relative"):
                    exists = local_exists(resolved); broken = not exists
                    status = "200" if exists else "404"
                imgs.append({
                    "page": page_url, "src": u,
                    "resolved_url": resolved if isinstance(resolved, str) else "",
                    "local_asset": isinstance(resolved, str) and kind != "external",
                    "filename": os.path.basename(u) if u else "",
                    "alt": None, "alt_category": "SOURCE",
                    "width": None, "height": None,
                    "loading": None, "decoding": None,
                    "kind": kind + ":source", "broken": broken, "status": status,
                })
    return imgs

def classify_links(soup, page_url):
    internal, external = [], []
    for a in soup.find_all("a", href=True):
        href = a.get("href").strip()
        text = a.get_text(strip=True)
        if href.startswith("#") or href == "" or href.lower().startswith("mailto:"):
            continue
        if href.startswith("javascript:"):
            continue
        if href.startswith("/") or href.startswith(STAGING_PREFIX) or href.startswith("http"):
            low = href.lower()
            if "woodsat.com" in low or "woodsat-staging" in low:
                if href.startswith(STAGING_PREFIX):
                    target_slug = href[len(STAGING_PREFIX):].strip("/")
                elif href.startswith("https://woodsat.com/"):
                    target_slug = href[len("https://woodsat.com/"):].strip("/")
                elif href.startswith("/"):
                    target_slug = href.strip("/")
                else:
                    target_slug = None
                internal.append({"href": href, "text": text, "target_slug": target_slug})
            else:
                if href.startswith("http"):
                    external.append({"href": href, "text": text})
                else:
                    # bare local path under site root but not woodsat -> still internal-ish
                    internal.append({"href": href, "text": text, "target_slug": href.strip("/")})
        else:
            # relative link
            internal.append({"href": href, "text": text, "target_slug": href})
    return internal, external

def get_meta(soup, name=None, prop=None):
    if name:
        t = soup.find("meta", attrs={"name": name})
    else:
        t = soup.find("meta", attrs={"property": prop})
    return t.get("content", "").strip() if t else None

def extract_page(url):
    fp = staging_url_to_file(url)
    rec = {"url": url, "file": fp, "exists": bool(fp and os.path.isfile(fp))}
    if not rec["exists"]:
        return rec
    with open(fp, encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")

    title = soup.title.get_text(strip=True) if soup.title else None
    h1 = soup.find_all("h1")
    h2 = soup.find_all("h2")
    h3 = soup.find_all("h3")
    h4 = soup.find_all("h4")
    rec.update({
        "title": title,
        "h1_count": len(h1), "h1_text": [h.get_text(strip=True) for h in h1],
        "h2_count": len(h2), "h2_text": [h.get_text(strip=True) for h in h2],
        "h3_count": len(h3), "h3_text": [h.get_text(strip=True) for h in h3],
        "h4_count": len(h4), "h4_text": [h.get_text(strip=True) for h in h4],
    })
    # word count from <main> if present else body
    main = soup.find("main") or soup.body or soup
    words = re.findall(r"\b[\w'-]+\b", main.get_text(" ", strip=True))
    rec["word_count"] = len(words)

    rec["images"] = extract_images(soup, url)
    rec["image_count"] = len([i for i in rec["images"] if not i["src"].endswith(".svg") or True])
    rec["image_count"] = sum(1 for i in rec["images"] if i["kind"] != "external:source")  # imgs only
    internal, external = classify_links(soup, url)
    rec["internal_links"] = internal
    rec["external_links"] = external
    rec["internal_link_count"] = len(internal)
    rec["external_link_count"] = len(external)

    # SEO
    rec["canonical"] = None
    can = soup.find("link", rel="canonical")
    if can:
        rec["canonical"] = can.get("href")
    rec["og_url"] = get_meta(soup, prop="og:url")
    rec["twitter_card"] = get_meta(soup, name="twitter:card")
    rec["robots"] = get_meta(soup, name="robots")
    rec["meta_description"] = get_meta(soup, name="description")
    rec["title_tag"] = title

    # JSON-LD
    ld = []
    for s in soup.find_all("script", type="application/ld+json"):
        txt = s.get_text(strip=True)
        ld.append(txt)
    rec["jsonld_raw"] = ld
    rec["jsonld_node_types"] = []
    for t in ld:
        for m in re.finditer(r'"@type"\s*:\s*"([^"]+)"', t):
            rec["jsonld_node_types"].append(m.group(1))
    rec["jsonld_has_graph"] = any('"@graph"' in t for t in ld)

    # Form (rfq)
    form = soup.find("form", class_=re.compile(r"rfq"))
    rec["form"] = None
    if form:
        rec["form"] = {
            "action": form.get("action"),
            "method": (form.get("method") or "").upper(),
            "field_names": [i.get("name") for i in form.find_all("input") if i.get("name")],
            "textarea_names": [t.get("name") for t in form.find_all("textarea") if t.get("name")],
        }

    # Content fingerprint
    rec["paragraphs"] = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
    rec["headings_text"] = ([h.get_text(strip=True) for h in h1] +
                            [h.get_text(strip=True) for h in h2] +
                            [h.get_text(strip=True) for h in h3] +
                            [h.get_text(strip=True) for h in h4])
    rec["list_items"] = [li.get_text(" ", strip=True) for li in soup.find_all("li")]
    tables = []
    for tbl in soup.find_all("table"):
        cells = [c.get_text(" ", strip=True) for c in tbl.find_all(["td", "th"])]
        tables.append(cells)
    rec["tables"] = tables
    rec["table_cell_count"] = sum(len(t) for t in tables)

    # route safety scans
    raw = html
    rec["route_bare_contact"] = bool(re.search(r'href="/contact/"', raw))
    rec["route_double_prefix"] = bool(re.search(r'/woodsat-staging/woodsat-staging/', raw))
    rec["route_hardcoded_prod"] = [a["href"] for a in soup.find_all("a", href=True)
                                   if a["href"].startswith("https://woodsat.com/")]
    return rec

def main():
    urls = load_sitemap_urls()
    pages = []
    for u in urls:
        pages.append(extract_page(u))
    # link graph
    slug_to_url = {}
    for p in pages:
        slug = p["url"].replace("https://woodsat.com/", "").strip("/")
        slug_to_url[slug] = p["url"]
    graph = {}
    for p in pages:
        slug = p["url"].replace("https://woodsat.com/", "").strip("/")
        inbound = []
        for q in pages:
            if q is p:
                continue
            for link in q.get("internal_links", []):
                tgt = link.get("target_slug")
                if tgt is not None and tgt == slug:
                    inbound.append({"from": q["url"], "text": link["text"]})
        targets = sorted(set(l.get("target_slug") for l in p.get("internal_links", []) if l.get("target_slug")))
        graph[slug] = {
            "url": p["url"],
            "outbound_links": len(p.get("internal_links", [])),
            "unique_internal_targets": targets,
            "inbound_links": len(inbound),
            "inbound_detail": inbound,
        }
    out = {"pages": pages, "graph": graph}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("extracted", len(pages), "pages ->", OUT)
    # quick summary
    imgs = [i for p in pages for i in p.get("images", [])]
    broken = [i for i in imgs if i["broken"]]
    print("images total:", len(imgs), "| broken:", len(broken))
    for b in broken:
        print("  BROKEN", b["page"], b["src"], b["status"])
    print("route bare /contact/:", sum(1 for p in pages if p.get("route_bare_contact")))
    print("route double prefix:", sum(1 for p in pages if p.get("route_double_prefix")))
    print("route hardcoded prod links:", sum(len(p.get("route_hardcoded_prod", [])) for p in pages))

if __name__ == "__main__":
    main()
