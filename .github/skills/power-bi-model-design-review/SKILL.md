---
name: power-bi-model-design-review
description: 'Reviews an existing Power BI semantic model against reusable checklist standards for schema, relationships, DAX, governance, and maintainability. Use for health checks, release readiness reviews, and inherited-model audits.'
---

# Power BI Model Design Review (Copilot)

Use this skill for structured model audits.

## Checklist sources

- [Semantic Model and Relationships](../../../docs/checklists/semantic-model-and-relationships.md)
- [DAX and Measures](../../../docs/checklists/dax-and-measures.md)
- [Power Query and Data Sources](../../../docs/checklists/power-query-and-data-sources.md)
- [Security, Governance, Testing, and Documentation](../../../docs/checklists/security-governance-testing-documentation.md)
- [Accessibility and Performance](../../../docs/checklists/accessibility-and-performance.md) (performance-related rows only when relevant)
- [Theme source and deployable copy](../../../docs/theme/README.md) (for cross-layer UX/governance checks)

## Review rules

- Preserve each row's "When applicable", "Mark N/A when", and threshold logic.
- Do not fail an item just because a pattern is absent when the row itself allows N/A.
- Treat justified exceptions as valid only when rationale is documented.
- When theme choices undermine readability, accessibility, or consistency, flag the issue and route remediation to visual verification/theme governance skills.

## Procedure

1. Baseline model structure, relationships, and key measures.
2. Run checklist rows by relevance and mark Pass / Needs Work / N/A.
3. Prioritize findings by user impact and threshold severity.
4. Provide remediation in dependency order (foundational model issues first).
5. Include cross-layer findings when model semantics and theme/visual consumption conflict (for example, low-contrast KPI semantics or inconsistent comparable metric formats).

## Output format

| Priority | Row | Status | Finding | Why it matters | Recommended change |
|---|---:|---|---|---|---|
