"""PHASE 4.17 report data generator (READ-ONLY).

Emits the machine-readable deliverables (URL mapping, query->URL map, opportunity
CSVs, matrices) from verified structural facts.

GSC_DATA_AVAILABLE = false for the Woodsat property, therefore EVERY
search-performance metric field is emitted as the literal string NOT_AVAILABLE
(CSV) or null (JSON). No metric is estimated, inferred, or fabricated.
"""
import csv
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, '..'))
FACTS = os.path.join(HERE, 'phase417_structural_facts.json')

NA = 'NOT_AVAILABLE'

facts = json.load(open(FACTS, encoding='utf-8'))
PAGES = facts['pages']

PROD = 'https://woodsat.com/'
STG = '/woodsat-staging/'

# ---------------------------------------------------------------- 1. URL MAP
mapping = []
for slug in sorted(PAGES):
    p = PAGES[slug]
    mapping.append({
        'slug': slug or '(home)',
        'production_url': p['production_url'],
        'staging_route': p['staging_route'],
        'canonical_in_build': p['canonical'],
        'canonical_host_is_production': bool(p['canonical'] and p['canonical'].startswith(PROD)),
        'in_sitemap': p['production_url'] in facts['sitemap_urls'],
        'meta_robots': p['meta_robots'],
        'mapping_status': 'MAPPED',
    })

unmapped = [u for u in facts['sitemap_urls']
            if u not in {m['production_url'] for m in mapping}]

url_map = {
    'phase': '4.17',
    'purpose': ('Production<->staging URL equivalence for ANALYSIS ONLY. '
                'Not written to production, not used to alter any route.'),
    'GSC_DATA_AVAILABLE': False,
    'production_base': PROD,
    'staging_base': 'https://diecasting.github.io/woodsat-staging/',
    'staging_path_prefix': STG,
    'normalization_rules': [
        'lowercase host',
        'force single trailing slash on directory-style routes',
        'strip #fragment',
        'strip ?query (no parameterised routes exist in this site)',
        'treat https://woodsat.com/<slug>/ == /woodsat-staging/<slug>/ as the same logical page',
        'www and non-www treated as the same logical host',
    ],
    'mapped_count': len(mapping),
    'unmapped_count': len(unmapped),
    'unmapped_urls': unmapped,
    'gsc_rows_mapped': NA,
    'gsc_urls_unmappable': NA,
    'note': ('No GSC rows exist for the Woodsat property, so no GSC URL could be '
             'mapped. The mapping table below is the complete site-side equivalence '
             'table, ready for use the moment GSC access is granted.'),
    'mapping': mapping,
}
json.dump(url_map, open(os.path.join(OUT, 'gsc_url_mapping.json'), 'w', encoding='utf-8'),
          indent=2, ensure_ascii=False)

