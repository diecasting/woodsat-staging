const { chromium } = require(process.env.NMOD + '/playwright');

const BASE = 'http://localhost:8137/woodsat-staging/';
const SLUGS = [
  'best-wood-for-speaker-boxes',
  'mdf-vs-baltic-birch-plywood-speaker-cabinets',
  'wooden-vs-mdf-speaker-cabinets',
  'custom-cnc-wood-routing-services',
  'high-gloss-piano-lacquer-finishing-process-wood-speakers',
  'acoustic-wood-speaker-enclosures',
  'speaker-box-calculator',
  'speaker-box-finishes',
  'speaker-box-materials',
  'speaker-box-veneering',
  'speaker-cabinet-manufacturing',
  'subwoofer-enclosure-design',
  'wooden-speaker-cabinet-designs',
];
const SHOT_DIR = process.env.SHOT_DIR;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const results = [];
  for (const slug of SLUGS) {
    const url = BASE + slug + '/';
    const r = { slug, url, overflow: false, overflowPx: 0, brokenImages: [], imageCount: 0, errors: [] };
    try {
      const resp = await page.goto(url, { waitUntil: 'networkidle', timeout: 20000 });
      r.status = resp ? resp.status() : null;
      await page.waitForTimeout(400);
      const data = await page.evaluate(() => {
        const vw = window.innerWidth;
        const de = document.documentElement;
        const docOverflow = de.scrollWidth - vw;
        // find elements that stick out past the viewport horizontally
        const offenders = [];
        const all = de.querySelectorAll('*');
        for (const el of all) {
          const rect = el.getBoundingClientRect();
          if (rect.width > 0 && (rect.right > vw + 1 || rect.left < -1)) {
            offenders.push({
              tag: el.tagName.toLowerCase(),
              cls: (el.className && el.className.toString) ? el.className.toString().slice(0, 60) : '',
              right: Math.round(rect.right),
              left: Math.round(rect.left),
            });
          }
        }
        const imgs = Array.from(document.images);
        const broken = imgs
          .filter(im => !im.complete || im.naturalWidth === 0)
          .map(im => im.currentSrc || im.src);
        return { vw, docOverflow, offenders: offenders.slice(0, 8), imageCount: imgs.length, broken };
      });
      r.overflowPx = data.docOverflow;
      r.overflow = data.docOverflow > 2 || data.offenders.length > 0;
      r.offenders = data.offenders;
      r.imageCount = data.imageCount;
      r.brokenImages = data.broken;
      if (r.brokenImages.length) r.errors.push('broken images: ' + r.brokenImages.join(', '));
      if (r.overflow) r.errors.push('horizontal overflow ' + r.overflowPx + 'px');
      await page.screenshot({ path: SHOT_DIR + '/' + slug + '.png', fullPage: true });
    } catch (e) {
      r.errors.push('EXCEPTION: ' + e.message);
    }
    results.push(r);
    console.log(`[${r.slug}] status=${r.status} overflow=${r.overflow}(${r.overflowPx}px) imgs=${r.imageCount} broken=${r.brokenImages.length} ${r.errors.length ? 'ERR:' + r.errors.join('; ') : 'OK'}`);
  }
  await browser.close();
  const fs = require('fs');
  fs.writeFileSync(process.env.OUT_JSON, JSON.stringify(results, null, 2));
  const totalOverflow = results.filter(r => r.overflow).length;
  const totalBroken = results.reduce((a, r) => a + r.brokenImages.length, 0);
  console.log(`\nSUMMARY: overflow_pages=${totalOverflow} broken_images=${totalBroken}`);
  if (totalOverflow === 0 && totalBroken === 0) console.log('VISUAL_REGRESSION = PASS');
  else console.log('VISUAL_REGRESSION = FAIL');
})();
