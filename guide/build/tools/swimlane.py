"""Top-to-bottom swimlane diagrams as inline SVG inside HTML (rendered by render-html.mjs).
lanes: [(name, cls)], steps: [(lane_index, number, text)]"""
import html, textwrap
from htmlfig import page
FILL = {"you": ("#EDE9FE", "#6D28D9", "#3B0764"), "n": ("#F1F5F9", "#475569", "#0F172A"),
        "ai": ("#DBEAFE", "#1D4ED8", "#1E3A8A"), "r": ("#FEE2E2", "#B91C1C", "#7F1D1D"),
        "ext": ("#E0F2FE", "#0369A1", "#0C4A6E"), "g": ("#DCFCE7", "#15803D", "#14532D"),
        "a": ("#FEF3C7", "#B45309", "#78350F")}
def swimlane(name, lanes, steps, lane_w=200, box_w=184, line_h=19, wrap=20, gap=26):
    W = lane_w * len(lanes) + 2; top = 56
    # compute box heights
    boxes = []
    y = top + 10
    for lane, num, text in steps:
        lines = textwrap.wrap(text, wrap, break_long_words=False)
        h = 18 + line_h * len(lines) + 8
        x = lane * lane_w + (lane_w - box_w) / 2
        boxes.append((x, y, h, lane, num, lines))
        y += h + gap
    H = y + 4
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="DejaVu Sans, Arial, sans-serif">',
         '<defs><marker id="ar" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="9" refX="10" refY="4.5" orient="auto"><path d="M0,0 L11,4.5 L0,9 z" fill="#334155"/></marker></defs>']
    for i, (ln, cls) in enumerate(lanes):
        f, st, tx = FILL[cls]
        bg = "#F8FAFC" if i % 2 == 0 else "#FFFFFF"
        s.append(f'<rect x="{i*lane_w}" y="0" width="{lane_w}" height="{H}" fill="{bg}" stroke="#CBD5E1"/>')
        s.append(f'<rect x="{i*lane_w+6}" y="6" width="{lane_w-12}" height="40" rx="8" fill="{f}" stroke="{st}" stroke-width="2"/>')
        s.append(f'<text x="{i*lane_w+lane_w/2}" y="32" text-anchor="middle" font-size="15" font-weight="bold" fill="{tx}">{html.escape(ln)}</text>')
    # connectors (down, across, down) drawn first
    for a, b in zip(boxes, boxes[1:]):
        x1 = a[0] + box_w / 2; y1 = a[1] + a[2]; x2 = b[0] + box_w / 2; y2 = b[1]
        ym = y1 + gap / 2
        s.append(f'<path d="M{x1},{y1} L{x1},{ym} L{x2},{ym} L{x2},{y2-1}" fill="none" stroke="#334155" stroke-width="1.6" marker-end="url(#ar)"/>')
    for x, y, h, lane, num, lines in boxes:
        f, st, tx = FILL[lanes[lane][1]]
        s.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="{h}" rx="7" fill="{f}" stroke="{st}" stroke-width="2"/>')
        s.append(f'<circle cx="{x+13}" cy="{y}" r="12" fill="#0F172A"/><text x="{x+13}" y="{y+4.5}" text-anchor="middle" font-size="12" font-weight="bold" fill="#fff">{num}</text>')
        for k, t in enumerate(lines):
            s.append(f'<text x="{x+box_w/2}" y="{y+30+k*line_h}" text-anchor="middle" font-size="14" fill="{tx}">{html.escape(t)}</text>')
    s.append('</svg>')
    page(name, "".join(s), width=W)