# ------------------------------------------------- 2. QUERY UNIVERSE / OWNERS
# Query universe carried forward from PHASE 4.15/4.16 architecture.
# These are TARGET queries (intent definitions), NOT observed GSC queries.
QUERY_UNIVERSE = [
    # query, classification, intended owner slug, cluster
    ('woodsat', 'BRAND', '', 'brand'),
    ('woodsat speaker cabinet', 'BRAND', '', 'brand'),
    ('woodsat manufacturer', 'BRAND', 'about-us', 'brand'),
    ('wooden speaker cabinet manufacturer', 'COMMERCIAL', 'custom-wooden-speaker-cabinet-manufacturer', 'speaker cabinet manufacturer'),
    ('speaker cabinet manufacturer', 'COMMERCIAL', 'custom-wooden-speaker-cabinet-manufacturer', 'speaker cabinet manufacturer'),
    ('custom speaker cabinet manufacturer', 'COMMERCIAL', 'custom-wooden-speaker-cabinet-manufacturer', 'custom speaker cabinet'),
    ('speaker cabinet supplier', 'COMMERCIAL', 'custom-wooden-speaker-cabinet-manufacturer', 'speaker cabinet supplier'),
    ('wooden speaker cabinet supplier', 'COMMERCIAL', 'custom-wooden-speaker-cabinet-manufacturer', 'speaker cabinet supplier'),
    ('speaker cabinet factory', 'COMMERCIAL', 'custom-wooden-speaker-cabinet-manufacturer', 'speaker cabinet manufacturer'),
    ('oem speaker cabinet', 'OEM_ODM', 'oem-wooden-speaker-cabinet-manufacturer', 'OEM speaker cabinet'),
    ('oem wooden speaker cabinet manufacturer', 'OEM_ODM', 'oem-wooden-speaker-cabinet-manufacturer', 'OEM speaker cabinet'),
    ('speaker cabinet oem manufacturer', 'OEM_ODM', 'oem-wooden-speaker-cabinet-manufacturer', 'OEM speaker cabinet'),
    ('odm speaker enclosure', 'OEM_ODM', 'oem-wooden-speaker-cabinet-manufacturer', 'OEM speaker cabinet'),
    ('speaker cabinet cnc machining', 'SERVICE', 'speaker-cabinet-cnc-machining-service', 'CNC speaker cabinet'),
    ('speaker cabinet cnc machining service', 'SERVICE', 'speaker-cabinet-cnc-machining-service', 'CNC speaker cabinet'),
    ('cnc wood routing', 'SERVICE', 'custom-cnc-wood-routing-services', 'CNC speaker cabinet'),
    ('cnc speaker cabinet manufacturing', 'SERVICE', 'speaker-cabinet-cnc-machining-service', 'CNC speaker cabinet'),
    ('hifi speaker cabinet', 'PRODUCT_APPLICATION', 'hifi-speaker-cabinet-manufacturer', 'HIFI speaker cabinet'),
    ('hifi speaker cabinet manufacturer', 'PRODUCT_APPLICATION', 'hifi-speaker-cabinet-manufacturer', 'HIFI speaker cabinet'),
    ('audiophile speaker cabinet', 'PRODUCT_APPLICATION', 'hifi-speaker-cabinet-manufacturer', 'HIFI speaker cabinet'),
    ('wooden speaker enclosure manufacturer', 'COMMERCIAL', 'wooden-speaker-enclosure-manufacturer', 'speaker enclosure'),
    ('speaker enclosure manufacturer', 'COMMERCIAL', 'wooden-speaker-enclosure-manufacturer', 'speaker enclosure'),
    ('acoustic speaker enclosure', 'PRODUCT_APPLICATION', 'acoustic-wood-speaker-enclosures', 'speaker enclosure'),
    ('wooden speaker box manufacturer', 'COMMERCIAL', 'wooden-speaker-box-manufacturer', 'speaker box'),
    ('speaker box', 'PRODUCT_APPLICATION', 'wooden-speaker-box-manufacturer', 'speaker box'),
    ('speaker box manufacturer', 'COMMERCIAL', 'wooden-speaker-box-manufacturer', 'speaker box'),
    ('empty speaker box', 'PRODUCT_APPLICATION', 'custom-empty-wooden-speaker-cabinet-boxes-manufacturer', 'empty speaker box'),
    ('empty speaker cabinet manufacturer', 'COMMERCIAL', 'custom-empty-wooden-speaker-cabinet-boxes-manufacturer', 'empty speaker box'),
    ('blank speaker cabinet', 'PRODUCT_APPLICATION', 'custom-empty-wooden-speaker-cabinet-boxes-manufacturer', 'empty speaker box'),
    ('subwoofer cabinet', 'PRODUCT_APPLICATION', 'subwoofer-enclosure-design', 'subwoofer'),
    ('subwoofer enclosure design', 'INFORMATIONAL', 'subwoofer-enclosure-design', 'subwoofer'),
    ('bookshelf speaker cabinet', 'PRODUCT_APPLICATION', None, 'bookshelf speaker cabinet'),
    ('mdf speaker cabinet', 'MATERIALS', 'mdf-vs-baltic-birch-plywood-speaker-cabinets', 'MDF'),
    ('baltic birch speaker cabinet', 'MATERIALS', 'mdf-vs-baltic-birch-plywood-speaker-cabinets', 'Baltic birch'),
    ('plywood speaker cabinet', 'MATERIALS', 'mdf-vs-baltic-birch-plywood-speaker-cabinets', 'plywood'),
    ('mdf vs plywood speaker', 'INFORMATIONAL', 'wooden-vs-mdf-speaker-cabinets', 'MDF'),
    ('best wood for speaker boxes', 'INFORMATIONAL', 'best-wood-for-speaker-boxes', 'materials'),
    ('speaker cabinet materials', 'INFORMATIONAL', 'speaker-box-materials', 'materials'),
    ('speaker box materials', 'INFORMATIONAL', 'speaker-box-materials', 'materials'),
    ('speaker cabinet design', 'INFORMATIONAL', 'wooden-speaker-cabinet-designs', 'materials'),
    ('speaker cabinet construction', 'INFORMATIONAL', 'speaker-cabinet-manufacturing', 'materials'),
    ('speaker box calculator', 'INFORMATIONAL', 'speaker-box-calculator', 'materials'),
    ('speaker box veneering', 'INFORMATIONAL', 'speaker-box-veneering', 'materials'),
    ('speaker box finishes', 'INFORMATIONAL', 'speaker-box-finishes', 'materials'),
    ('piano lacquer speaker finish', 'INFORMATIONAL', 'high-gloss-piano-lacquer-finishing-process-wood-speakers', 'materials'),
    ('contact woodsat', 'NAVIGATIONAL', 'contact', 'brand'),
]


