# How the guide and PDF are built

Everything here only reads the repository; it writes only inside `guide/`.

| File | Purpose |
|---|---|
| `inventory.py` | Every repository file and folder, with type, purpose and safety flag (Green / Amber / Red, plus the AI-file label) |
| `details.py` | The plain-English summary and technical role for each of the 176 items |
| `gen_section14.py` | Writes `../14-file-directory.md` and its folder-tree figures `../images/14-*-tree.png` sources |
| `build_pdf.py` | Markdown sections -> HTML (pandoc) -> PDF (Chromium via `print_pdf.mjs`); two passes so the contents page shows page numbers |
| `print_pdf.mjs` | Prints the HTML with page numbers and the colour legend in the footer |
| `tools/render.mjs` | Renders `../images/src/*.mmd` (Mermaid) to PNG |
| `tools/render-html.mjs` | Renders `../images/src/*.html` figures to PNG |
| `tools/htmlfig.py`, `treefig.py`, `swimlane.py`, `swimlanes_all.py` | Helpers that write the HTML figure sources |

## Rebuild

Needs pandoc, Python 3 with `pypdf`, and Node.js with Playwright's Chromium.

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
