#!/usr/bin/env python3
"""Build guide/PowerBI-Development-VSCode-Copilot.pdf from the guide's Markdown files.

Pipeline
  1. Markdown -> HTML with pandoc.
  2. Each diagram is grouped with its caption and walkthrough into one block
     that never splits across pages. Tall, narrow diagrams sit beside their
     text ("side" layout); wider ones sit above it ("full" layout).
  3. print_pdf.mjs lays the HTML out in Chromium, shrinks any block that is
     taller than a page, applies per-figure size overrides, and prints.
  4. Every page is rasterised and its empty space measured. When a page is
     more than about a third empty because the next block did not fit, that
     block's diagram is shrunk a little (never below a readable minimum) and
     the PDF is rebuilt. The contents page numbers come from the final PDF.

Run:  python3 guide/build/build_pdf.py
Needs: pandoc, python3 with bs4 + pypdf + Pillow, node with playwright, pdftoppm.
"""
import glob, html, json, os, re, struct, subprocess, sys
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.dirname(HERE)
OUT_HTML = os.path.join(HERE, "guide.html")
OUT_PDF = os.path.join(GUIDE, "PowerBI-Development-VSCode-Copilot.pdf")
METRICS = os.path.join(HERE, "metrics.json")
OVERRIDES = os.path.join(HERE, "fit_overrides.json")
WORK = os.path.join(HERE, ".pages")

ORDER = ["00-start-here"] + [f"{i:02d}-" for i in range(1, 15)] + ["A-", "B-", "C-"]
FILES = []
for prefix in ORDER:
    FILES += sorted(glob.glob(os.path.join(GUIDE, prefix + "*.md")))

# page geometry (A4 portrait), keep in sync with CSS below
PAGE_W, PAGE_H, M_TOP, M_BOTTOM, M_SIDE = 210, 297, 15, 17, 16  # mm
SIDE_MAX_W = 400  # px: width of the diagram column in "side" layout
SIDE_IF_NARROWER = 560  # css px: diagrams narrower than this go "side"
EMPTY_LIMIT = 1 / 3


def png_css_size(rel):
    with open(os.path.join(GUIDE, rel), "rb") as f:
        w, h = struct.unpack(">II", f.read(24)[16:24])
    return w / 3, h / 3


def md_to_html(path):
    md = open(path, encoding="utf-8").read()
    res = subprocess.run(
        ["pandoc", "-f", "markdown-implicit_figures+pipe_tables+raw_html+fancy_lists+startnum", "-t", "html5", "--wrap=none"],
        input=md, capture_output=True, text=True, check=True)
    return res.stdout


def group_figures(soup):
    """Wrap image + caption + following lists in div.fig (side or full)."""
    figs = []
    for img_p in list(soup.find_all("p")):
        img = img_p.find("img", recursive=False)
        if img is None or img_p.get_text(strip=True):
            continue
        src = img["src"]
        w, h = png_css_size(src)
        parts = [img_p]
        nxt = img_p.find_next_sibling()
        if nxt is not None and nxt.name == "p" and nxt.get_text().startswith("Figure"):
            parts.append(nxt)
            nxt = nxt.find_next_sibling()
            while nxt is not None and nxt.name in ("ol", "ul"):
                parts.append(nxt)
                nxt = nxt.find_next_sibling()
        fid = os.path.splitext(os.path.basename(src))[0]
        layout = "side" if w <= SIDE_IF_NARROWER else "full"
        fig = soup.new_tag("div", attrs={"class": f"fig {layout}", "id": "f-" + fid,
                                         "data-w": f"{w:.0f}", "data-h": f"{h:.0f}"})
        img_p.insert_before(fig)
        holder = soup.new_tag("div", attrs={"class": "figimg"})
        img_p.extract()
        img.attrs = {"src": src, "alt": img.get("alt", "")}
        holder.append(img)
        fig.append(holder)
        text = soup.new_tag("div", attrs={"class": "figtext"})
        for p in parts[1:]:
            text.append(p.extract())
        fig.append(text)
        if layout == "side":
            for lst in text.find_all(["ol", "ul"], recursive=False):
                n = int(lst.get("start", 1))
                for li in lst.find_all("li", recursive=False):
                    tag = soup.new_tag("span", attrs={"class": "n"})
                    tag.string = (f"{n}. " if lst.name == "ol" else "• ")
                    li.insert(0, tag)
                    n += 1
        cap = parts[1].get_text() if len(parts) > 1 else ""
        m = re.match(r"Figure ([0-9A-C]+\.\d+)", cap)
        figs.append({"id": fid, "num": m.group(1) if m else None})
    return figs


