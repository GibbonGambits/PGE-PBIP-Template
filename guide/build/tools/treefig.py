"""Render folder trees from the inventory as HTML figure sources."""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from inventory import INV, safety
from htmlfig import page
ROOT = "/home/user/PGE-PBIP-Template"
CLS = {"G": "g", "A": "a", "R": "r"}
TREE_CSS = """<style>
.tree{font-size:15px;line-height:1.25}
.node{display:flex;align-items:center;margin:3px 0}
.lab{border:2px solid;border-radius:6px;padding:3px 8px;font-family:"DejaVu Sans Mono",monospace;font-size:14px;white-space:nowrap}
.desc{margin-left:10px;color:#334155;font-size:14px}
.guide{color:#94A3B8;font-family:"DejaVu Sans Mono",monospace;white-space:pre;font-size:14px}
.ai{outline:3px dashed #1D4ED8;outline-offset:1px}
</style>"""
def children(p):
    pre = "" if p == "" else p + "/"
    kids = [k for k in INV if k.startswith(pre) and "/" not in k[len(pre):]]
    return sorted(kids, key=lambda k: (not os.path.isdir(os.path.join(ROOT, k)), k.lower()))
def render(name, root, depth=99, width=1100, title=None, collapse=()):
    rows = []
    def walk(p, prefix, d):
        kids = children(p)
        for i, k in enumerate(kids):
            last = i == len(kids) - 1
            s, ai = safety(k)
            isdir = os.path.isdir(os.path.join(ROOT, k))
            lab = os.path.basename(k) + ("/" if isdir else "")
            guide = prefix + ("└── " if last else "├── ")
            desc = INV[k][1]
            hidden = isdir and (d >= depth or k in collapse)
            if hidden:
                n = sum(1 for x in INV if x.startswith(k + "/"))
                desc += f"  <i>({n} items inside, shown later)</i>"
            rows.append(f"<div class=node><span class=guide>{html.escape(guide)}</span><span class='lab {CLS[s]}{' ai' if ai else ''}'>{html.escape(lab)}</span><span class=desc>{desc}</span></div>")
            if isdir and not hidden:
                walk(k, prefix + ("    " if last else "│   "), d + 1)
    if root:
        s, ai = safety(root)
        rows.append(f"<div class=node><span class='lab {CLS[s]}{' ai' if ai else ''}'>{html.escape(root)}/</span><span class=desc>{INV[root][1]}</span></div>")
    else:
        rows.append("<div class=node><span class='lab n'>PGE-PBIP-Template/ (repository root)</span></div>")
    walk(root, "", 1)
    head = f"<h3 style='margin:0 0 8px 0'>{title}</h3>" if title else ""
    page(name, TREE_CSS + head + "<div class=tree>" + "".join(rows) + "</div>", width)

def render_subset(name, root, keep, collapse=(), width=1000):
    """keep(path)->bool decides which children are shown; collapse = folders shown closed."""
    rows = []
    def walk(p, prefix):
        kids = [k for k in children(p) if keep(k)]
        for i, k in enumerate(kids):
            last = i == len(kids) - 1
            s, ai = safety(k)
            isdir = os.path.isdir(os.path.join(ROOT, k))
            lab = os.path.basename(k) + ("/" if isdir else "")
            guide = prefix + ("└── " if last else "├── ")
            desc = INV[k][1]
            closed = isdir and k in collapse
            if closed:
                n = sum(1 for x in INV if x.startswith(k + "/"))
                desc += f"  <i>({n} items inside, shown in their own tree)</i>"
            rows.append(f"<div class=node><span class=guide>{html.escape(guide)}</span><span class='lab {CLS[s]}{' ai' if ai else ''}'>{html.escape(lab)}</span><span class=desc>{desc}</span></div>")
            if isdir and not closed:
                walk(k, prefix + ("    " if last else "│   "))
    if root:
        s, ai = safety(root)
        rows.append(f"<div class=node><span class='lab {CLS[s]}{' ai' if ai else ''}'>{html.escape(root)}/</span><span class=desc>{INV[root][1]}</span></div>")
    else:
        rows.append("<div class=node><span class='lab n'>PGE-PBIP-Template/ (repository root)</span></div>")
    walk(root, "")
    page(name, TREE_CSS + "<div class=tree>" + "".join(rows) + "</div>", width)
    return len(rows)
