# Semantic Model and Relationships Checklist

Focused standards for model architecture, keys, relationships, and author-facing model structure.

Use each item as **Pass / Needs Work / N/A**.

## Model structure and relationships

### Row 11
- Check: Assess whether the model follows a star-schema-friendly design where practical: fact tables for events/observations, dimensions for filtering/grouping, and snowflaking only when it clearly helps more than it hurts.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema
- When applicable: the report uses a semantic model with relationships and reusable fields
- Guidance: focus on whether the chosen structure improves usability and correctness for this report, not on blindly forcing a textbook pattern
- Quantitative threshold: 0 fact-to-fact relationships unless justified
- Quantitative threshold: 0 snowflake chains longer than 1 hop unless justified

### Row 12
- Check: Assess whether relationship cardinality is appropriate, preferring one-to-many where the business grain supports it.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships
- When applicable: the report model has relationships between reusable entities
- Guidance: only flag many-to-many as an issue when it is avoidable or unjustified for the business requirement
- Quantitative threshold: 100% of one-side relationship keys must be unique
- Quantitative threshold: 0 avoidable many-to-many relationships

### Row 13
- Check: Assess whether relationship direction and filter propagation are correct, and whether bi-directional filtering is minimized and justified when used.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/relationships-bidirectional-filtering
- When applicable: the report relies on model relationships for filter behavior
- Guidance: record active filter directions and why any bi-directional relationships are required
- Quantitative threshold: target 0 bi-directional relationships
- Quantitative threshold: 1 bi-directional relationship requires review; 2 or more require strong justification

### Row 14
- Check: Assess whether inactive relationships are needed for alternate contexts (for example: multiple date roles) and whether measures use them cleanly with USERELATIONSHIP where appropriate.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/relationships-active-inactive
- When applicable: multiple valid filter paths exist and must be activated deliberately
- Mark N/A when: the model has only one relevant path/context
- Guidance: do not mark this incomplete simply because inactive relationships are absent

### Row 15
- Check: Assess whether key design is appropriate for the model.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/star-schema
- When applicable: the report depends on dimensional joins or key-based relationships
- Mark N/A when: this concern is handled upstream or is not material to the report design
- Guidance: prefer stable unique keys and avoid fragile concatenated keys unless clearly justified
- Quantitative threshold: 0 concatenated relationship keys unless justified
- Quantitative threshold: 0 nulls on one-side relationship keys
- Quantitative threshold: many-side key null rate should be <=0.1% unless intentionally allowed

### Row 16
- Check: Assess whether role-playing dimensions are needed (for example: Order Date vs Ship Date).
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/relationships-active-inactive
- When applicable: the report analyzes the same business entity in multiple valid roles/contexts
- Mark N/A when: the report has only one relevant date/context path
- Guidance: separate dimension instances or alternate patterns are useful only when the business meaning actually differs
- Quantitative threshold: 2 or more distinct business date meanings = role-playing design or explicit alternate context pattern required
- Quantitative threshold: 2 or more active analytical date roles on the same fact = review required

### Row 17
- Check: Assess whether Composite models and DirectQuery are used only when necessary, and whether the trade-offs are documented.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/composite-model-guidance
- When applicable: the report mixes storage modes, requires near-real-time access, or cannot reasonably import the required data
- Mark N/A when: the report is a clean import design and DirectQuery is not needed
- Guidance: mark Yes for a deliberate import design when it satisfies the requirement
- Quantitative threshold: freshness requirement <=15 minutes or near-real-time access may justify DirectQuery/composite
- Quantitative threshold: interactive visual latency target above 2 seconds in import due to size/freshness constraints = review storage mode choice