CSS = """
@page { size: A4 portrait; margin: %(t)smm %(s)smm %(b)smm %(s)smm; }
@page cover { margin: 0; }
@page wide { size: A4 landscape; margin: %(t)smm %(s)smm %(b)smm %(s)smm; }
.wide { page: wide; }
.fig.wide .figtext > ol, .fig.wide .figtext > ul { column-count: 2 !important; column-gap: 10mm; }
html { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 11pt; color: #0F172A; line-height: 1.42; }
body { margin: 0; }
h1 { font-size: 20pt; margin: 14pt 0 8pt 0; color: #1E3A8A; border-bottom: 3px solid #1D4ED8; padding-bottom: 3pt; break-after: avoid; }
h2 { font-size: 14pt; margin: 12pt 0 5pt 0; color: #1E293B; break-after: avoid; }
p { margin: 0 0 6pt 0; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 6pt 0; padding-left: 18pt; }
li { margin: 0 0 2pt 0; }
table { border-collapse: collapse; width: 100%%; font-size: 11pt; margin: 4pt 0 8pt 0; }
th, td { border: 1px solid #94A3B8; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #E2E8F0; }
tr { break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 10pt; background: #F1F5F9; padding: 0 2px; border-radius: 3px; overflow-wrap: anywhere; }
pre { background: #0F172A; color: #E2E8F0; padding: 6pt 8pt; border-radius: 6px; white-space: pre-wrap; word-break: break-all; font-size: 10pt; break-inside: avoid; margin: 0 0 8pt 0; }
pre code { background: none; color: inherit; padding: 0; }
blockquote { border-left: 4px solid #1D4ED8; background: #EFF6FF; margin: 6pt 0; padding: 4pt 10pt; break-inside: avoid; }
blockquote p { margin: 0; }
a { color: #1D4ED8; text-decoration: none; overflow-wrap: anywhere; }
hr { display: none; }
.appx-a table { table-layout: fixed; }
.appx-a th:nth-child(1) { width: 31%%; } .appx-a th:nth-child(2) { width: 15%%; }
.appx-a th:nth-child(3) { width: 40%%; } .appx-a th:nth-child(4) { width: 14%%; }
.appx-b table, .appx-c table { table-layout: fixed; }
.appx-c th:nth-child(1) { width: 27%%; } .appx-c th:nth-child(2) { width: 61%%; } .appx-c th:nth-child(3) { width: 12%%; }
.appx-b th:nth-child(1) { width: 46%%; } .appx-b th:nth-child(2) { width: 54%%; }
.fig { break-inside: avoid; margin: 8pt 0 10pt 0; }
.fig img { display: block; }
.fig.full .figimg img { margin: 0 auto 4pt auto; }
.fig.side { display: flow-root; }
.fig.side .figimg { float: left; margin: 0 6mm 2mm 0; }
.fig.side .figtext ol, .fig.side .figtext ul { list-style: none; padding-left: 0; }
.fig.side .figtext li .n { font-weight: bold; }
.figtext > p:first-child { margin-bottom: 4pt; }
.fig.full .figtext > ol, .fig.full .figtext > ul { column-count: 2; column-gap: 8mm; }
.fig.full .figtext li { break-inside: avoid; }
.start { break-before: page; break-after: page; }
.start h1 { margin-top: 0; }
#the-whole-system-in-one-picture { break-before: page; margin-top: 0; }
.toc h1 { margin-top: 0; }
.toc table td, .toc table th { padding: 1.5pt 5pt; }
.toc { break-after: page; }
.toc table td:last-child, .toc table th:last-child { text-align: right; width: 18mm; }
.cover { page: cover; height: 297mm; box-sizing: border-box; padding: 30mm 22mm 20mm 22mm; background: linear-gradient(160deg, #1E3A8A 0%%, #1D4ED8 55%%, #0EA5E9 100%%); color: #fff; position: relative; }
.cover h1 { color: #fff; border: none; font-size: 34pt; line-height: 1.15; margin-top: 30mm; }
.cover .sub { font-size: 15pt; margin-top: 8mm; line-height: 1.4; }
.cover .meta { position: absolute; bottom: 24mm; left: 22mm; right: 22mm; font-size: 11pt; }
""" % {"t": M_TOP, "b": M_BOTTOM, "s": M_SIDE}


