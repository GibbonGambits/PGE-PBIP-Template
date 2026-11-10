// Print the masterclass HTML to PDF with Chromium (Playwright).
// Usage: node print_pdf.mjs <input.html> <output.pdf>
import { createRequire } from 'node:module';
import path from 'node:path';
const require = createRequire(import.meta.url);
let chromium;
try { ({ chromium } = require('playwright')); }
catch { ({ chromium } = require('/opt/node-tools/node_modules/playwright')); }

const [, , input, output] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
await page.emulateMedia({ media: 'print' });
const footer = `
<div style="width:100%; font-family:'DejaVu Sans',Arial,sans-serif; font-size:7.5px; color:#475569; padding:0 14mm; display:flex; justify-content:space-between; align-items:center;">
  <span>PGE-PBIP Masterclass &nbsp;|&nbsp;
    <span style="background:#DCFCE7;border:1px solid #15803D;padding:0 3px">Green: safe</span>
    <span style="background:#FEF3C7;border:1px solid #B45309;padding:0 3px">Amber: care</span>
    <span style="background:#FEE2E2;border:1px solid #B91C1C;padding:0 3px">Red: do not edit</span>
    <span style="border:1.5px dashed #1D4ED8;padding:0 3px">Blue dashed: AI file</span></span>
  <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
</div>`;
await page.pdf({
  path: output,
  preferCSSPageSize: true,
  printBackground: true,
  displayHeaderFooter: true,
  headerTemplate: '<div></div>',
  footerTemplate: footer,
});
await browser.close();
console.log('wrote', output);
