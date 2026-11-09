---
name: powerbi-theme-governance
description: 'Normalizes and promotes docs/theme/Theme.json into a schema-compliant deployable theme copy for Copilot workflows. Use when updating palette, typography, semantic colors, or preparing a theme for PBIP registration.'
---

# Power BI Theme Governance (Copilot)

Use this skill to manage theme source vs deployable artifacts safely and consistently.

## Scope

- Source file: `docs/theme/Theme.json`
- Deployable output: `docs/theme/Theme.deployable.json`
- This skill does not require PBIP artifact edits; it prepares a compliant theme artifact for downstream use.

## Promotion policy

1. Keep `Theme.json` as editable source of truth.
2. Normalize legacy semantic keys:
   - `good -> maximum`
   - `bad -> minimum`
   - ensure `null` exists
3. Reorder `dataColors` so `#FFFFFF` is not the default series color.
4. Preserve white for intended background/text usage.
5. Emit a separate deployable copy with schema-compliant root keys only.

## Allowed deployable root keys

- `name`
- `dataColors`
- `background`
- `foreground`
- `tableAccent`
- `maximum`
- `minimum`
- `null`
- `textClasses`
- `visualStyles`

## Checklist alignment

- [Report Design and Interactions](../../../docs/checklists/report-design-and-interactions.md) — rows 51, 71, 72, 75
- [Accessibility and Performance](../../../docs/checklists/accessibility-and-performance.md) — row 67

## Procedure

1. Read `docs/theme/Theme.json`.
2. Produce normalized `Theme.deployable.json` from source.
3. Validate:
   - root keys are compliant
   - `#FFFFFF` is not first in `dataColors`
   - `maximum`, `minimum`, `null` are present
4. Record any unresolved semantic/color accessibility risks as checklist findings.

## Output format

| Check | Status | Evidence | Required action |
|---|---|---|---|

