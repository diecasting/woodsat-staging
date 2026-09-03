
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
    