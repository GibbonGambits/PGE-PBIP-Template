#!/usr/bin/env python3
"""Build guide/PGE-PBIP-Masterclass.pdf from the guide's Markdown sections.

Steps: Markdown -> HTML fragments (pandoc), wide figures wrapped in landscape
blocks, title page + legend + visual table of contents, then Chromium (via
Playwright, see print_pdf.mjs) prints the PDF. Two passes: the first finds the
page each section starts on, the second writes those page numbers into the TOC.

Run from anywhere:  python3 guide/build/build_pdf.py
Needs: pandoc, node with playwright, python pypdf.
"""
import glob, html, os, re, struct, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.dirname(HERE)
IMAGES = os.path.join(GUIDE, "images")
OUT_HTML = os.path.join(HERE, "masterclass.html")
OUT_PDF = os.path.join(GUIDE, "PGE-PBIP-Masterclass.pdf")
WIDE_MIN_W, WIDE_MAX_H = 1000, 700  # css px (PNG pixels / 3)

SECTIONS = sorted(f for f in glob.glob(os.path.join(GUIDE, "[0-9][0-9]-*.md")))


def png_css_size(rel):
    with open(os.path.join(GUIDE, rel), "rb") as f:
        w, h = struct.unpack(">II", f.read(24)[16:24])
    return w / 3, h / 3


def wrap_wide(md):
    """Put each wide figure (image + caption + walkthrough) on landscape pages."""
    lines, out, inside_manual, open_auto = md.split("\n"), [], False, False
    for line in lines:
        s = line.strip()
        if s.startswith('<div class="landscape">'):
            inside_manual = True
        elif s == "</div>" and inside_manual:
            inside_manual = False
        m = re.match(r"!\[[^\]]*\]\((images/[^)]+\.png)\)", s)
        ends_block = m or s.startswith("## ") or s == "---"
        if open_auto and ends_block:
            out += ["", "</div>", ""]
            open_auto = False
        if m and not inside_manual:
            w, h = png_css_size(m.group(1))
            if w >= WIDE_MIN_W and h < WIDE_MAX_H:
                out += ["", '<div class="landscape">', ""]
                open_auto = True
        out.append(line)
    if open_auto:
        out += ["", "</div>", ""]
    # a heading directly before a landscape block moves inside it, so it is
    # never stranded alone on a portrait page
    i = 0
    while i < len(out):
        if out[i].strip() == '<div class="landscape">':
            j = i - 1
            while j >= 0 and not out[j].strip():
                j -= 1
            if j >= 0 and out[j].lstrip().startswith("#"):
                heading = out.pop(j)
                i -= 1
                out.insert(i + 1, "")
                out.insert(i + 2, heading)
        i += 1
    return "\n".join(out)


def md_to_html(path):
    md = wrap_wide(open(path, encoding="utf-8").read())
    res = subprocess.run(
        ["pandoc", "-f", "markdown-implicit_figures+pipe_tables+raw_html", "-t", "html5", "--wrap=none"],
        input=md, capture_output=True, text=True, check=True)
    body = res.stdout
    # give every image its natural size so nothing is ever enlarged
    def size_img(m):
        src = m.group(1)
        w, h = png_css_size(src)
        return f'<img src="{src}" style="width:{w:.0f}px" data-h="{h:.0f}"'
    body = re.sub(r'<img src="(images/[^"]+\.png)"', size_img, body)
    body = body.replace("<p>Walkthrough of", '<p class="wt">Walkthrough of')
    return body


def section_meta(path):
    text = open(path, encoding="utf-8").read()
    title = re.search(r"^# (.+)$", text, re.M).group(1)
    first_img = re.search(r"\((images/[^)]+\.png)\)", text)
    num = os.path.basename(path)[:2]
    return num, title, first_img.group(1) if first_img else None


