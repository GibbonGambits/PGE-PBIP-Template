---
name: power-bi-performance-troubleshooting
description: 'Diagnoses slow Power BI models and reports using checklist thresholds for page density, slicers, DAX, and query reduction. Use when visuals are slow, pages queue, or interaction latency is high.'
---

# Power BI Performance Troubleshooting (Copilot)

Use this skill for bottleneck-first triage.

## Checklist sources

- [Accessibility and Performance](../../../docs/checklists/accessibility-and-performance.md)
- [Report Design and Interactions](../../../docs/checklists/report-design-and-interactions.md) (interaction/query behavior rows)
- [Semantic Model and Relationships](../../../docs/checklists/semantic-model-and-relationships.md) (storage/relationship contributors)
- [DAX and Measures](../../../docs/checklists/dax-and-measures.md) (DAX contributors)

## Primary thresholds to enforce

- Repeated interactions: `<100 ms excellent`, `100-1000 ms acceptable`, `>1000 ms investigate`.
- DAX query time `>1000 ms`: treat as model/DAX review candidate.
- Other/queueing `>500 ms`: review page density and render order.
- Slicer and visual-density thresholds from the checklist are mandatory review triggers.

## Procedure

1. Capture evidence first (Performance Analyzer and observed interactions).
2. Classify delays: DAX query vs visual rendering vs Other/queueing.
3. Map bottlenecks to checklist rows and thresholds.
4. Propose minimal, ordered fixes and expected performance effect.
5. Re-test and report before/after timings.

## Output format

| Symptom | Row | Current value | Threshold | Root cause hypothesis | Fix |
|---|---:|---|---|---|---|

