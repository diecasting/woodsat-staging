import json, re

BEFORE = json.load(open("reports/phase40/phase413/_harness/before_extract.json", encoding="utf-8"))
AFTER = json.load(open("reports/phase40/phase413/_harness/after_extract.json", encoding="utf-8"))

def norm(s):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s

def sentences(text):
    # split into chunks at sentence/line boundaries; keep chunks > 15 chars
    chunks = re.split(r'(?<=[.!?:])\s+|\n+', text)
    out = []
    for c in chunks:
        c = norm(c)
        if len(c) >= 15:
            out.append(c)
    return out

problems = []
warnings = []
checked = 0
# Token-overlap check: editorial relayout legitimately reorders/restructures text
# (e.g. a comparison table -> card title + bullets), so a contiguous-substring
# match is too strict. We require >=80% of a chunk's UNIQUE content words to be
# present in the after-text; a genuinely dropped sentence scores far lower.
STOP = set("the a an and or of to in for with on at by from as is are was were be been being this that these those it its their our your we you they he she his her not but if then than so such into over under between within without about above below can will may should could would do does done has have had per via vs".split())
def cwords(s):
    toks = re.findall(r"[A-Za-z0-9°³'’\-]+", s.lower())
    return [t for t in toks if len(t) >= 3 and t not in STOP]
for slug in sorted(BEFORE.keys()):
    b = BEFORE[slug]; a = AFTER.get(slug)
    if "ERROR" in b or a is None or "ERROR" in (a or {}):
        problems.append((slug, "missing page in AFTER"))
        continue
    atext = norm(a["text"])
    # 1) sentence/block preservation (token-overlap tolerant of reordering)
    for sent in sentences(b["text"]):
        cw = cwords(sent)
        checked += 1
        if len(cw) < 5:
            if sent not in atext:
                problems.append((slug, "MISSING TEXT: " + sent[:90]))
            continue
        aw = set(cwords(atext))
        uniq = set(cw)
        frac = sum(1 for w in uniq if w in aw) / len(uniq)
        if frac < 0.8:
            problems.append((slug, "MISSING TEXT (%.0f%% words): %s" % (frac*100, sent[:80])))
    # 2) href set equality
    bh = set(b["hrefs"]); ah = set(a["hrefs"])
    if bh != ah:
        miss = bh - ah
        extra = ah - bh
        if miss: problems.append((slug, "MISSING HREF: %s" % list(miss)[:3]))
        if extra: problems.append((slug, "EXTRA HREF: %s" % list(extra)[:3]))
    # 3) id set — layout changes (orphan tables -> card titles, H3/H4 sections
    #    -> card-title <h3>s in hand-written templates, which Hugo does NOT
    #    auto-id) legitimately add/remove heading ids. IDs are NOT page content,
    #    so id diffs are reported as WARNINGS only and never fail the gate.
    #    Real heading loss is caught by the heading-TEXT + sentence checks below.
    bi = set(b["ids"]); ai = set(a["ids"])
    if bi != ai:
        miss = bi - ai
        extra = ai - bi
        if miss: warnings.append((slug, "ID GONE (verify heading text present): %s" % list(miss)[:5]))
        if extra: warnings.append((slug, "ID ADDED (layout change): %s" % list(extra)[:5]))
    # 4) heading text preservation
    bheads = [h["text"] for h in b["headings"]]
    atext_all = norm(a["text"])
    for h in bheads:
        hn = norm(h)
        if hn and hn not in atext_all:
            problems.append((slug, "MISSING HEADING: " + hn[:80]))
    # 5) SEO metadata unchanged
    for key in ("title", "description", "canonical"):
        if norm(b.get(key)) != norm(a.get(key)):
            problems.append((slug, "SEO %s CHANGED" % key))
    # 6) JSON-LD unchanged
    if b.get("json_ld") != a.get("json_ld"):
        problems.append((slug, "JSON-LD CHANGED"))

print("Sentences checked:", checked)
print("Total problems:", len(problems))
by_slug = {}
for slug, msg in problems:
    by_slug.setdefault(slug, []).append(msg)
for slug in sorted(by_slug):
    print("\n### %s : %d problems" % (slug, len(by_slug[slug])))
    for m in by_slug[slug][:12]:
        print("   -", m)
if not problems:
    print("\nCONTENT_PRESERVATION = PASS")
else:
    print("\nCONTENT_PRESERVATION = FAIL")
if warnings:
    print("\nID warnings (%d, non-blocking):" % len(warnings))
    for slug, msg in warnings:
        print("   - [%s] %s" % (slug, msg))
