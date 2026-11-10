// Lay out the guide HTML in Chromium, size every diagram block so it fits on
// one page, record block sizes, then print the PDF with page numbers.
// Usage: node print_pdf.mjs <in.html> <out.pdf> <overrides.json> <metrics.json> <geometry-json>
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
const require = createRequire(import.meta.url);
let chromium;
try { ({ chromium } = require('playwright')); }
catch { ({ chromium } = require('/opt/node-tools/node_modules/playwright')); }

const [, , input, output, overridesPath, metricsPath, geoJson] = process.argv;
const geo = JSON.parse(geoJson);
const overrides = fs.existsSync(overridesPath) ? JSON.parse(fs.readFileSync(overridesPath, 'utf8')) : {};
const mm = 96 / 25.4;
const contentW = Math.floor((geo.pageW - 2 * geo.side) * mm);
const contentH = Math.floor((geo.pageH - geo.top - geo.bottom) * mm);
const landW = Math.floor((geo.pageH - 2 * geo.side) * mm);
const landH = Math.floor((geo.pageW - geo.top - geo.bottom) * mm);

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: contentW, height: 1200 } });
await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
await page.emulateMedia({ media: 'print' });

const metrics = await page.evaluate(({ contentW, contentH, sideMaxW, overrides }) => {
  const out = {};
  for (const fig of document.querySelectorAll('.fig')) {
    const id = fig.id.slice(2);
    const w = +fig.dataset.w, h = +fig.dataset.h;
    const img = fig.querySelector('img');
    const side = fig.classList.contains('side');
    const fit = side ? Math.min(1, sideMaxW / w) : Math.min(1, contentW / w);
    const minScale = Math.min(0.6, fit);
    const capH = side ? 470 : 330;   // px: default height cap so blocks stay compact
    const sc = (overrides.scale || {})[id];
    const forced = (overrides.force || {})[id];
    let scale = forced !== undefined ? forced : sc !== undefined ? Math.min(sc, fit) : Math.max(minScale, Math.min(fit, capH / h));
    const apply = (s) => { img.style.width = (w * s) + 'px'; img.style.height = (h * s) + 'px'; };
    apply(scale);
    // shrink until the whole block fits on one page (keeps diagram + text together)
    let guard = 0;
    while (forced === undefined && fig.getBoundingClientRect().height > contentH - 8 && scale > minScale && guard++ < 60) {
      scale = Math.max(minScale, scale - 0.02);
      apply(scale);
    }
    out[id] = { forced: forced !== undefined, scale, minScale, fit, blockH: fig.getBoundingClientRect().height,
                imgH: img.getBoundingClientRect().height, side };
  }
  return out;
}, { contentW, contentH, sideMaxW: geo.sideMaxW, overrides });

