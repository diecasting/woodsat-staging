"""PHASE 4.17 structural extraction harness (READ-ONLY).

Extracts verifiable SITE-SIDE facts from the current build (public/) plus the
sitemap, and builds the production<->staging URL mapping used for analysis only.

This harness does NOT and CANNOT produce search-performance metrics
(clicks/impressions/CTR/position). Those require Google Search Console.
Where GSC is unavailable every metric field is emitted as null and flagged
GSC_NOT_AVAILABLE. No fabrication.
"""
import json
import os
import re
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
PUBLIC = os.path.join(ROOT, 'public')
OUT = os.path.join(ROOT, 'reports', 'phase40', 'phase417')

PROD_BASE = 'https://woodsat.com/'
STAGING_BASE = 'https://diecasting.github.io/woodsat-staging/'
STAGING_PREFIX = '/woodsat-staging/'

TAG_RE = re.compile(r'<[^>]+>')
SCRIPT_RE = re.compile(r'<(script|style)\b.*?</\1>', re.S | re.I)


def text_of(html):
    html = SCRIPT_RE.sub(' ', html)
    return re.sub(r'\s+', ' ', TAG_RE.sub(' ', html)).strip()


def attr(html, pattern):
    m = re.search(pattern, html, re.I)
    return m.group(1).strip() if m else None


