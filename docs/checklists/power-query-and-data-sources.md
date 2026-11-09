# Power Query and Data Sources Checklist

Focused standards from the modeling checklist for source connectivity, query shaping, typing, and parameter strategy.

Use each item as **Pass / Needs Work / N/A**.

### Row 2
- Check: Assess whether source connections should be parameterized for environment switching (for example: server, database, workspace, file path, URL, date boundary).
- Microsoft Learn: https://learn.microsoft.com/en-us/power-query/power-query-query-parameters
- When applicable: the same report/model must move across environments or source boundaries without code edits
- Mark N/A when: the report intentionally targets one fixed source/environment and parameterization would add complexity without a deployment benefit
- Guidance: record the connection types reviewed and whether parameters are truly needed for this report
- Quantitative threshold: 2 or more environments (for example: Dev/Test/Prod) = parameterization expected
- Quantitative threshold: 2 or more source endpoints, workspaces, databases, URLs, or file paths for the same report = parameterization expected

### Row 3
- Check: Assess whether the model avoids local file system data sources (for example: desktop file paths) unless a gateway-backed design is explicitly intended.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-onprem

### Row 4
- Check: Assess whether query folding is preserved where possible and whether expensive non-folding steps are pushed late.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/power-query-folding
- When applicable: the connector supports folding or source pushdown
- Mark N/A when: folding does not apply (for example: flat files, static tables, or connectors that do not support it)
- Guidance: state which steps can fold, where row/column reduction occurs, and which non-folding steps are justified
- Quantitative threshold: 0 known non-folding steps before the first major row filter or column reduction is preferred
- Quantitative threshold: 100% of easy pushdown steps (row filters, column selection, simple renames/types) should occur before any known non-folding step

### Row 5
- Check: Assess whether a Staging → Reference pattern is actually warranted.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/power-query-referenced-queries
- When applicable: multiple outputs share heavy transformations, source logic is reused, or branching queries increase maintenance cost
- Mark N/A when: the query layer is small/simple and staging would add more complexity than value
- Guidance: do not fail this item just because staging tables are absent; first decide whether the report needs them
- Quantitative threshold: 2 or more downstream queries reusing the same heavy transformation = staging/reference expected
- Quantitative threshold: 2 or more branches from the same source query = staging/reference should be considered

### Row 6
- Check: Assess whether only required columns and rows are loaded, with row filters and column reduction applied as early as practical.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/import-modeling-data-reduction
- When applicable: the report imports or materializes data into the model
- Guidance: note any intentionally retained helper fields or extra history that is required for the report
- Quantitative threshold: 0 clearly unused loaded columns unless justified
- Quantitative threshold: review when more than 10% of loaded columns are not used in relationships, calculations, or visuals

### Row 7
- Check: Assess whether data typing is controlled at the correct layer.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-query/data-types
- When applicable: the report depends on typed values for sorting, relationships, visuals, or DAX behavior
- Mark N/A when: typing is intentionally governed upstream (for example: source/dataflow) and repeated typing in Power Query is unnecessary
- Guidance: avoid uncontrolled Any/variant behavior and document where type governance actually lives
- Quantitative threshold: 0 model-facing columns with uncontrolled Any/variant behavior unless justified
- Quantitative threshold: 100% of relationship keys, sort-by columns, date columns, and numeric measure-source columns must be explicitly typed somewhere

### Row 8
- Check: Assess whether query, table, column, and measure names follow a consistent naming standard that fits the intended audience.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization
- When applicable: report authors or support staff use the semantic model directly
- Guidance: prefer descriptive business names for author-facing fields and consistent technical naming where appropriate
- Quantitative threshold: 0 duplicate visible field names in the same table
- Quantitative threshold: 0 placeholder names such as Column1, Table, or Query1 in visible author-facing fields

### Row 9
- Check: Assess whether business rules and assumptions are documented at the layer where they are implemented.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview
- When applicable: the report contains non-obvious logic in source shaping, DAX, model design, or report interactions
- Mark N/A when: the report contains little or no transformation/business logic at that layer
- Guidance: document where the logic actually lives instead of forcing comments where no rule exists
- Quantitative threshold: 100% of non-obvious transformations should be documented
- Quantitative threshold: 100% of exception-handling logic should be documented
- Quantitative threshold: 1 or more manual overrides or hard-coded business rules = documentation required

### Row 10
- Check: Assess whether parameterized filters (date ranges, environment selectors, source boundaries) are actually needed.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-dynamic-m-query-parameters
- When applicable: they solve a real deployment, refresh, or maintenance problem
- Mark N/A when: fixed upstream shaping is intentional and parameterization would not improve performance, deployment, or maintainability
- Guidance: do not fail this item only because parameters are absent; decide whether the report needs them first

