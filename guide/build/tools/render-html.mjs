import { createRequire } from 'node:module'; const require = createRequire(import.meta.url); const { chromium } = require('playwright');
import fs from 'node:fs'; import path from 'node:path';
const SRC = process.argv[2], OUT = process.argv[3]; const only = process.argv.slice(4);
const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 3, viewport: { width: 1400, height: 900 } });
let files = fs.readdirSync(SRC).filter(f => f.endsWith('.html')).sort();
if (only.length) files = files.filter(f => only.some(o => f.startsWith(o)));
for (const f of files) {
  await page.setContent(fs.readFileSync(path.join(SRC, f), 'utf8'));
  const el = await page.$('#c'); const out = path.join(OUT, f.replace(/\.html$/, '.png'));
  await el.screenshot({ path: out }); const bb = await el.boundingBox(); console.log('OK', f, Math.round(bb.width)+'x'+Math.round(bb.height));
}
await browser.close();
