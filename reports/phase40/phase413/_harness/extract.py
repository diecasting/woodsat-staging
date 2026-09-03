import re, os, json, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "public_before"
OUT = sys.argv[2] if len(sys.argv) > 2 else "reports/phase40/phase413/_harness/before_extract.json"

# target content files -> output dir (slug == filename without .md for these pages)
TARGETS = [
 "content/posts/best-wood-for-speaker-boxes.md",
 "content/posts/mdf-vs-baltic-birch-plywood-speaker-cabinets.md",
 "content/posts/wooden-vs-mdf-speaker-cabinets.md",
 "content/posts/custom-cnc-wood-routing-services.md",
 "content/posts/high-gloss-piano-lacquer-finishing-process-wood-speakers.md",
 "content/posts/acoustic-wood-speaker-enclosures.md",
 "content/posts/speaker-box-calculator.md",
 "content/posts/speaker-box-finishes.md",
 "content/posts/speaker-box-materials.md",
 "content/posts/speaker-box-veneering.md",
 "content/posts/speaker-cabinet-manufacturing.md",
 "content/posts/subwoofer-enclosure-design.md",
 "content/posts/wooden-speaker-cabinet-designs.md",
]

def strip_tags(html):
    # remove script/style
    html = re.sub(r'<script[\s\S]*?</script>', ' ', html, flags=re.I)
    html = re.sub(r'<style[\s\S]*?</style>', ' ', html, flags=re.I)
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&#39;', "'", text)
    text = re.sub(r'&quot;', '"', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract(html):
    title = re.search(r'<title>([\s\S]*?)</title>', html, re.I)
    desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([\s\S]*?)["\']', html, re.I)
    canonical = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([\s\S]*?)["\']', html, re.I)
    # all href (handle quoted OR minified unquoted values)
    hrefs = re.findall(r'href=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))', html)
    hrefs = [a or b or c for (a, b, c) in hrefs]
    # all id (handle quoted OR minified unquoted values)
    ids = re.findall(r'\bid=(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))', html)
    ids = [a or b or c for (a, b, c) in ids]
    # json-ld
    ld = re.findall(r'<script\s+type=["\']application/ld\+json["\'][\s\S]*?>([\s\S]*?)</script>', html, re.I)
    # h1/h2/h3 heading texts
    heads = re.findall(r'<h([1-6])[^>]*>([\s\S]*?)</h\1>', html, re.I)
    head_texts = [(int(l), strip_tags(h)) for l, h in heads]
    text = strip_tags(html)
    return dict(
        title=title.group(1).strip() if title else None,
        description=desc.group(1).strip() if desc else None,
        canonical=canonical.group(1).strip() if canonical else None,
        json_ld=[x.strip() for x in ld],
        hrefs=sorted(set(hrefs)),
        ids=sorted(set(ids)),
        headings=[{"level": l, "text": t} for l, t in head_texts],
        text=text,
    )

result = {}
for t in TARGETS:
    slug = os.path.basename(t)[:-3]
    p = os.path.join(ROOT, slug, "index.html")
    if not os.path.exists(p):
        result[slug] = {"ERROR": "missing " + p}
        continue
    html = open(p, encoding='utf-8', errors='replace').read()
    result[slug] = extract(html)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print("Wrote", OUT, "for", len(result), "pages")
for k, v in result.items():
    if "ERROR" in v:
        print("  ERR", k, v["ERROR"])
    else:
        print(f"  {k}: text={len(v['text'])} chars, hrefs={len(v['hrefs'])}, ids={len(v['ids'])}, h1={sum(1 for h in v['headings'] if h['level']==1)}")