def owner_exists(slug):
    return slug is not None and slug in PAGES


rows = []
for q, cls, owner, cluster in QUERY_UNIVERSE:
    exists = owner_exists(owner)
    p = PAGES.get(owner) if exists else None
    rows.append({
        'query': q,
        'query_classification': cls,
        'query_cluster': cluster,
        'intended_owner_slug_phase416': (owner if owner is not None else 'NONE (content gap)'),
        'intended_owner_production_url': (p['production_url'] if p else 'NONE'),
        'owner_page_exists': 'YES' if exists else 'NO',
        'actual_gsc_landing_page': NA,
        'correct_owner': NA,
        'clicks': NA,
        'impressions': NA,
        'ctr': NA,
        'position': NA,
        'cannibalization_risk_gsc': NA,
        'cannibalization_risk_structural': (
            'RESOLVED_STRUCTURALLY_4.16' if cls in ('COMMERCIAL', 'OEM_ODM') and exists
            else ('N/A' if cls in ('BRAND', 'NAVIGATIONAL') else 'LOW')),
        'opportunity_class': ('CONTENT_GAP' if not exists else
                              ('BRAND' if cls == 'BRAND' else 'REQUIRES_GSC_TO_CLASSIFY')),
        'contextual_inbound_links': (p['contextual_inbound_count'] if p else 0),
        'owner_word_count': (p['word_count'] if p else 0),
        'evidence_class': 'STRUCTURAL_INFERRED (no GSC)',
    })

