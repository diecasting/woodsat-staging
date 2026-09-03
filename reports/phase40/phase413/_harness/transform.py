import re, sys, os

def read_parts(path):
    txt = open(path, encoding='utf-8').read()
    if txt.startswith('---'):
        m = re.match(r'^---\n(.*?)\n---\n', txt, re.DOTALL)
        fm = m.group(0)
        body = txt[m.end():]
    else:
        fm = ''
        body = txt
    return fm, body

SC_RE = re.compile(r'^\{\{<')
SCC_RE = re.compile(r'^\{\{/')
HEAD_RE = re.compile(r'^(#{1,6})\s+(.*)$')
LIST_RE = re.compile(r'^\s*[-*]\s+')
HR_SET = {'---', '***', '___'}

def parse_blocks(body):
    lines = body.split('\n')
    blocks = []
    i = 0; n = len(lines)
    while i < n:
        ln = lines[i]
        s = ln.strip()
        if s == '':
            i += 1; continue
        m = HEAD_RE.match(ln)
        if m:
            blocks.append(('h', len(m.group(1)), m.group(2).strip())); i += 1; continue
        if LIST_RE.match(ln):
            items = []
            while i < n and LIST_RE.match(lines[i]):
                items.append(re.sub(r'^\s*[-*]\s+', '', lines[i])); i += 1
            blocks.append(('list', items)); continue
        if s in HR_SET:
            blocks.append(('hr',)); i += 1; continue
        if s.startswith('>'):
            buf = []
            while i < n and lines[i].strip().startswith('>'):
                buf.append(lines[i]); i += 1
            blocks.append(('quote', buf)); continue
        if SC_RE.match(s) or SCC_RE.match(s):
            buf = []
            while i < n and (SC_RE.match(lines[i].strip()) or SCC_RE.match(lines[i].strip()) or (lines[i].strip()=='' and i+1<n and (SC_RE.match(lines[i+1].strip()) or SCC_RE.match(lines[i+1].strip()) or lines[i+1].lstrip().startswith('<')))):
                buf.append(lines[i]); i += 1
                if lines[i-1].strip()=='' and i<n and not (SC_RE.match(lines[i].strip()) or SCC_RE.match(lines[i].strip()) or lines[i].lstrip().startswith('<')):
                    break
            blocks.append(('sc', buf)); continue
        if s.startswith('<'):
            buf = []
            while i < n and lines[i].strip()!='' and lines[i].lstrip().startswith('<'):
                buf.append(lines[i]); i += 1
            blocks.append(('raw', buf)); continue
        buf = []
        while i < n and lines[i].strip()!='' and not HEAD_RE.match(lines[i]) and not LIST_RE.match(lines[i]) and not lines[i].strip().startswith('>') and not lines[i].lstrip().startswith('<') and not SC_RE.match(lines[i].strip()) and not SCC_RE.match(lines[i].strip()) and lines[i].strip() not in HR_SET:
            buf.append(lines[i]); i += 1
        blocks.append(('para', buf))
    return blocks

def is_table(lines):
    ne = [l for l in lines if l.strip()]
    if len(ne) < 4: return False
    short = sum(1 for l in ne if len(l.strip()) < 45)
    return (short / len(ne)) >= 0.6

def is_data_row(lines):
    # Strict orphan-table detector. The previous heuristic matched prose
    # paragraphs (e.g. a short intro line with no period) as fake comparison
    # tables, which mangled links into dead card titles. Real orphan tables have
    # terse cells, no sentence punctuation, and a tabular hint.
    ne = [l.strip() for l in lines if l.strip()]
    if not ne or len(ne) > 6:
        return False
    if any('<' in l for l in ne):
        return False
    if any(l.startswith('>') for l in ne):
        return False
    if not all(len(l) <= 48 for l in ne):
        return False
    if any(l.endswith(('.', '!', '?', ':')) for l in ne):
        return False
    # Require a regular ASCII digit (not a superscript like ³ in "kg/m³"), so a
    # column-header row that only "matches" via a unit superscript is NOT treated
    # as a data row and merged into the body.
    hint = any(('**' in l) or any(ch in '0123456789' for ch in l) for l in ne)
    if not hint:
        return False
    return True

