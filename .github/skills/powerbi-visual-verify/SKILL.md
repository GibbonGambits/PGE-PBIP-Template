---
name: powerbi-visual-verify
description: 'Reviews rendered Power BI screenshots and maps defects to checklist-backed fixes for layout, interactions, accessibility, and formatting. Use when validating final render quality after PBIR/TMDL changes.'
---

# Power BI Visual Verify (Copilot)

Use this skill to verify rendered output, not just JSON validity.

## Repository conventions

- SVG-header mode is default.
- Visual-title mode is allowed when explicitly needed and documented in the active page spec.
- Findings must be reported by page display name.

## Checklist sources

- [Report Design and Interactions](../../../docs/checklists/report-design-and-interactions.md)
- [Accessibility and Performance](../../../docs/checklists/accessibility-and-performance.md)
- [Security, Governance, Testing, and Documentation](../../../docs/checklists/security-governance-testing-documentation.md) (user-readiness rows when relevant)
- [Theme source and deployable copy](../../../docs/theme/README.md)

## Procedure

1. Review all screenshots for the changed pages.
2. Score relevant rows as Pass / Needs Work / N/A.
3. For each defect, cite the row, threshold, and visible evidence.
4. Recommend source-level fixes (PBIR/TMDL/build script), never image edits.
5. Re-verify after fixes and report residual issues.

Theme-specific verification checks:
- Confirm a deliberately applied theme exists (checklist row 51).
- Check for white-on-white or low-contrast series outcomes when background is white (rows 67, 71, 75).
- Verify repeated metric formats stay consistent after theme changes (row 72).
- If theme source changed, confirm the deployable copy is schema-compliant and that legacy `good`/`bad` fields were normalized during promotion.

## Output format

| Page | Row | Status | Visual evidence | Threshold/standard | Recommended source fix |
|---|---:|---|---|---|---|