FIELDS = list(rows[0].keys())
with open(os.path.join(OUT, 'query_url_performance_map.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

# ------------------------------------------- 3. POSITION BUCKET CSVs (empty)
BUCKET_FIELDS = ['query', 'page', 'clicks', 'impressions', 'ctr', 'position',
                 'query_intent', 'intended_owner_phase416', 'correct_owner',
                 'cannibalization_risk', 'opportunity_class', 'internal_priority_score',
                 'data_status']
for name in ('position_4_10_opportunities.csv', 'position_11_20_opportunities.csv'):
    with open(os.path.join(OUT, name), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=BUCKET_FIELDS)
        w.writeheader()
        w.writerow({k: NA for k in BUCKET_FIELDS} | {
            'query': NA, 'data_status': 'GSC_DATA_AVAILABLE=false — no position data exists for the Woodsat property. Zero rows emitted rather than fabricated rows.'})

# ------------------------------------- 4. COMMERCIAL KEYWORD OPPORTUNITY MATRIX
MATRIX_FIELDS = ['query', 'intent', 'current_url', 'intended_owner', 'impressions',
                 'clicks', 'ctr', 'position', 'opportunity', 'evidence_class']
commercial_classes = ('COMMERCIAL', 'OEM_ODM', 'SERVICE', 'PRODUCT_APPLICATION', 'MATERIALS')
with open(os.path.join(OUT, 'commercial_keyword_opportunity_matrix.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=MATRIX_FIELDS)
    w.writeheader()
    for r in rows:
        if r['query_classification'] not in commercial_classes:
            continue
        w.writerow({
            'query': r['query'],
            'intent': r['query_classification'],
            'current_url': NA,
            'intended_owner': r['intended_owner_production_url'],
            'impressions': NA,
            'clicks': NA,
            'ctr': NA,
            'position': NA,
            'opportunity': ('CONTENT_GAP' if r['owner_page_exists'] == 'NO'
                            else 'REQUIRES_GSC_TO_CLASSIFY'),
            'evidence_class': 'STRUCTURAL_INFERRED',
        })

# ------------------------------------------------- 5. TOP 20 (structural only)
# Ranked by STRUCTURAL priority only. Explicitly NOT a search-performance ranking.
def structural_score(slug):
    """Transparent structural-only priority score (0-100).

    Components (no GSC input):
      commercial_role_weight   35
      authority_deficit        25  (fewer contextual inbound links = more headroom)
      serp_presentation_risk   25  (title/meta truncation risk)
      content_depth_headroom   15
    """
    p = PAGES.get(slug)
    if not p:
        return None, {}
    role_w = {
        'custom-wooden-speaker-cabinet-manufacturer': 35,
        'oem-wooden-speaker-cabinet-manufacturer': 30,
        'speaker-cabinet-cnc-machining-service': 28,
        'hifi-speaker-cabinet-manufacturer': 28,
        'wooden-speaker-enclosure-manufacturer': 26,
        'wooden-speaker-box-manufacturer': 26,
        'custom-empty-wooden-speaker-cabinet-boxes-manufacturer': 24,
    }.get(slug, 12)
    max_in = max(x['contextual_inbound_count'] for x in PAGES.values()) or 1
    authority_deficit = round(25 * (1 - p['contextual_inbound_count'] / max_in), 1)
    tl = p['title_tag_len'] or 0
    dl = p['meta_description_len'] or 0
    risk = 0
    if tl > 65:
        risk += 13
    if dl > 160:
        risk += 12
    depth = round(15 * (1 - min(p['word_count'], 1500) / 1500), 1)
    total = round(role_w + authority_deficit + risk + depth, 1)
    return total, {
        'commercial_role_weight': role_w,
        'authority_deficit': authority_deficit,
        'serp_presentation_risk': risk,
        'content_depth_headroom': depth,
    }


cands = []
for slug in PAGES:
    if slug in ('', 'thanks', 'contact', 'resource'):
        continue
    sc, comps = structural_score(slug)
    p = PAGES[slug]
    cands.append({
        'slug': slug,
        'production_url': p['production_url'],
        'structural_priority_score': sc,
        'components': comps,
        'contextual_inbound_count': p['contextual_inbound_count'],
        'title_tag_len': p['title_tag_len'],
        'meta_description_len': p['meta_description_len'],
        'word_count': p['word_count'],
        'clicks': None, 'impressions': None, 'ctr': None, 'position': None,
        'gsc_note': 'GSC_NOT_AVAILABLE',
    })
cands.sort(key=lambda x: -x['structural_priority_score'])

top20 = {
    'phase': '4.17',
    'GSC_DATA_AVAILABLE': False,
    'WARNING': ('This is NOT a list of search-performance opportunities. No GSC data '
                'exists for the Woodsat property, so query-level opportunities '
                '(position 4-10, 11-20, CTR gaps) CANNOT be produced. '
                'The list below is a STRUCTURAL readiness ranking only.'),
    'ranking_basis': 'STRUCTURAL_INFERRED',
    'score_formula': ('commercial_role_weight(35) + authority_deficit(25) + '
                      'serp_presentation_risk(25) + content_depth_headroom(15); '
                      'NO clicks/impressions/CTR/position input'),
    'is_google_ranking_probability': False,
    'is_traffic_prediction': False,
    'meaningful_query_level_opportunities_found': 0,
    'reason_zero': 'GSC_DATA_AVAILABLE=false (service account has no access to any Woodsat property)',
    'structural_candidates_count': len(cands),
    'structural_candidates': cands,
}
json.dump(top20, open(os.path.join(OUT, 'top_20_search_opportunities.json'), 'w', encoding='utf-8'),
          indent=2, ensure_ascii=False)

print('WROTE gsc_url_mapping.json          mapped=%d unmapped=%d' % (len(mapping), len(unmapped)))
print('WROTE query_url_performance_map.csv rows=%d' % len(rows))
print('WROTE position_4_10_opportunities.csv   (0 data rows)')
print('WROTE position_11_20_opportunities.csv  (0 data rows)')
print('WROTE commercial_keyword_opportunity_matrix.csv')
print('WROTE top_20_search_opportunities.json  structural_candidates=%d' % len(cands))
print()
print('=== structural priority top 12 ===')
for c in cands[:12]:
    print(f"  {c['structural_priority_score']:>5}  {c['slug'][:56]:<56} in={c['contextual_inbound_count']:>2} "
          f"tlen={c['title_tag_len']} dlen={c['meta_description_len']}")
print()
print('=== content gaps (no owner page) ===')
for r in rows:
    if r['owner_page_exists'] == 'NO':
        print('  ', r['query'], '->', r['intended_owner_slug_phase416'])
