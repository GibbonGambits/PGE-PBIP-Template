# DAX and Measures Checklist

Focused standards for explicit measures, DAX quality, time intelligence, formatting, and metric documentation.

Use each item as **Pass / Needs Work / N/A**.

### Row 28
- Check: Assess whether measures are used instead of calculated columns where the logic is aggregation-oriented or presentation-oriented.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures
- When applicable: the report needs reusable business calculations, KPI logic, percentages, or aggregations across filter context
- Mark N/A when: the logic is truly row-level and belongs in a calculated column or upstream data shaping
- Guidance: favor measures for aggregated business logic and reserve calculated columns for row-by-row derivation that cannot be handled upstream
- Quantitative threshold: 100% of aggregation-oriented business calculations should be exposed as measures
- Quantitative threshold: 0 visuals should rely on calculated columns for logic that should behave dynamically by filter context

### Row 29
- Check: Assess whether measure naming and prefixes/suffixes follow a consistent standard that helps authors understand measure type and usage.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization
- When applicable: the model exposes reusable measures to report authors
- Mark N/A when: the team intentionally uses a no-prefix standard and that standard is applied consistently
- Guidance: keep naming readable and consistent; do not introduce prefix noise unless it truly helps authors
- Quantitative threshold: 0 visible measures should violate the chosen naming standard without justification
- Quantitative threshold: 0 duplicate visible measure names

### Row 30
- Check: Assess whether explicit measures are used for report metrics instead of relying on implicit aggregations of raw columns.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/model-explorer
- When applicable: the report exposes business metrics, KPIs, or reusable calculations
- Mark N/A when: a raw column is used only for simple ad hoc exploration and not as a governed published metric
- Guidance: prefer explicit measures for governed metrics so behavior, naming, formatting, and logic stay consistent
- Quantitative threshold: 100% of published business metrics should use explicit measures
- Quantitative threshold: 0 KPI or business-critical visuals should rely on implicit aggregation of raw columns

### Row 31
- Check: Assess whether calculation groups, if used, are documented, tested, and safe for author consumption.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/model-explorer
- When applicable: the model uses calculation groups for time intelligence, formatting, or reusable calculation logic
- Mark N/A when: the model does not use calculation groups
- Guidance: if used, review format string behavior, precedence, test coverage, and author guidance
- Quantitative threshold: 100% of calculation groups should have documented purpose
- Quantitative threshold: 100% of calculation items should have test coverage for format string and intended behavior

### Row 32
- Check: Assess whether time intelligence uses a robust Date table with unique continuous dates and the correct date-table setup.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/model-date-tables
- When applicable: the report uses dates for filtering, grouping, or time-based calculations
- Mark N/A when: the report does not perform time-based analysis
- Guidance: review date continuity, uniqueness, blanks, full-year coverage, and whether the intended date table strategy is correctly implemented
- Quantitative threshold: 1 dedicated date table expected for standard time intelligence
- Quantitative threshold: 0 blanks and 0 duplicate values in the date column
- Quantitative threshold: 0 missing dates in the covered range

### Row 33
- Check: Assess whether DAX context-modifying functions such as FILTER, ALL, and ALLEXCEPT are used intentionally and do not accidentally remove needed filter context.
- Microsoft Learn: https://learn.microsoft.com/en-us/dax/best-practices/dax-avoid-avoid-filter-as-filter-argument
- When applicable: the model contains measures using context-modifying functions
- Mark N/A when: the model does not use these patterns
- Guidance: review each usage for whether the removed or preserved context matches the business intent
- Quantitative threshold: 100% of measures using ALL or ALLEXCEPT should have clear business intent
- Quantitative threshold: 0 avoidable FILTER-as-filter-argument patterns for simple predicates

### Row 34
- Check: Assess whether DAX divisions use DIVIDE where appropriate instead of the / operator.
- Microsoft Learn: https://learn.microsoft.com/en-us/dax/divide-function-dax
- When applicable: the model contains division logic in measures or calculation items
- Mark N/A when: the denominator is guaranteed non-zero and the design intentionally does not need DIVIDE behavior
- Guidance: prefer DIVIDE for safer handling of zero or blank denominators
- Quantitative threshold: 100% of non-trivial DAX divisions should use DIVIDE unless explicitly justified otherwise

### Row 35
- Check: Assess whether repeated DAX expressions are cached with VAR where it improves readability or performance.
- Microsoft Learn: https://learn.microsoft.com/en-us/dax/best-practices/dax-variables
- When applicable: the same subexpression is used more than once in a measure or calculation item
- Mark N/A when: the expression is simple enough that VAR adds no meaningful value
- Guidance: use VAR when it reduces repeated evaluation or makes complex DAX easier to understand and maintain
- Quantitative threshold: 2 or more repeated subexpressions inside the same measure = review VAR usage

### Row 36
- Check: Assess whether reusable base measures are separated from presentation measures such as KPI wrappers, percentages, and time variants.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization
- When applicable: the model exposes multiple related presentations of the same business metric
- Mark N/A when: the model is too small/simple for a layered measure pattern to add value
- Guidance: base measures should hold core logic, while presentation measures build on them for readability and reuse
- Quantitative threshold: 2 or more presentation variants of the same metric = review for base-measure pattern

### Row 37
- Check: Assess whether visible measures have correct explicit formatting such as decimals, thousand separators, percentages, and currency.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-measures
- When applicable: the report exposes reusable measures to authors or end users
- Guidance: review format strings on visible measures and keep semantically identical metrics formatted consistently
- Quantitative threshold: 100% of visible measures should have intentional formatting
- Quantitative threshold: 0 repeated business metrics should display with inconsistent units or decimal precision unless justified

### Row 38
- Check: Assess whether metric definitions, exclusions, and caveats are surfaced through descriptions, tooltips, or other author/user-facing documentation.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/report-page-tooltips
- When applicable: the report contains business-critical KPIs, exception-heavy measures, or metrics that can be misunderstood without context
- Mark N/A when: the metric is fully self-explanatory and has no material exclusions or caveats
- Guidance: prioritize definitions for KPIs, percentages, exception-based metrics, and regulated numbers
- Quantitative threshold: 100% of business-critical KPIs should have a visible definition path (tooltip, description, or help text)

### Row 39
- Check: Assess whether calculated tables are avoided for ETL-style shaping that should happen upstream.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-query/dataflows/best-practices-for-dimensional-model-using-dataflows
- When applicable: the model contains calculated tables or table-building logic beyond small helper scenarios
- Mark N/A when: a calculated table is intentionally used for semantic-only purposes such as disconnected parameters, small helper tables, or controlled calculation patterns
- Guidance: use upstream dataflows/source shaping for ETL tasks and reserve calculated tables for semantic-model needs
- Quantitative threshold: 0 calculated tables should be used solely for ETL-style source reshaping

