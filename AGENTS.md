# AGENTS.md

Universal entry point for GitHub Copilot workflows in this repository. Keep it short — Copilot policy lives in `.github/copilot-instructions.md`, while `copilot-instructions.md` is detailed PBIP reference material.

## What this repo is

A Power BI PBIP starter template for agentic dashboard development. Reports and semantic models are source-controlled as plain files (`Template.Report/` PBIR JSON, `Template.SemanticModel/` TMDL), built by agents, and verified against what Power BI Desktop actually rendered — not against JSON validity.

## Rule precedence

For GitHub Copilot, `.github/copilot-instructions.md` is the primary policy authority.  
`copilot-instructions.md` is the detailed PBIP reference for implementation mechanics.  

## Non-negotiable guardrails

1. New business measures go in `_Measures`; keep existing legacy measure homes unless migration is explicitly approved.
2. SVG KPI measures go in `_SVG_Measures` only, named by page (`P1_...`, `P2_...`).
3. SVG backgrounds and custom themes live in `Template.Report/StaticResources/RegisteredResources/` and must be registered in `report.json`.
4. Follow `.github/copilot-instructions.md` for Copilot policy, and use `copilot-instructions.md` for detailed PBIP schema/property constraints (including forbidden properties).
5. Write `.tmdl` as UTF-8 **without BOM**, and never use inline `//` comments in TMDL.
6. Use context-appropriate formatting (whole numbers where appropriate; justified decimals/currency/percentages allowed), while keeping repeated metrics consistent and applying thousand separators where relevant.
7. SVG KPI cards use the image visual pattern (`sourceType='imageData'`, measure in `sourceField`).
8. Generate fake CSV data with Python (numpy + pandas), no venv.
9. Never call a page done on JSON validity alone — verify the rendered screenshot against `.github/skills/powerbi-visual-verify/SKILL.md`.
10. Give every measure a `description`. The model is context for the next agent and for Copilot/data agents; an undocumented measure is a measure someone will duplicate.

## How work is organised

Three layers, deliberately separate. `docs/AI-CONTEXT.md` explains why.

| Layer | Answers | Where |
| --- | --- | --- |
| **Steering** | How we always build | `.github/copilot-instructions.md` (Copilot primary policy), `copilot-instructions.md` (detailed reference), this file, `.github/instructions/*.instructions.md` |
| **Specs** | What we are building, this once | `specs/` — one file per dashboard or page |
| **Hooks** | What runs, and when | `scripts/hooks/` wrappers + `scripts/Invoke-PbipVerify.ps1` (manual execution) |

**Write a spec before building a new dashboard or page.** Copy `specs/TEMPLATE.md`, fill it in, build against it. When the page renders clean, fold any rule that will apply to the *next* dashboard back into `.github/copilot-instructions.md` (Copilot policy) and keep `copilot-instructions.md` aligned as detailed reference material — specs are disposable, steering is not.

## Verification is part of building

Every report or model edit ends in the Desktop Bridge loop:

```
edit PBIR/TMDL → validate → reload Desktop → screenshot every page → review PNGs → fix
```

Run the verification loop manually and block completion until the screenshots have been reviewed. Preflight with `powershell -NoProfile -File scripts\Test-PbipBridge.ps1`. If the bridge is unavailable the loop fails open — say the report was not visually verified rather than claiming it renders correctly.

On a **first build**, Power BI Desktop often refuses to load the PBIP at all and leaves the window on *Untitled*. That is a load error, not a broken bridge, and *continue with errors* is not a fix. The bridge cannot read that dialog — run `scripts\Test-PbipSemantics.ps1` to find the cause in the source. A reload can raise a second dialog, *"Your report has issues that could not be resolved"* - a PBIR schema fault, usually a malformed filter. Screenshots taken after pressing *Continue* on it are **untrusted**: the failing objects are silently dropped. See *Known caveats* in `.github/skills/powerbi-visual-verify/SKILL.md`.

## Before you finish

- `powershell -NoProfile -File scripts\validate-json.ps1`
- `powershell -NoProfile -File scripts\validate-pbip.ps1`
- `powershell -NoProfile -File scripts\Test-PbipSemantics.ps1` — the load-time errors Desktop reports as a dialog, found in source
- Screenshots reviewed, findings reported by page **display name** (not page id).
