# How the guide and PDF are built

Everything here only reads the repository; it writes only inside `guide/`.

| File | Purpose |
|---|---|
| `inventory.py` | Every repository file and folder, with type, purpose and safety flag (Green / Amber / Red, plus the AI-file label) |
| `details.py` | The plain-English summary and technical role for each of the 176 items |
| `gen_appendix_a.py` | Writes `../A-file-directory.md` (Appendix A) and its folder-tree figure sources `../images/src/14-*-tree.html` |
| `build_pdf.py` | Markdown -> HTML (pandoc); groups each diagram with its caption and walkthrough; prints with `print_pdf.mjs`; measures empty space on every page and shrinks a diagram slightly when that keeps a page from being more than a third empty; fills in contents page numbers |
| `fit_overrides.json` | Diagram scale overrides chosen by the fitting step (regenerated on every build) |
| `print_pdf.mjs` | Sizes every diagram block to fit one page, records block sizes, prints with page numbers |
| `tools/render.mjs` | Renders `../images/src/*.mmd` (Mermaid) to PNG |
| `tools/render-html.mjs` | Renders `../images/src/*.html` figures to PNG |
| `tools/htmlfig.py`, `treefig.py`, `swimlane.py`, `swimlanes_all.py` | Helpers that write the HTML figure sources |

## Rebuild

Needs pandoc, `pdftoppm`, Python 3 with `bs4`, `pypdf` and Pillow, and Node.js with Playwright's Chromium.

```bash
cd guide/build/tools && npm install mermaid@11
```

```bash
node guide/build/tools/render.mjs guide/images/src guide/images
```

```bash
node guide/build/tools/render-html.mjs guide/images/src guide/images
```

```bash
python3 guide/build/build_pdf.py
```