def main():
    pages = {}
    # slug -> set of slugs it links to
    outbound = defaultdict(set)
    contextual = defaultdict(set)

    for dirpath, _dirnames, filenames in os.walk(PUBLIC):
        for fn in filenames:
            if fn != 'index.html':
                continue
            fp = os.path.join(dirpath, fn)
            rel = os.path.relpath(fp, PUBLIC).replace('\\', '/')
            slug = '' if rel == 'index.html' else rel[:-len('/index.html')]
            if '/' in slug:  # skip nested/paginated
                continue
            html = open(fp, encoding='utf-8', errors='replace').read()

            title = attr(html, r'<title>(.*?)</title>')
            canonical = attr(html, r'rel=["\']?canonical["\']?\s+href=["\']?([^"\'>\s]+)')
            if not canonical:
                canonical = attr(html, r'href=["\']?([^"\'>\s]+)["\']?\s+rel=["\']?canonical')
            desc = attr(html, r'<meta\s+name=["\']?description["\']?\s+content=["\']([^"\']*)["\']')
            if desc is None:
                desc = attr(html, r'<meta\s+content=["\']([^"\']*)["\']\s+name=["\']?description')
            robots = attr(html, r'<meta\s+name=["\']?robots["\']?\s+content=["\']([^"\']*)["\']')
            h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.S | re.I)
            h1 = text_of(h1s[0]) if h1s else None
            h2s = [text_of(x) for x in re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.S | re.I)]
            jsonld = len(re.findall(r'application/ld\+json', html, re.I))
            has_form = bool(re.search(r'formspree\.io/f/', html, re.I))
            words = len(text_of(html).split())

            pages[slug] = {
                'slug': slug,
                'staging_route': STAGING_PREFIX + (slug + '/' if slug else ''),
                'production_url': PROD_BASE + (slug + '/' if slug else ''),
                'title_tag': title,
                'title_tag_len': len(title) if title else None,
                'canonical': canonical,
                'meta_description': desc,
                'meta_description_len': len(desc) if desc else None,
                'meta_robots': robots,
                'h1': h1,
                'h1_count': len(h1s),
                'h2_count': len(h2s),
                'jsonld_blocks': jsonld,
                'has_contact_form': has_form,
                'word_count': words,
            }

            # ---- contextual vs chrome (nav/header/footer) link separation ----
            main_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.S | re.I)
            main_html = main_m.group(1) if main_m else ''
            chrome_html = html.replace(main_html, ' ') if main_html else html

            def targets(fragment):
                found = set()
                for href in re.findall(r'href=["\']?([^"\'>\s]+)', fragment, re.I):
                    tgt = None
                    if href.startswith(STAGING_PREFIX):
                        tgt = href[len(STAGING_PREFIX):]
                    elif href.startswith(PROD_BASE):
                        tgt = href[len(PROD_BASE):]
                    elif href.startswith('/') and not href.startswith('//'):
                        tgt = href[1:]
                    if tgt is None:
                        continue
                    tgt = tgt.split('#')[0].split('?')[0].strip('/')
                    if not tgt or '.' in tgt.split('/')[-1] or '/' in tgt:
                        continue
                    found.add(tgt)
                return found

            ctx = targets(main_html)
            chrome = targets(chrome_html)
            pages[slug]['contextual_outbound'] = sorted(x for x in ctx if x != slug)
            pages[slug]['chrome_outbound_count'] = len(chrome)
            outbound[slug] = ctx
            contextual[slug] = ctx

    inbound = defaultdict(set)
    for src, tgts in contextual.items():
        for t in tgts:
            if t != src:
                inbound[t].add(src)

    for slug, p in pages.items():
        p['contextual_inbound_pages'] = sorted(inbound.get(slug, []))
        p['contextual_inbound_count'] = len(inbound.get(slug, []))
        p['contextual_outbound_count'] = len(p.get('contextual_outbound', []))
        # legacy aliases retained for readability
        p['inbound_internal_count'] = p['contextual_inbound_count']
        p['outbound_internal_count'] = p['contextual_outbound_count']
        # every metric requiring GSC:
        p['clicks'] = None
        p['impressions'] = None
        p['ctr'] = None
        p['position'] = None
        p['gsc_note'] = 'GSC_NOT_AVAILABLE'

    # sitemap
    sm = os.path.join(PUBLIC, 'sitemap.xml')
    sitemap_urls = []
    if os.path.exists(sm):
        sitemap_urls = re.findall(r'<loc>(.*?)</loc>', open(sm, encoding='utf-8').read())

    result = {
        'phase': '4.17',
        'generated_from': 'public/ build @ baseline 366334a',
        'GSC_DATA_AVAILABLE': False,
        'page_count': len(pages),
        'sitemap_url_count': len(sitemap_urls),
        'sitemap_hosts': sorted({re.sub(r'^(https?://[^/]+).*', r'\1', u) for u in sitemap_urls}),
        'pages': pages,
        'sitemap_urls': sitemap_urls,
    }
    os.makedirs(os.path.join(OUT, '_harness'), exist_ok=True)
    with open(os.path.join(OUT, '_harness', 'phase417_structural_facts.json'), 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print('pages parsed:', len(pages))
    print('sitemap urls:', len(sitemap_urls), 'hosts:', result['sitemap_hosts'])
    print()
    print('=== commercial pages: CONTEXTUAL inbound/outbound/words ===')
    commercial = [
        'custom-wooden-speaker-cabinet-manufacturer',
        'oem-wooden-speaker-cabinet-manufacturer',
        'hifi-speaker-cabinet-manufacturer',
        'wooden-speaker-enclosure-manufacturer',
        'wooden-speaker-box-manufacturer',
        'custom-empty-wooden-speaker-cabinet-boxes-manufacturer',
        'speaker-cabinet-cnc-machining-service',
    ]
    for s in commercial:
        p = pages.get(s)
        if not p:
            print(f'  {s}: MISSING')
            continue
        print(f"  {s[:52]:<52} in={p['inbound_internal_count']:>3} out={p['outbound_internal_count']:>3} "
              f"words={p['word_count']:>5} h1={p['h1_count']} jsonld={p['jsonld_blocks']} form={p['has_contact_form']}")
    print()
    print('=== orphan check (inbound == 0) ===')
    orphans = [s for s, p in pages.items() if p['inbound_internal_count'] == 0 and s != '']
    print('orphans:', orphans if orphans else 'NONE')
    print()
    print('=== title tag lengths outside 30-65 ===')
    for s, p in sorted(pages.items()):
        L = p['title_tag_len']
        if L and (L < 30 or L > 65):
            print(f'  {s or "(home)"} -> {L} :: {p["title_tag"]}')


if __name__ == '__main__':
    main()