CSS = r"""
@page { size: A4 portrait; margin: 16mm 14mm 18mm 14mm; }
@page wide { size: A4 landscape; margin: 14mm 14mm 16mm 14mm; }
@page cover { size: A4 portrait; margin: 0; }
html { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 10.5pt; color: #0F172A; line-height: 1.45; }
body { margin: 0; }
h1 { font-size: 22pt; margin: 0 0 10pt 0; color: #1E3A8A; border-bottom: 3px solid #1D4ED8; padding-bottom: 4pt; }
h2 { font-size: 15pt; margin: 16pt 0 6pt 0; color: #1E293B; break-after: avoid; }
h3 { font-size: 12pt; margin: 12pt 0 4pt 0; break-after: avoid; }
p, li { orphans: 3; widows: 3; }
section.chapter { break-before: page; }
.landscape { page: wide; break-before: page; }
.landscape img { max-height: 112mm; }
.landscape { font-size: 9.6pt; }
.landscape > p { margin: 3pt 0; }
.landscape > ol, .landscape > ul { column-count: 2; column-gap: 9mm; }
.landscape li { break-inside: avoid; }
img { max-width: 100%; height: auto; max-height: 242mm; display: block; margin: 6pt auto 4pt auto; object-fit: contain; break-inside: avoid; }
h1 + p img { max-height: 205mm; }
h2 + p img { max-height: 222mm; }
.landscape h1 + p img, .landscape h2 + p img { max-height: 108mm; }
p:has(> img) { break-inside: avoid; break-after: avoid; margin: 0; }
p:has(> img) + p { break-before: avoid; }
table { border-collapse: collapse; width: 100%; font-size: 8.8pt; margin: 6pt 0; }
th, td { border: 1px solid #94A3B8; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #E2E8F0; }
tr { break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt; background: #F1F5F9; padding: 0 2px; border-radius: 3px; overflow-wrap: anywhere; }
pre { background: #0F172A; color: #E2E8F0; padding: 7pt 9pt; border-radius: 6px; white-space: pre-wrap; word-break: break-all; font-size: 8.4pt; break-inside: avoid; }
pre code { background: none; color: inherit; padding: 0; font-size: inherit; }
blockquote { border-left: 4px solid #1D4ED8; background: #EFF6FF; margin: 8pt 0; padding: 4pt 10pt; }
a { color: #1D4ED8; text-decoration: none; overflow-wrap: anywhere; }
hr { display: none; }
.wt { break-after: avoid; margin-bottom: 2pt; }
.wt + ol > li:first-child, .wt + ul > li:first-child { break-before: avoid; }
#s19 table { table-layout: fixed; font-size: 7.6pt; }
#s19 th:nth-child(1) { width: 5%; } #s19 th:nth-child(2) { width: 44%; } #s19 th:nth-child(3) { width: 13%; }
#s19 th:nth-child(4) { width: 24%; } #s19 th:nth-child(5) { width: 8%; } #s19 th:nth-child(6) { width: 6%; }
#s19 td, #s19 th { padding: 2pt 3pt; }
#s19 code { font-size: 7.2pt; background: none; padding: 0; }
.marker { font-size: 1px; color: #fff; }
/* cover */
.cover { page: cover; height: 297mm; box-sizing: border-box; padding: 26mm 20mm 18mm 20mm; background: linear-gradient(160deg, #1E3A8A 0%, #1D4ED8 55%, #0EA5E9 100%); color: #fff; position: relative; }
.cover h1 { color: #fff; border: none; font-size: 34pt; line-height: 1.15; margin-top: 18mm; }
.cover .sub { font-size: 15pt; opacity: .95; margin-top: 6mm; }
.cover .meta { position: absolute; bottom: 20mm; left: 20mm; right: 20mm; font-size: 10.5pt; opacity: .95; }
.cover .chips { margin-top: 14mm; display: flex; gap: 8px; flex-wrap: wrap; }
.cover .chip { background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.5); border-radius: 20px; padding: 4px 12px; font-size: 10pt; }
.cover .legendbox { margin-top: 16mm; background: #fff; border-radius: 10px; padding: 6px; }
.cover .legendbox img { max-height: 80mm; margin: 0 auto; }
/* toc */
.toc h1 { margin-bottom: 6pt; }
.tocgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 7pt; }
.toccard { display: flex; gap: 8pt; border: 1.5px solid #CBD5E1; border-radius: 8px; padding: 6pt; break-inside: avoid; align-items: center; background: #F8FAFC; }
.toccard .thumb { width: 36mm; height: 21mm; flex: none; background: #fff; border: 1px solid #E2E8F0; border-radius: 4px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.toccard .thumb img { max-width: 100%; max-height: 100%; margin: 0; }
.toccard .num { font-size: 15pt; font-weight: bold; color: #1D4ED8; }
.toccard .t { font-size: 9.6pt; font-weight: bold; line-height: 1.25; }
.toccard .pg { font-size: 9pt; color: #475569; margin-top: 2pt; }
.part { grid-column: 1 / span 2; font-weight: bold; color: #1E293B; margin: 4pt 0 0 0; font-size: 10.5pt; border-bottom: 1px solid #CBD5E1; }
"""