MOVABLE = {"p", "ul", "ol", "table", "pre", "blockquote"}
DEFER = {}


def apply_defers(soup, defer):
    """Move a figure block below the next n movable siblings (like a float)."""
    for fid, n in defer.items():
        fig = soup.find("div", id="f-" + fid)
        if fig is None:
            continue
        for _ in range(n):
            nxt = fig.find_next_sibling()
            if nxt is None or nxt.name not in MOVABLE:
                break
            nxt.extract()
            fig.insert_before(nxt)


def movable_after(fid):
    soup = BeautifulSoup(open(OUT_HTML, encoding="utf-8").read(), "html.parser")
    fig = soup.find("div", id="f-" + fid)
    nxt = fig.find_next_sibling() if fig else None
    return nxt is not None and nxt.name in MOVABLE


def chapter_title(path):
    return re.search(r"^# (.+)$", open(path, encoding="utf-8").read(), re.M).group(1)


def build_html(page_of=None):
    titles = [chapter_title(p) for p in FILES]
    out = [f"<!DOCTYPE html><html><head><meta charset='utf-8'><base href='file://{GUIDE}/'>"
           f"<title>Power BI Development with VS Code and GitHub Copilot</title><style>{CSS}</style></head><body>"]
    out.append("""<div class="cover"><div style="font-size:12pt;letter-spacing:2px">A PRACTICAL GUIDE FOR NEW DEVELOPERS</div>
<h1>Power BI Development with VS Code and GitHub Copilot</h1>
<div class="sub">State of Practice, Nov 10, 2026</div>
<div class="sub" style="margin-top:4mm">By Raj Rana</div>
<div class="meta">Facts checked against the repository and official documentation on 10 November 2026.</div></div>""")
    rows = "".join(
        f"<tr><td>{html.escape(t)}</td><td>{page_of.get(i, '') if page_of else ''}</td></tr>"
        for i, t in enumerate(titles))
    out.append(f"""<section class="toc"><h1>Contents</h1>
<div class="fig full" id="f-00-2-roadmap" data-w="836" data-h="574"><div class="figimg"><img src="images/00-2-roadmap.png" alt="Guide roadmap"></div>
<div class="figtext"><p><strong>The guide at a glance.</strong> Start here is two pages. Parts 1 and 2 explain the pieces and how they connect; Part 3 walks through the common tasks; Part 4 is for looking things up.</p></div></div>
<table><tr><th>Chapter</th><th>Page</th></tr>{rows}</table></section>""")
    figs = []
    for i, path in enumerate(FILES):
        soup = BeautifulSoup(md_to_html(path), "html.parser")
        figs += group_figures(soup)
        apply_defers(soup, DEFER)
        base = os.path.basename(path)
        cls = "start" if base.startswith("00-") else "chapter appx-" + base[0].lower() if base[0] in "ABC" else "chapter"
        out.append(f"<section class='{cls}' data-idx='{i}'>{soup}</section>")
    out.append("</body></html>")
    open(OUT_HTML, "w", encoding="utf-8").write("\n".join(out))
    return titles, figs


