#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 4.14 visual regression sweep via Playwright.

Serves public/ at http://localhost:8137/woodsat-staging/ and loads every page at
1440/1024/768/390/375, recording horizontal overflow + broken images + captures.
Writes visual_results.json + screenshots.
"""
import os, json, subprocess, shutil, sys
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
PUBLIC = os.path.join(ROOT, "public")
PREVIEW_ROOT = os.path.join(ROOT, "reports", "phase40", "phase414", "_harness", "preview_root")
STAGING_DIR = os.path.join(PREVIEW_ROOT, "woodsat-staging")
SHOT_DIR = os.path.join(ROOT, "reports", "phase40", "phase414", "screenshots")
OUT = os.path.join(ROOT, "reports", "phase40", "phase414", "_harness", "visual_results.json")
PORT = 8137
BASE = f"http://localhost:{PORT}/woodsat-staging/"

VIEWPORTS = [1440, 1024, 768, 390, 375]

def setup_preview():
    if os.path.isdir(STAGING_DIR):
        shutil.rmtree(STAGING_DIR)
    shutil.copytree(PUBLIC, STAGING_DIR)
    os.makedirs(SHOT_DIR, exist_ok=True)

def serve():
    # serve from PREVIEW_ROOT so /woodsat-staging/ resolves
    p = subprocess.Popen(["/d/hugo/hugo" if False else "python",
                          "-m", "http.server", str(PORT), "--directory", PREVIEW_ROOT],
                         cwd=PREVIEW_ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return p

def main():
    import time
    NODE = r"C:/Users/anson/.workbuddy/binaries/node/versions/22.22.2/node.exe"
    NMOD = r"C:/Users/anson/.workbuddy/binaries/node/workspace/node_modules"
    setup_preview()
    srv = serve()
    time.sleep(1.5)
    # read urls from sitemap (production canonical -> staging path)
    import re
    with open(os.path.join(PUBLIC, "sitemap.xml"), encoding="utf-8") as f:
        sm = f.read()
    urls = re.findall(r"<loc>([^<]+)</loc>", sm)
    # build list of (slug_path)
    pages = []
    for u in urls:
        slug = u.replace("https://woodsat.com/", "").strip("/")
        pages.append(slug)  # "" for home
    # write a small node script
    script = r'''
    const { chromium } = require('playwright');
    (async () => {
      const base = process.env.BASE;
      const shots = process.env.SHOT_DIR;
      const vws = JSON.parse(process.env.VWS);
      const pages = JSON.parse(process.env.PAGES);
      const browser = await chromium.launch();
      const results = [];
      for (const slug of pages) {
        const url = base + slug;
        for (const vw of vws) {
          const ctx = await browser.newContext({ viewport: { width: vw, height: 900 } });
          const page = await ctx.newPage();
          // Block external hosts so layout/overflow checks never hang on wp-content/Formspree.
          await page.route('**/*', route => {
            const u = route.request().url();
            if (u.startsWith(base)) return route.continue();
            return route.abort();
          });
          try {
            await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });
          } catch(e) { /* continue */ }
          await page.waitForTimeout(400);
          const metrics = await page.evaluate(() => {
            const de = document.documentElement;
            const overflow = de.scrollWidth - de.clientWidth;
            const offenders = [];
            if (overflow > 0) {
              const all = document.querySelectorAll('*');
              for (const el of all) {
                const r = el.getBoundingClientRect();
                if (r.right > window.innerWidth + 1 && r.width > 0) {
                  offenders.push((el.tagName||'').toLowerCase() + (el.className?('.'+String(el.className).split(' ')[0]):''));
                  if (offenders.length >= 8) break;
                }
              }
            }
            const imgs = Array.from(document.images);
            const brokenImgs = imgs.filter(i => !i.complete || i.naturalWidth === 0).map(i => i.currentSrc || i.src);
            return { overflow, offenders, brokenImgs };
          });
          const name = (slug || 'home') + '_' + vw + '.png';
          try { await page.screenshot({ path: shots + '/' + name, fullPage: true }); } catch(e) {}
          results.push({
            page: slug || 'home', viewport: vw, url,
            overflow: metrics.overflow, overflow_px: metrics.overflow,
            offenders: metrics.offenders,
            broken_images: metrics.brokenImgs, broken_images_count: metrics.brokenImgs.length,
            screenshot: name,
          });
          await ctx.close();
        }
      }
      await browser.close();
      console.log(JSON.stringify(results));
    })();
    '''
    node_script = os.path.join(os.path.dirname(OUT), "visual_node.js")
    with open(node_script, "w", encoding="utf-8") as f:
        f.write(script)
    env = dict(os.environ)
    env["BASE"] = BASE
    env["SHOT_DIR"] = SHOT_DIR
    env["VWS"] = json.dumps(VIEWPORTS)
    env["PAGES"] = json.dumps(pages)
    env["NODE_PATH"] = NMOD
    try:
        out = subprocess.run([NODE, node_script], env=env, cwd=os.path.dirname(node_script),
                             capture_output=True, text=True, timeout=900)
        if out.returncode != 0:
            print("NODE ERR:", out.stderr[:2000]); 
        data = json.loads(out.stdout.strip().split("\n")[-1])
    except Exception as e:
        print("EXC:", e); data = []
    finally:
        srv.terminate()
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    # summary
    tot = len(data)
    ovf = sum(1 for r in data if r.get("overflow_px", 0) > 0)
    brk = sum(r.get("broken_images_count", 0) for r in data)
    print(f"visual sweep: {tot} page/viewport combos | overflow={ovf} | broken_images={brk}")

if __name__ == "__main__":
    main()
