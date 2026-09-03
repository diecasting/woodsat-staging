import re, os

import glob
TARGETS = sorted(glob.glob("content/posts/*.md")) + sorted(glob.glob("content/pages/*.md"))
# exclude index and non-target pages
EXCLUDE = {"_index.md","about-us.md","contact.md","thanks.md",
 "custom-empty-wooden-speaker-cabinet-boxes-manufacturer.md",
 "custom-wooden-speaker-cabinet-manufacturer.md",
 "hifi-speaker-cabinet-manufacturer.md","oem-wooden-speaker-cabinet-manufacturer.md",
 "speaker-cabinet-cnc-machining-service.md","wooden-speaker-box-manufacturer.md",
 "wooden-speaker-enclosure-manufacturer.md"}
TARGETS = [t for t in TARGETS if os.path.basename(t) not in EXCLUDE]

def analyze(path):
    txt = open(path, encoding='utf-8').read()
    fm = ''
    body = txt
    if txt.startswith('---'):
        m = re.match(r'^---\n(.*?)\n---\n', txt, re.DOTALL)
        if m:
            fm = m.group(1); body = txt[m.end():]
    lines = body.split('\n')
    h2=[]; h3=[]; lists=0; links=set(); paras=0; orphan_candidates=[]
    i=0; n=len(lines)
    while i<n:
        line=lines[i]
        if line.strip()=='':
            i+=1; continue
        mh=re.match(r'^(#{2,6})\s+(.*)$',line)
        if mh:
            lvl=len(mh.group(1)); t=mh.group(2).strip()
            if lvl==2: h2.append(t)
            elif lvl==3: h3.append(t)
            i+=1; continue
        if re.match(r'^\s*[-*]\s+',line):
            while i<n and re.match(r'^\s*[-*]\s+',lines[i]): i+=1
            lists+=1; continue
        para=[]
        while i<n and lines[i].strip()!='' and not re.match(r'^(#{1,6})\s+',lines[i]) and not re.match(r'^\s*[-*]\s+',lines[i]):
            para.append(lines[i]); i+=1
        ptext='\n'.join(para)
        paras+=1
        for l in re.findall(r'\]\(([^)]+)\)', ptext): links.add(l)
        sub=[s for s in ptext.split('\n') if s.strip()]
        # exclude shortcode/html wrapper artifacts
        sub_real=[s for s in sub if not (s.strip().startswith('{{<') or s.strip().startswith('</') or s.strip().startswith('<div') or s.strip().startswith('{{'))]
        if len(sub_real)>=4:
            shorties=[s for s in sub_real if len(s)<40]
            if len(shorties)>=len(sub_real)*0.7 and not any('.' in s for s in sub_real[:3] if len(s)<40):
                orphan_candidates.append(sub_real)
        continue
    return dict(path=path, h2=h2, h3=h3, n_h2=len(h2), n_h3=len(h3),
                lists=lists, paras=paras, n_links=len(links),
                links=sorted(links), orphan=orphan_candidates)

for t in TARGETS:
    a=analyze(t)
    print("="*80)
    print(t)
    print(f"  H2={a['n_h2']} H3={a['n_h3']} lists={a['lists']} paras={a['paras']} links={a['n_links']} orphan_tables={len(a['orphan'])}")
    print("  H2:", a['h2'])
    if a['h3']: print("  H3:", a['h3'])
    for oc in a['orphan']:
        print("  ORPHAN candidate lines:", oc[:8], "..." if len(oc)>8 else "")