### Row 18
- Check: Assess whether aggregations are needed for DirectQuery or very large models.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/aggregations-advanced
- When applicable: the report has large detail tables, repeated slow detail queries, or DirectQuery workloads that would benefit
- Mark N/A when: the model is import-only, already summarized appropriately, or too small/simple to benefit
- Guidance: do not force aggregation tables where scale does not justify them
- Quantitative threshold: fact table >=50 million rows = review aggregations
- Quantitative threshold: DirectQuery detail queries repeatedly >2 seconds = review aggregations

### Row 19
- Check: Assess whether Auto Date-Time is disabled and whether a deliberate date-table strategy is used instead.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/auto-date-time
- When applicable: the report uses dates for filtering, grouping, or time intelligence
- Guidance: verify that hidden auto date tables are not creating clutter or conflicting date behavior

### Row 20
- Check: Assess whether technical-only keys, helper columns, sort-by columns, and duplicate raw columns should be hidden from Report view.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization
- When applicable: the field is truly technical-only for report authors
- Guidance: do not mark this as an issue just because a field looks technical; if authors genuinely need it for visuals, export, drillthrough, reconciliation, or troubleshooting, keeping it visible can be correct
- Quantitative threshold: 100% of visible technical-looking fields must have a valid use case (visual, export, drillthrough, reconciliation, or troubleshooting)
- Quantitative threshold: review when 1 or more visible technical-only fields have no real author/support use case

## Tables and columns

### Row 23
- Check: Assess whether display folders are used where they materially improve discoverability for report authors.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/model-explorer
- When applicable: the model exposes enough measures or reusable attributes that the field list becomes hard to navigate
- Mark N/A when: the model is small enough that folders add little value or create unnecessary nesting
- Guidance: prefer simple, business-oriented folder groupings rather than deep technical folder trees
- Quantitative threshold: 10 or more visible measures in one table = review display folders
- Quantitative threshold: 20 or more visible author-facing fields in one table = folders should be considered

### Row 24
- Check: Assess whether descriptive metadata is filled out for visible tables, columns, measures, hierarchies, and other author-facing elements.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/model-explorer
- When applicable: report authors or support staff will browse the model directly
- Mark N/A when: the model is tiny and the visible elements are fully self-explanatory
- Guidance: prioritize visible measures, KPI fields, calculated fields, and any non-obvious business terms
- Quantitative threshold: 100% of visible measures should have descriptions
- Quantitative threshold: 100% of visible non-obvious author-facing fields should have descriptions

### Row 25
- Check: Assess whether Sort by Column is set correctly for labels that have a business order different from alphabetical order.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-sort-by-column
- When applicable: the report contains month names, weekday names, bands, stages, fiscal periods, or other ordered labels
- Mark N/A when: all displayed labels are naturally sorted as-is
- Guidance: review visible ordered labels, including custom categories and staged process values
- Quantitative threshold: 100% of displayed ordinal labels should have correct Sort by Column set
- Quantitative threshold: 0 visibly mis-sorted month/day/band labels

### Row 26
- Check: Assess whether only necessary author-facing columns are exposed in Report view and whether unused columns are hidden.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization
- When applicable: the model is intended for report authoring, self-service, or shared semantic use
- Mark N/A when: a visible field is genuinely needed for visuals, export, drillthrough, reconciliation, troubleshooting, or support workflows
- Guidance: do not hide fields only because they look technical; hide them only when they are truly unnecessary for authors
- Quantitative threshold: 0 clearly unused visible columns unless justified
- Quantitative threshold: 100% of visible technical-looking fields should have a documented author/support use case

### Row 27
- Check: Assess whether applicable data categories are set for fields such as URL, image, address, city, country, latitude, and longitude.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-data-categorization
- When applicable: the model exposes fields used in maps, links, images, or geospatial visuals
- Mark N/A when: the report has no fields where data categorization affects behavior
- Guidance: review author-facing geo, URL, and image fields; do not over-categorize fields that do not need it
- Quantitative threshold: 100% of author-facing geo, URL, and image fields should have correct categories
- Quantitative threshold: 0 map-critical latitude/longitude fields left uncategorized