def merge_tables(blocks):
    out = []
    i = 0; n = len(blocks)
    while i < n:
        b = blocks[i]
        if b[0] == 'para' and is_data_row(b[1]):
            run = [b]
            i += 1
            while i < n and blocks[i][0] == 'para' and is_data_row(blocks[i][1]):
                run.append(blocks[i]); i += 1
            if len(run) >= 2:
                merged = []
                for rb in run:
                    if merged: merged.append('')
                    merged.extend(rb[1])
                out.append(('table', merged))
            else:
                out.append(b)
        else:
            out.append(b); i += 1
    return out

def esc_title(t):
    t = t.strip().strip('*').strip('`').strip()
    t = t.replace('"', '&quot;')
    return t

def table_to_cards(lines, nest=False):
    groups = []
    cur = []
    for ln in lines:
        if ln.strip() == '':
            if cur: groups.append(cur); cur=[]
        else:
            cur.append(ln.strip())
    if cur: groups.append(cur)
    out = []
    out.append('{{< card-grid cols=2 >}}')
    # If the first group is a plain header (no bold label, no digits), render it
    # as a "Comparison Overview" card; otherwise treat every group as a data row.
    if groups and not any('**' in l or any(c.isdigit() for c in l) for l in groups[0]):
        out.append('{{< card title="Comparison Overview" >}}')
        for h in groups[0]:
            out.append('- ' + h)
        out.append('{{< /card >}}')
        data_groups = groups[1:]
    else:
        data_groups = groups
    for g in data_groups:
        title = g[0]
        out.append('{{< card title="%s" >}}' % esc_title(title))
        for line in g[1:]:
            out.append('- ' + line)
        out.append('{{< /card >}}')
    out.append('{{< /card-grid >}}')
    return out

def emit_block(b, bg='warm', nest=False):
    # NOTE: markdown content is emitted DIRECTLY inside the band (no <div class="measure"> wrapper).
    # Wrapping markdown in a raw <div> makes Goldmark treat it as a raw HTML block and it will NOT
    # render markdown (links/bold) inside. The 4.12 CSS already constrains .section > .container > p
    # to 760px, so the measure wrapper is both unnecessary and harmful (breaks links).
    out = []
    t = b[0]
    if t == 'para':
        txt = '\n'.join(b[1])
        if is_table(b[1]):
            out.extend(table_to_cards(b[1], nest=nest))
        else:
            out.append('{{< band bg="%s" >}}' % bg)
            out.append(txt)
            out.append('{{< /band >}}')
    elif t == 'list':
        out.append('{{< band bg="%s" >}}' % bg)
        out.append('{{< checklist cols=2 >}}')
        for it in b[1]:
            out.append('{{< checklist-item >}}' + it + '{{< /checklist-item >}}')
        out.append('{{< /checklist >}}')
        out.append('{{< /band >}}')
    elif t == 'quote':
        out.append('{{< band bg="%s" >}}' % bg)
        out.extend(b[1])
        out.append('{{< /band >}}')
    elif t == 'hr':
        out.append('{{< band bg="%s" >}}' % bg)
        out.append('---')
        out.append('{{< /band >}}')
    elif t == 'table':
        out.extend(table_to_cards(b[1]))
    elif t == 'raw':
        out.append('{{< band bg="%s" >}}' % bg)
        out.extend(b[1])
        out.append('{{< /band >}}')
    elif t == 'sc':
        joined = '\n'.join(b[1])
        if 'rfq-form' in joined:
            # The rfq-form partial renders its own <section id="rfq">. Emitting it
            # bare avoids nesting it inside a band <section>, and keeps the form
            # HTML out of markdownify (which could mangle block-level markup).
            out.append(joined)
        else:
            out.append('{{< band bg="%s" >}}' % bg)
            out.extend(b[1])
            out.append('{{< /band >}}')
    elif t == 'h':
        out.append(('#' * b[1]) + ' ' + b[2])
    return out

def emit_block_in_card(b):
    out = []
    t = b[0]
    if t == 'para':
        if is_table(b[1]):
            out.extend(table_to_cards(b[1], nest=True))
        else:
            out.append('\n'.join(b[1]))
    elif t == 'list':
        out.append('{{< checklist cols=2 >}}')
        for it in b[1]:
            out.append('{{< checklist-item >}}' + it + '{{< /checklist-item >}}')
        out.append('{{< /checklist >}}')
    elif t == 'quote':
        out.extend(b[1])
    elif t == 'raw':
        out.extend(b[1])
    elif t == 'sc':
        out.extend(b[1])
    elif t == 'table':
        out.extend(table_to_cards(b[1], nest=True))
    elif t == 'hr':
        out.append('---')
    elif t == 'h':
        out.append(('#' * b[1]) + ' ' + b[2])
    return out

