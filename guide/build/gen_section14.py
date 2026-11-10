"""Generate guide/14-file-directory.md and its folder-tree figures from inventory.py + details.py."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "tools"))
from inventory import INV, safety, NAMES
from details import D
import treefig
ROOT = "/home/user/PGE-PBIP-Template"
P = ".github/skills/powerbi-pbiviz-custom-visuals"
isdir = lambda p: os.path.isdir(os.path.join(ROOT, p))
def under(base):
    return lambda k: k == base or k.startswith(base + "/")
GROUPS = [
 ("Root files", "", lambda k: not isdir(k), (), "The nine files that sit directly in the repository's top folder."),
 ("Root folders", "", lambda k: isdir(k), {k for k in INV if "/" not in k and isdir(k)}, "The nine top-level folders, each opened in its own tree below."),
 (".github: top level", ".github", lambda k: True, {".github/agents", ".github/instructions", ".github/skills"}, "GitHub's own configuration, plus the folders the AI agent reads."),
 (".github/agents and .github/instructions", None, None, None, "Expert modes and file-type rules for GitHub Copilot."),
 (".github/skills, part 1", ".github/skills", lambda k: k == ".github/skills/README.md" or k.split("/")[2] in ("power-bi-model-design-review", "power-bi-performance-troubleshooting", "powerbi-dashboard-header", "powerbi-fieldparameter"), set(), "The skills index and the first four skills."),
 (".github/skills, part 2", ".github/skills", lambda k: k.split("/")[2] in ("powerbi-modeling", "powerbi-theme-governance", "powerbi-visual-verify", "powerbi-pbiviz-custom-visuals"), {P}, "Three more skills, and the custom-visual kit, which gets its own trees."),
 ("Custom-visual kit: project files and tools", P + "/assets", lambda k: k.split("/")[4] in ("project", "tools"), set(), "The base project every visual starts from, and the three kit scripts."),
 ("Custom-visual kit: shared library", P + "/assets/shared", lambda k: True, set(), "Code shared by every custom visual."),
 ("Custom-visual kit: templates, blank", P + "/assets/templates", under(P + "/assets/templates/blank"), set(), "The templates folder and the minimal 'blank' starter visual."),
 ("Custom-visual kit: templates, varianceChart", P + "/assets/templates", under(P + "/assets/templates/varianceChart"), set(), "The IBCS period-chart starter visual (same six-item layout)."),
 ("Custom-visual kit: templates, varianceTable", P + "/assets/templates", under(P + "/assets/templates/varianceTable"), set(), "The IBCS statement-table starter visual (same six-item layout)."),
 ("Custom-visual kit: SKILL.md and references", P, lambda k: not k.endswith("/assets"), set(), "The skill procedure and its eight reference documents."),
 ("Template.Report: definition", "Template.Report", lambda k: not k.startswith("Template.Report/StaticResources"), set(), "The report's pointer file, ID card and definition files."),
 ("Template.Report: StaticResources", "Template.Report/StaticResources", lambda k: True, set(), "Themes and images used by the report."),
 ("Template.SemanticModel", "Template.SemanticModel", lambda k: True, set(), "The data model, as TMDL text files."),
 ("docs: guides", "docs", lambda k: True, {"docs/checklists"}, "Human guides, the theme source, and the checklists folder."),
 ("docs/checklists", "docs/checklists", lambda k: True, set(), "Six focused quality checklists and their index."),
 ("python", "python", lambda k: True, set(), "Optional Python guidance; no scripts ship here."),
 ("scripts", "scripts", lambda k: True, {"scripts/hooks"}, "PowerShell validation and verification scripts."),
 ("scripts/hooks", "scripts/hooks", lambda k: True, set(), "The four hook wrapper scripts."),
 ("specs", "specs", lambda k: True, set(), "Plans for one dashboard or page at a time."),
 ("tests: prompts", "tests", lambda k: not k.startswith("tests/results"), set(), "The tests folder, its guide and the three AI prompts."),
 ("tests/results", "tests/results", lambda k: True, set(), "Generated test reports (Red: written by scripts)."),
]
def order(root, keep, collapse):
    out = []
    def walk(p):
        for k in [x for x in treefig.children(p) if keep(x)]:
            out.append(k)
            if isdir(k) and k not in collapse:
                walk(k)
    walk(root)
    return out
os.chdir(os.path.join(ROOT, "guide", "images"))
md = ["# 14. File-by-file directory", "",
"Every one of the repository's 176 files and folders, grouped by folder. Each group opens with a folder-tree diagram coloured with the safety legend from Section 00 (fill colour = safety; blue dashed outline = AI agent file). Under each tree, the numbered entries follow the tree from top to bottom and give:",
"", "- the **exact path** and its **safety flag**;", "- **What it is:** a plain-English summary with a real-world comparison;", "- **Technical role:** what the file does for the tools.", "",
"Folders that appear closed in one tree are opened in their own tree, and their entry appears there.", ""]
seen = []
fig = 0
for title, root, keep, collapse, intro in GROUPS:
    if root is None:  # special: agents + instructions as one tree from .github
        root = ".github"; keep = lambda k: k.startswith(".github/agents") or k.startswith(".github/instructions"); collapse = set()
        entries = order(root, keep, collapse)
    else:
        entries = order(root, keep, collapse)
        if root and root not in seen:
            entries = [root] + entries
    entries = [e for e in entries if not (e in collapse)]
    fig += 1
    name = f"14-{fig:02d}-tree"
    treefig.render_subset(name, root, keep, collapse=collapse, width=1000)
    md += [f"## 14.{fig} {title}", "", f"![Folder tree: {title}](images/{name}.png)", "",
           f"**Figure 14.{fig} — {title}.** {intro}", "", f"Walkthrough of Figure 14.{fig}:", ""]
    for i, p in enumerate(entries, 1):
        s, ai = safety(p)
        tag = f"**{NAMES[s]}**" + (" · **AI file**" if ai else "")
        slash = "/" if isdir(p) else ""
        what, role = D[p]
        esc = lambda t: t.replace("*", "\\*").replace("<", "&lt;")
        what, role = esc(what), esc(role)
        md += [f"{i}. `{p}{slash}` — {tag}", f"   - *What it is:* {what}", f"   - *Technical role:* {role}"]
        seen.append(p)
    md.append("")
missing = sorted(set(INV) - set(seen)); dup = sorted({x for x in seen if seen.count(x) > 1})
md += ["---", "", f"**Coverage check:** {len(set(seen))} of {len(INV)} items listed above."]
open(os.path.join(ROOT, "guide", "14-file-directory.md"), "w").write("\n".join(md) + "\n")
print("figures", fig, "entries", len(seen), "unique", len(set(seen)), "missing", missing, "dup", dup)