PARTS = {"00": "Part 1 - Foundations", "05": "Part 2 - How it fits", "08": "Part 3 - Doing the work", "14": "Part 4 - Look it up"}


def build_html(page_of=None):
    metas = [section_meta(p) for p in SECTIONS]
    parts = [f"<!DOCTYPE html><html><head><meta charset='utf-8'><base href='file://{GUIDE}/'><title>PGE-PBIP Masterclass</title><style>{CSS}</style></head><body>"]
    parts.append(f"""<div class="cover">
<div style="font-size:12pt;letter-spacing:2px;opacity:.85">A VISUAL LEARNING GUIDE</div>
<h1>PGE-PBIP Masterclass</h1>
<div class="sub">Power BI projects, Git, VS Code and AI agents, explained one picture at a time, using the GibbonGambits/PGE-PBIP-Template repository.</div>
<div class="chips"><span class="chip">{len(SECTIONS)} sections</span><span class="chip">176 files and folders covered</span><span class="chip">for absolute beginners</span></div>
<div class="legendbox"><img src="images/00-1-legend.png" style="width:1136px"></div>
<div class="meta">Colour legend shown above is used in every diagram.<br>Facts checked against official documentation on 10 November 2026.</div>
</div>""")
    cards = []
    for num, title, img in metas:
        if num in PARTS:
            cards.append(f"<div class='part'>{PARTS[num]}</div>")
        t = html.escape(re.sub(r"^\d+\.\s*", "", title)).replace("`", "")
        pg = f"page {page_of[num]}" if page_of and num in page_of else "page"
        thumb = f"<img src='{img}'>" if img else ""
        cards.append(f"<div class='toccard'><div class='thumb'>{thumb}</div><div><div class='num'>{num}</div><div class='t'>{t}</div><div class='pg'>{pg}</div></div></div>")
    parts.append(f"<section class='chapter toc'><h1>Contents</h1><div class='tocgrid'>{''.join(cards)}</div></section>")
    for path, (num, title, img) in zip(SECTIONS, metas):
        body = md_to_html(path)
        body = re.sub(r"(<h1[^>]*>)", r"\1<span class='marker'>@@SEC" + num + "@@</span>", body, count=1)
        parts.append(f"<section class='chapter' id='s{num}'>{body}</section>")
    parts.append("</body></html>")
    open(OUT_HTML, "w", encoding="utf-8").write("\n".join(parts))


def print_pdf():
    subprocess.run(["node", os.path.join(HERE, "print_pdf.mjs"), OUT_HTML, OUT_PDF], check=True)


def find_pages():
    from pypdf import PdfReader
    r = PdfReader(OUT_PDF)
    found = {}
    for i, pg in enumerate(r.pages, 1):
        for m in re.findall(r"@@SEC(\d\d)@@", pg.extract_text() or ""):
            found.setdefault(m, i)
    return found, len(r.pages)


if __name__ == "__main__":
    build_html()
    print_pdf()
    pages, n = find_pages()
    build_html(pages)
    print_pdf()
    pages2, n2 = find_pages()
    if pages2 != pages:  # TOC length changed nothing in practice, but be safe
        build_html(pages2); print_pdf(); pages2, n2 = find_pages()
    print("pages:", n2, "section starts:", pages2)