def group_has_rfq(g):
    for b in g['blocks']:
        if b[0] in ('sc','raw') and any('rfq-form' in l for l in b[1]):
            return True
    return False

def group_has_h4(g):
    return any(b[0]=='h' and b[1]==4 for b in g['blocks'])

def emit_h4_faq(blocks):
    # Preserve ALL content. Leading non-H4 blocks (before the first H4) are
    # emitted as plain bands; each H4 starts a card and the following blocks
    # fill it. This guarantees no text (e.g. an intro sentence before the first
    # #### step) is silently dropped.
    out = []
    items = []
    cur = None
    leading = []
    seen_h4 = False
    for b in blocks:
        if b[0] == 'h' and b[1] == 4:
            seen_h4 = True
            if cur is not None:
                items.append(cur)
            cur = {'title': b[2], 'blocks': []}
        elif seen_h4:
            if cur is not None:
                cur['blocks'].append(b)
            else:
                leading.append(b)
        else:
            leading.append(b)
    if cur is not None:
        items.append(cur)
    for b in leading:
        out.extend(emit_block(b))
    if not items:
        return out
    out.append('{{< card-grid cols=1 >}}')
    for it in items:
        out.append('{{< card title="%s" >}}' % esc_title(it['title']))
        for b in it['blocks']:
            out.extend(emit_block_in_card(b))
        out.append('{{< /card >}}')
    out.append('{{< /card-grid >}}')
    return out

def transform(blocks):
    out = []
    blocks = merge_tables(blocks)
    # split into H2 sections
    intro = []
    sections = []
    cur_sec = None
    for b in blocks:
        if b[0]=='h' and b[1]==2:
            cur_sec = {'title': b[2], 'blocks': []}
            sections.append(cur_sec)
        elif cur_sec is not None:
            cur_sec['blocks'].append(b)
        else:
            intro.append(b)
    # intro
    if intro:
        for b in intro:
            out.extend(emit_block(b, bg='sand'))
    # sections
    for sec in sections:
        out.append('## ' + sec['title'])
        loose = []
        groups = []
        cur = None
        for b in sec['blocks']:
            if b[0]=='h' and b[1]==3:
                cur = {'title': b[2], 'blocks': []}
                groups.append(cur)
            elif cur is not None:
                cur['blocks'].append(b)
            else:
                loose.append(b)
        if any(b[0] == 'h' and b[1] == 4 for b in loose):
            # H4 steps that are direct children of an H2 section (no intervening
            # H3) become a clean FAQ-style card-grid while preserving any leading
            # intro sentence and every step's body text.
            out.extend(emit_h4_faq(loose))
        else:
            for b in loose:
                out.extend(emit_block(b))
        if groups:
            all_simple = all(not group_has_rfq(g) and not group_has_h4(g) for g in groups)
            if all_simple:
                cols = 3 if len(groups) >= 3 else 2
                out.append('{{< card-grid cols=%d >}}' % cols)
                for g in groups:
                    out.append('{{< card title="%s" >}}' % esc_title(g['title']))
                    for b in g['blocks']:
                        out.extend(emit_block_in_card(b))
                    out.append('{{< /card >}}')
                out.append('{{< /card-grid >}}')
            else:
                for g in groups:
                    if group_has_rfq(g):
                        out.append('### ' + g['title'])
                        for b in g['blocks']:
                            out.extend(emit_block(b, bg='sand'))
                    elif group_has_h4(g):
                        out.append('### ' + g['title'])
                        out.extend(emit_h4_faq(g['blocks']))
                    else:
                        out.append('{{< card-grid cols=1 >}}')
                        out.append('{{< card title="%s" >}}' % esc_title(g['title']))
                        for b in g['blocks']:
                            out.extend(emit_block_in_card(b))
                        out.append('{{< /card >}}')
                        out.append('{{< /card-grid >}}')
    return out

if __name__ == '__main__':
    inp = sys.argv[1]
    outp = sys.argv[2] if len(sys.argv) > 2 else None
    fm, body = read_parts(inp)
    blocks = parse_blocks(body)
    out_lines = transform(blocks)
    new_body = '\n'.join(out_lines) + '\n'
    new_txt = fm + new_body
    if outp:
        open(outp, 'w', encoding='utf-8').write(new_txt)
        print("WROTE", outp)
    else:
        sys.stdout.write(new_txt)