// ---- page composer -------------------------------------------------------
// Walk the chapters in order, simulating where pages break, using live layout
// positions. Diagram blocks never split. When the next block does not fit and
// the page would be left more than ~30% empty: shrink that block slightly if
// it is close to fitting; else float the following paragraph above it; else
// grow the diagrams already on the page to fill the gap.
const composeLog = await page.evaluate(({ contentH, metrics, landW, landH }) => {
  const H = contentH - 4, LIMIT = H * 0.28;
  const log = [];
  const isHead = (e) => /^H[1-3]$/.test(e.tagName);
  const isFig = (e) => e && e.classList && e.classList.contains('fig');
  const splittable = (e) => ['P', 'UL', 'OL', 'TABLE'].includes(e.tagName);
  const movable = (e) => e && ['P', 'UL', 'OL', 'TABLE', 'PRE', 'BLOCKQUOTE'].includes(e.tagName);
  const sections = [...document.querySelectorAll('section.chapter')];
  const flat = () => sections.flatMap(s => [...s.children]);
  const top = (e) => e.getBoundingClientRect().top + window.scrollY;
  const next = (e) => { const all = flat(); return all[all.indexOf(e) + 1]; };
  const heightOf = (e) => {
    const n = next(e);
    if (n) return top(n) - top(e);
    const cs = getComputedStyle(e);
    return e.getBoundingClientRect().height + parseFloat(cs.marginTop) + parseFloat(cs.marginBottom);
  };
  const setScale = (fig, s) => {
    const img = fig.querySelector('img'), m = metrics[fig.id.slice(2)];
    img.style.width = (+fig.dataset.w * s) + 'px'; img.style.height = (+fig.dataset.h * s) + 'px';
    m.scale = s;
  };
  const shrinkInto = (fig, room) => {
    const m = metrics[fig.id.slice(2)], h = +fig.dataset.h;
    if (m.forced) return false;
    const before = m.scale, over = heightOf(fig) - room;
    const ih = fig.querySelector('img').getBoundingClientRect().height;
    const s = (ih - over - 3) / h;
    if (s < m.minScale || s < before * 0.72) return false;
    setScale(fig, s);
    if (heightOf(fig) <= room) return true;
    setScale(fig, before); return false;
  };
  const grow = (figs, gap) => {
    // give the gap to the figures on this page, last first
    let left = gap - 10;
    for (const fig of [...figs].reverse()) {
      if (left < 8) break;
      const m = metrics[fig.id.slice(2)], h = +fig.dataset.h;
      if (m.forced) continue;
      const ih = fig.querySelector('img').getBoundingClientRect().height;
      const before = heightOf(fig);
      const s = Math.min(m.fit, (ih + left) / h);
      if (s > m.scale + 0.005) {
        setScale(fig, s);
        log.push('grow ' + fig.id + ' to ' + s.toFixed(2));
      }
      left -= heightOf(fig) - before;
      // still room: lay the walkthrough out in one column instead of two
      const lists = [...fig.querySelectorAll('.figtext > ol, .figtext > ul')];
      if (left > 30 && fig.classList.contains('full') && lists.length) {
        const b2 = heightOf(fig);
        lists.forEach(l => l.style.columnCount = '1');
        const d = heightOf(fig) - b2;
        if (d > left + 6) lists.forEach(l => l.style.columnCount = '');
        else { left -= d; log.push('one-column ' + fig.id); }
      }
    }
  };
  const lines = (e) => {
    let rects;
    if (e.tagName === 'TABLE') rects = [...e.querySelectorAll('tr')].map(r => r.getBoundingClientRect());
    else { const r = document.createRange(); r.selectNodeContents(e); rects = [...r.getClientRects()]; }
    const out = [];
    for (const x of rects.filter(x => x.height > 0).map(x => [x.top + window.scrollY, x.bottom + window.scrollY]).sort((a, b) => a[0] - b[0])) {
      const last = out[out.length - 1];
      if (last && x[0] < last[1] - 2) last[1] = Math.max(last[1], x[1]); else out.push([x[0], x[1]]);
    }
    return out;
  };
  // where the next page starts when element e crosses the page end
  const splitAt = (e, pageEnd) => {
    const ls = lines(e);
    const i = ls.findIndex(l => l[1] > pageEnd);
    if (i <= 0) return top(e);                       // nothing fits: whole element moves
    if (e.tagName === 'P' && (i < 3 || ls.length - i < 3)) return i < 3 ? top(e) : ls[Math.max(0, ls.length - 3)][0];
    return ls[i][0];
  };

  // A page holding only [heading] + one wide diagram (+ a little text) that
  // would stay more than ~30% empty becomes a landscape page, with the diagram
  // printed larger so it fills the page.
  const tryLandscape = (endEl) => {
    const all = flat();
    const i0 = all.findIndex(e => top(e) >= pageStart - 1), i1 = all.indexOf(endEl);
    if (i0 < 0 || i1 <= i0) return false;
    const items = all.slice(i0, i1);
    const figs = items.filter(isFig);
    if (figs.length !== 1) return false;
    const fig = figs[0], w = +fig.dataset.w, h = +fig.dataset.h;
    if (w / h < 1.3 || w < 600) return false;
    const others = items.filter(e => e !== fig && !isHead(e));
    if (others.some(e => !['P', 'UL', 'OL'].includes(e.tagName))) return false;
    if (others.reduce((a, e) => a + heightOf(e), 0) > 140) return false;
    const m = metrics[fig.id.slice(2)];
    if (m.forced) return false;
    items.forEach(e => { e.classList.add('wide'); e.style.width = landW + 'px'; });
    const fixed = items.reduce((a, e) => a + heightOf(e), 0) - fig.querySelector('img').getBoundingClientRect().height;
    const s = Math.min(1.0, (landW - 4) / w, (landH * 0.95 - fixed) / h);
    setScale(fig, Math.max(s, m.scale));
    m.landscape = true;
    items.forEach(e => { e.style.width = ''; });
    log.push('landscape ' + fig.id + ' at ' + m.scale.toFixed(2));
    return true;
  };
  let el = sections[0].firstElementChild;
  let pageStart = top(el), pageFigs = [], guard = 0;
  const breakBefore = (e) => { pageStart = top(e); pageFigs = []; };
  const trace = [];
  while (el && guard++ < 6000) {
    const t = top(el) - pageStart;
    if (trace.length < 60) trace.push([el.tagName, el.id || (el.textContent||'').slice(0,30), Math.round(t), Math.round(heightOf(el)), Math.round(pageStart)]);
    if (isHead(el)) {
      const n = next(el);
      const need = heightOf(el) + (n ? (isFig(n) ? heightOf(n) : Math.min(heightOf(n), 70)) : 0);
      if (t + need <= H) { el = n; continue; }
      const gap = H - t;
      if (isFig(n) && gap > LIMIT && shrinkInto(n, gap - heightOf(el))) { el = n; continue; }
      if (gap > LIMIT && !tryLandscape(el) && pageFigs.length) grow(pageFigs, H - (top(el) - pageStart));
      breakBefore(el); el = n; continue;
    }
    const h = heightOf(el);
    if (splittable(el)) {
      while (top(el) + h - pageStart > H) {
        const ns = splitAt(el, pageStart + H);
        if (ns <= pageStart) { pageStart += H; } else { pageStart = ns; }
        pageFigs = [];
      }
      el = next(el); continue;
    }
    if (t + h <= H) { if (isFig(el)) pageFigs.push(el); el = next(el); continue; }
    const gap = H - t;
    if (isFig(el) && shrinkInto(el, gap)) { pageFigs.push(el); el = next(el); continue; }
    const fol = el.nextElementSibling;
    if (gap > LIMIT && movable(fol) && !isHead(fol)) {
      el.parentNode.insertBefore(fol, el);
      log.push('float before ' + el.id);
      el = fol; continue;
    }
    if (gap > LIMIT && !tryLandscape(el) && pageFigs.length) grow(pageFigs, H - (top(el) - pageStart));
    breakBefore(el); if (isFig(el)) pageFigs.push(el); el = next(el);
  }
  for (const fig of document.querySelectorAll('.fig')) {
    const m = metrics[fig.id.slice(2)];
    m.blockH = fig.getBoundingClientRect().height;
    m.imgH = fig.querySelector('img').getBoundingClientRect().height;
  }
  return { log, trace };
}, { contentH, metrics, landW, landH });
console.log('composer:', composeLog.log.length, 'actions');
fs.writeFileSync(metricsPath.replace('.json','-trace.json'), JSON.stringify(composeLog.trace));
fs.writeFileSync(metricsPath.replace('.json','-log.json'), JSON.stringify(composeLog.log, null, 1));
fs.writeFileSync(metricsPath, JSON.stringify(metrics, null, 1));

await page.pdf({
  path: output,
  preferCSSPageSize: true,
  printBackground: true,
  displayHeaderFooter: true,
  headerTemplate: '<div></div>',
  footerTemplate: `<div style="width:100%; font-family:'DejaVu Sans',Arial,sans-serif; font-size:9px; color:#475569; padding:0 16mm; display:flex; justify-content:space-between;">
    <span>PGE-PBIP Masterclass</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`,
});
await browser.close();
console.log('wrote', output);
