# Theme governance (`docs/theme`)

This folder separates editable theme source from deployable theme output.

## Files

- `Theme.json` — source file for palette and styling decisions (may include legacy fields such as `good` / `bad`).
- `Theme.deployable.json` — schema-compliant deployable copy produced from `Theme.json`.

## Promotion rules

When promoting source to deployable:

1. Keep `Theme.json` as the source of truth.
2. Normalize legacy semantic fields:
   - `maximum <- good`
   - `minimum <- bad`
   - ensure `null` exists.
3. Reorder `dataColors` so `#FFFFFF` is not the default series color.
4. Preserve white where appropriate for backgrounds/text.
5. Emit deployable output with allowed root keys only:
   - `name`, `dataColors`, `background`, `foreground`, `tableAccent`,
     `maximum`, `minimum`, `null`, `textClasses`, `visualStyles`.

## Checklist alignment

- [Report Design and Interactions](../checklists/report-design-and-interactions.md) — rows 51, 71, 72, 75
- [Accessibility and Performance](../checklists/accessibility-and-performance.md) — row 67

## Notes

- This process prepares theme artifacts only.
- PBIP report/model artifact registration is downstream work and should be handled separately.