def print_pdf():
    geo = json.dumps({"pageW": PAGE_W, "pageH": PAGE_H, "top": M_TOP, "bottom": M_BOTTOM, "side": M_SIDE,
                      "sideMaxW": SIDE_MAX_W})
    subprocess.run(["node", os.path.join(HERE, "print_pdf.mjs"), OUT_HTML, OUT_PDF, OVERRIDES, METRICS, geo], check=True)


def page_texts():
    from pypdf import PdfReader
    lig = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl"}
    out = []
    for p in PdfReader(OUT_PDF).pages:
        t = p.extract_text() or ""
        for a, b in lig.items():
            t = t.replace(a, b)
        out.append(t)
    return out


def empty_fractions():
    """Fraction of each page's content area left blank below the last ink."""
    from PIL import Image
    os.makedirs(WORK, exist_ok=True)
    for f in glob.glob(os.path.join(WORK, "*.png")):
        os.remove(f)
    subprocess.run(["pdftoppm", "-r", "30", "-gray", "-png", OUT_PDF, os.path.join(WORK, "p")], check=True)
    fr = []
    for f in sorted(glob.glob(os.path.join(WORK, "p-*.png"))):
        im = Image.open(f).convert("L")
        w, h = im.size
        ph = PAGE_W if w > h else PAGE_H
        top, bottom = int(h * M_TOP / ph), int(h * (ph - M_BOTTOM) / ph)
        px = im.load()
        last = top
        for y in range(bottom - 1, top, -1):
            if any(px[x, y] < 235 for x in range(0, w, 2)):
                last = y
                break
        fr.append((bottom - last) / (bottom - top))
    return fr


def fit(max_rounds=40, per_round=3):
    global DEFER
    state = {"scale": {}, "defer": {}}
    DEFER = state["defer"]
    json.dump(state, open(OVERRIDES, "w"))
    titles, figs = build_html()
    num_to_id = {f["num"]: f["id"] for f in figs if f["num"]}
    content_px = (PAGE_H - M_TOP - M_BOTTOM) / 25.4 * 96
    bad = []
    for rnd in range(max_rounds):
        print_pdf()
        metrics = json.load(open(METRICS))
        texts, empties = page_texts(), empty_fractions()
        bad, actions = [], 0
        for i in range(1, len(texts) - 1):
            if empties[i] <= EMPTY_LIMIT - 0.03:
                continue
            nxt = [l for l in texts[i + 1].splitlines() if l.strip()][:8]
            m = next((re.match(r"Figure ([0-9A-C]+\.\d+)", l) for l in nxt if re.match(r"Figure [0-9A-C]+\.\d+", l)), None)
            fid = num_to_id.get(m.group(1)) if m else None
            if not fid or fid not in metrics:
                bad.append((i + 1, round(empties[i], 2), "next page does not start with a figure"))
                continue
            if actions >= per_round:
                continue
            mt = metrics[fid]
            avail = empties[i] * content_px - 16
            need = mt["blockH"] - avail
            new_scale = mt["scale"] * (mt["imgH"] - need) / mt["imgH"]
            if need > 0 and new_scale >= mt["minScale"]:
                state["scale"][fid] = round(new_scale, 3)
                actions += 1
            elif movable_after(fid):
                state["defer"][fid] = state["defer"].get(fid, 0) + 1
                actions += 1
            else:
                bad.append((i + 1, round(empties[i], 2), f"{fid}: cannot shrink ({new_scale:.2f}) or float"))
        print(f"round {rnd}: pages {len(texts)}, actions {actions}, scale {len(state['scale'])}, defer {len(state['defer'])}, unresolved {bad}", flush=True)
        if actions == 0:
            return titles, bad
        DEFER = state["defer"]
        json.dump(state, open(OVERRIDES, "w"), indent=1)
        build_html()
    return titles, bad


