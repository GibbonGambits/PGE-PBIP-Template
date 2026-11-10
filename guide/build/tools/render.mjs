// Render guide/images/src/*.mmd -> guide/images/*.png (and keep crisp at scale 3)
import { createRequire } from 'node:module'; const require = createRequire(import.meta.url); const { chromium } = require('playwright');
import fs from 'node:fs';
import path from 'node:path';
const SRC = process.argv[2], OUT = process.argv[3];
const only = process.argv.slice(4);
const mermaidJs = fs.readFileSync(new URL('./node_modules/mermaid/dist/mermaid.min.js', import.meta.url), 'utf8');
const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 3, viewport: { width: 1800, height: 1200 } });
await page.setContent(`<html><head><style>body{margin:0;background:#fff;font-family:"DejaVu Sans",Arial,sans-serif} #c{display:inline-block;padding:16px;background:#fff}</style></head><body><div id="c"></div></body></html>`);
await page.addScriptTag({ content: mermaidJs });
await page.evaluate(() => {
  mermaid.initialize({ startOnLoad: false, theme: 'base', securityLevel: 'loose',
    fontFamily: '"DejaVu Sans", Arial, sans-serif',
    themeVariables: { fontSize: '17px', primaryColor: '#F1F5F9', primaryBorderColor: '#475569', lineColor: '#334155', primaryTextColor: '#0F172A', clusterBkg: '#F8FAFC', clusterBorder: '#94A3B8', actorBkg:'#E2E8F0', actorBorder:'#475569', noteBkgColor:'#FEF9C3', noteBorderColor:'#CA8A04', edgeLabelBackground:'#FFFFFF' },
    flowchart: { htmlLabels: true, curve: 'linear', nodeSpacing: 40, rankSpacing: 50, padding: 12, wrappingWidth: 320 },
    sequence: { useMaxWidth: false, actorMargin: 40, messageFontSize: 15, noteFontSize: 14, actorFontSize: 15, wrap: true, width: 170 },
    gitGraph: { useMaxWidth: false }, mindmap: { useMaxWidth: false }, timeline: { useMaxWidth: false } });
});
let files = fs.readdirSync(SRC).filter(f => f.endsWith('.mmd')).sort();
if (only.length) files = files.filter(f => only.some(o => f.startsWith(o)));
let failed = 0;
for (const f of files) {
  let code = fs.readFileSync(path.join(SRC, f), 'utf8');
  if (/^\s*(flowchart|graph)/.test(code)) code += `
classDef g fill:#DCFCE7,stroke:#15803D,color:#14532D,stroke-width:2px
classDef a fill:#FEF3C7,stroke:#B45309,color:#78350F,stroke-width:2px
classDef r fill:#FEE2E2,stroke:#B91C1C,color:#7F1D1D,stroke-width:2px
classDef ga fill:#DCFCE7,stroke:#1D4ED8,color:#14532D,stroke-width:4px,stroke-dasharray:6 3
classDef aa fill:#FEF3C7,stroke:#1D4ED8,color:#78350F,stroke-width:4px,stroke-dasharray:6 3
classDef ra fill:#FEE2E2,stroke:#1D4ED8,color:#7F1D1D,stroke-width:4px,stroke-dasharray:6 3
classDef ai fill:#DBEAFE,stroke:#1D4ED8,color:#1E3A8A,stroke-width:3px
classDef n fill:#F1F5F9,stroke:#475569,color:#0F172A,stroke-width:1.5px
classDef you fill:#EDE9FE,stroke:#6D28D9,color:#3B0764,stroke-width:2px
classDef ext fill:#E0F2FE,stroke:#0369A1,color:#0C4A6E,stroke-width:2px
classDef bad fill:#FFFFFF,stroke:#B91C1C,color:#7F1D1D,stroke-width:2px,stroke-dasharray:4 3
`;
  try {
    await page.evaluate(async (code) => {
      const { svg } = await mermaid.render('d' + Math.floor(Math.random()*1e9), code);
      const c = document.getElementById('c'); c.innerHTML = svg;
      const s = c.querySelector('svg'); s.style.maxWidth = 'none';
      const w = s.viewBox.baseVal && s.viewBox.baseVal.width; if (w) { s.setAttribute('width', w); s.setAttribute('height', s.viewBox.baseVal.height); }
    }, code);
    const el = await page.$('#c');
    const out = path.join(OUT, f.replace(/\.mmd$/, '.png'));
    await el.screenshot({ path: out });
    const bb = await el.boundingBox();
    console.log('OK', f, Math.round(bb.width) + 'x' + Math.round(bb.height));
  } catch (e) { failed++; console.log('FAIL', f, String(e.message || e).slice(0, 300)); }
}
await browser.close();
process.exit(failed ? 1 : 0);
