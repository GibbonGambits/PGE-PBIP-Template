---
name: powerbi-modeling
description: 'Power BI semantic modeling assistant for building and reviewing semantic models with checklist-based standards. Use when creating measures, designing relationships, tuning model structure, or validating model quality in PBIP.'
---

# Power BI Semantic Modeling (Copilot)

Use this skill for semantic-model authoring and review with focused checklist standards.

## Repository rules to apply first

- Use `.github/copilot-instructions.md` as the primary Copilot instruction file.
- New business measures go in `_Measures`.
- Keep existing legacy measure home tables unless migration is explicitly approved.
- SVG KPI measures stay in `_SVG_Measures` with page-prefixed naming.
- Use context-appropriate numeric formats (whole/decimal/currency/percent) and keep repeated metrics consistent.
- For theme normalization/promotion work, route to `.github/skills/powerbi-theme-governance/SKILL.md`.

## Checklist sources

- [Power Query and Data Sources](../../../docs/checklists/power-query-and-data-sources.md)
- [Semantic Model and Relationships](../../../docs/checklists/semantic-model-and-relationships.md)
- [DAX and Measures](../../../docs/checklists/dax-and-measures.md)
- [Security, Governance, Testing, and Documentation](../../../docs/checklists/security-governance-testing-documentation.md)

## Procedure

1. Inspect the model first (`Template.SemanticModel/definition/` or modeling MCP when available).
2. Select only relevant checklist rows.
3. Score each row as **Pass / Needs Work / N/A**.
4. For **N/A**, copy the applicable "Mark N/A when" reasoning.
5. For **Needs Work**, include the exact threshold and remediation.
6. Keep report-specific business definitions out of global instructions unless already standardized.

## Output format

Use this table:

| Row | Area | Status | Evidence | Threshold impact | Action |
|---:|---|---|---|---|---|