def page_numbers(titles):
    texts = page_texts()
    norm = lambda s: re.sub(r"\s+", "", s)
    found = {}
    first = next(i for i, t in enumerate(texts) if "Whatthisrepositoryis" in norm(t))
    for i, t in enumerate(titles):
        key = norm(t)[:28]
        for pno in range(first, len(texts)):
            if key in norm(texts[pno]):
                found[i] = pno + 1
                break
    return found


def figs_on(text):
    return re.findall(r"Figure ([0-9A-C]+\.\d+) —", text)


def feedback(state, num_to_id, rounds=8):
    """Fix pages that are still more than a third empty, using the real PDF."""
    content_px = (PAGE_H - M_TOP - M_BOTTOM) / 25.4 * 96
    for rnd in range(rounds):
        texts, empties = page_texts(), empty_fractions()
        metrics = json.load(open(METRICS))
        bad = [i for i, e in enumerate(empties) if e > EMPTY_LIMIT - 0.01 and i < len(texts) - 1]
        print(f"feedback {rnd}: over-empty pages {[i + 1 for i in bad]}", flush=True)
        if not bad:
            return
        changed = False
        for i in bad:
            gap = empties[i] * content_px - 18
            head = [l for l in texts[i + 1].splitlines() if l.strip()][:4]
            nxt = next((figs_on(l)[0] for l in head if figs_on(l)), None)
            nid = num_to_id.get(nxt)
            done = False
            if nid and nid in metrics:
                m = metrics[nid]
                # headings above the figure travel with it
                extra = 0 if head and head[0].startswith("Figure") else 40
                need = m["blockH"] + extra - gap
                s_new = m["scale"] * (m["imgH"] - need) / m["imgH"] if m["imgH"] else 0
                if m.get("landscape"):
                    # bring it back to a portrait page: its text wraps more there
                    native_h = m["imgH"] / m["scale"]
                    target = gap - extra - (m["blockH"] - m["imgH"]) * 1.6
                    s_new = min(target / native_h, 1.0)
                    if s_new >= 0.55:
                        state["force"][nid] = round(s_new - 0.01, 3); done = changed = True
                        s_new = -1
                if s_new != -1 and need > 0 and s_new >= 0.55 and s_new >= 0.7 * m["scale"]:
                    state["force"][nid] = round(min(s_new, m["fit"]) - 0.01, 3); done = changed = True
            if not done:
                for num in reversed(figs_on(texts[i])):
                    fid = num_to_id.get(num)
                    m = metrics.get(fid)
                    if m and not m.get("landscape") and m["scale"] < m["fit"] - 0.02:
                        grow_px = gap * 0.9
                        s_new = min(m["fit"], m["scale"] * (m["imgH"] + grow_px) / m["imgH"])
                        state["force"][fid] = round(s_new, 3); done = changed = True
                        break
            if not done:
                print("   cannot fix page", i + 1)
        if not changed:
            return
        json.dump(state, open(OVERRIDES, "w"), indent=1)
        build_html()
        print_pdf()


if __name__ == "__main__":
    # fixed sizes: the two Start here diagrams, and one small diagram enlarged to fill its page
    state = {"scale": {"00-1-legend": 0.8, "05-1-master-map": 0.8}, "force": {"03-2-three-places": 1.22}, "defer": {}}
    json.dump(state, open(OVERRIDES, "w"))
    titles, figs = build_html()
    num_to_id = {f["num"]: f["id"] for f in figs if f["num"]}
    print_pdf()
    feedback(state, num_to_id)
    pages = page_numbers(titles)
    build_html(pages)
    print_pdf()
    final = page_numbers(titles)
    if final != pages:
        build_html(final); print_pdf(); final = page_numbers(titles)
    emp = empty_fractions()
    over = [(i + 1, round(e, 2)) for i, e in enumerate(emp) if e > EMPTY_LIMIT]
    print("pages:", len(emp), "| chapter starts:", final)
    print("pages more than 1/3 empty:", over)
