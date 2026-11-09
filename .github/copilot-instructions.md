# Copilot instructions — PBIP Agentic BI Starter Pack

GitHub Copilot loads this file automatically. This is the **primary Copilot instruction file** for this repository.

Use `copilot-instructions.md` in the repository root as deep PBIP reference material when implementation detail is needed, but keep Copilot-facing policy here to avoid duplicate Copilot instruction files.

## Before generating dashboard pages on an initial prompt

Ask the user: `Do you want a Documentation page also?` — then follow the *Mandatory Clarification Question* section in [copilot-instructions.md](../copilot-instructions.md).

## Non-negotiable guardrails

1. New business measures go in `_Measures`; keep existing legacy measure homes unless migration is explicitly approved.
2. SVG KPI measures go in `_SVG_Measures` only, named by page (`P1_...`, `P2_...`).
3. SVG backgrounds and custom themes live in `Template.Report/StaticResources/RegisteredResources/` and must be registered in `report.json`.
4. Follow the PBIP schema and property constraints in [copilot-instructions.md](../copilot-instructions.md) exactly — including forbidden properties.
5. Write `.tmdl` as UTF-8 **without BOM**, and never use inline `//` comments in TMDL.
6. Prefer context-appropriate formatting: whole numbers where appropriate, but allow justified decimals, currency, and percentages. Keep repeated metrics consistently formatted.
7. SVG KPI cards use the image visual pattern (`sourceType='imageData'`, measure in `sourceField`).
8. Generate fake CSV data with Python (numpy + pandas), no venv.
9. Never call a page done on JSON validity alone — verify what Power BI actually rendered.
10. Give every measure a `description`.
11. Keep SVG-header mode as default; visual-title mode is allowed when needed and documented in the page spec.
12. Treat `docs/theme/Theme.json` as source input; generate a separate schema-compliant deployable theme copy before any report registration.

## Where things live

| | |
| --- | --- |
| Copilot primary steering file | `.github/copilot-instructions.md` |
| PBIP deep reference | `copilot-instructions.md` (root) |
| Scoped instructions (`applyTo` globs) | `.github/instructions/*.instructions.md` |
| Agent modes | `.github/agents/*.agent.md` |
| Copilot skills | `.github/skills/*/SKILL.md` |
| Checklist standards | `docs/checklists/*.md` |
| Theme source + deployable copy | `docs/theme/Theme.json` + `docs/theme/Theme.deployable.json` |
| Per-dashboard specs | `specs/` — write one before building a new page |
| How the context layers fit together | `docs/AI-CONTEXT.md` |

## Checklist standards (modeled from `vscodePowerBI_Modeling_Full_Checklist_Guide.xlsx`)

Use focused checklist files instead of one monolithic checklist:

- `docs/checklists/power-query-and-data-sources.md`
- `docs/checklists/semantic-model-and-relationships.md`
- `docs/checklists/dax-and-measures.md`
- `docs/checklists/report-design-and-interactions.md`
- `docs/checklists/accessibility-and-performance.md`
- `docs/checklists/security-governance-testing-documentation.md` (includes optional decommission planning)

Each checklist item preserves:
- when-applicable conditions
- Mark N/A when conditions
- quantitative thresholds
- Microsoft Learn links

## Theme governance (`docs/theme/Theme.json`)

Use `docs/theme/Theme.json` as the editable source of truth. Do not register it directly in report metadata unless it is promoted into a compliant deployable copy.

Promotion rules:
- `good` / `bad` are allowed as legacy source fields and must be normalized to deployable fields:
  - `maximum <- good`
  - `minimum <- bad`
  - ensure `null` exists (set intentionally)
- Reorder `dataColors` so `#FFFFFF` is not a default series color.
- Preserve white for backgrounds/text where appropriate (`background`, text classes, and style objects).
- Emit a separate schema-compliant deployable file under `docs/theme/` and use that artifact for downstream registration.

For Copilot execution, use `.github/skills/powerbi-theme-governance/SKILL.md`.

## Validation

```powershell
powershell -NoProfile -File scripts\validate-json.ps1
powershell -NoProfile -File scripts\validate-pbip.ps1
```

Rendered-output verification runs through the Power BI Desktop Bridge (`scripts\Test-PbipBridge.ps1`, `scripts\Invoke-PbipVerify.ps1`). Run it manually and review the PNGs in `tests/screenshots/` against `.github/skills/powerbi-visual-verify/SKILL.md` before calling a page done.
