# Accessibility and Performance Checklist

Focused standards for performance density, slicer scale, accessibility, and query-reduction behavior.

Use each item as **Pass / Needs Work / N/A**.

## Performance and load

### Row 21
- Check: Assess whether visual density per page is reasonable for the page size, audience, and interaction pattern.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization
- When applicable: the page contains multiple visuals, heavy custom formatting, or many interactions
- Guidance: there is no universal hard limit, but high visual counts increase queueing, rendering, and validation complexity
- Quantitative threshold: <=8 active visuals = low density; 9–12 = normal; 13–16 = review; >16 = high density and justification required
- Quantitative threshold: count each dominant large table/matrix as 2 visuals for review purposes

### Row 22
- Check: Assess whether high-cardinality slicers are necessary.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers
- When applicable: the report uses slicers over large text/ID domains
- Mark N/A when: the report has no such slicers
- Guidance: when they exist, prefer search, hierarchy, relative date, drillthrough, field parameters, or filter-pane patterns where they improve usability/performance
- Quantitative threshold: <=500 distinct slicer values = normal; 501–2,000 = review; 2,001–10,000 = require search/hierarchy/filter-pane/alternate pattern; >10,000 = avoid unless strongly justified

## Accessibility

### Row 67
- Check: Assess whether color contrast and non-color cues meet accessibility expectations.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports
- When applicable: the report uses color to communicate meaning or displays text over colored backgrounds
- Guidance: review contrast, label support, and whether important states are still understandable without color
- Quantitative threshold: text contrast should meet WCAG guidance where practical
- Quantitative threshold: 0 critical states should rely on color alone without icon/label support

### Row 68
- Check: Assess whether text sizes remain readable on common consumption devices such as laptops and projected displays.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports
- When applicable: the report is intended for meetings, presentations, or standard desktop use
- Guidance: review title, body, axis, label, and footnote sizes under realistic viewing conditions
- Quantitative threshold: body text should generally be at least 10 pt
- Quantitative threshold: major titles should generally be at least 12 pt

### Row 69
- Check: Assess report performance with Performance Analyzer and review slow visuals/measures.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/performance-analyzer
- When applicable: the report contains interactive visuals or users have reported slow behavior
- Guidance: also note whether the delay is mainly DAX query, visual display, or Other/queueing
- Quantitative threshold: repeated interactions — <100 ms excellent; 100–1000 ms acceptable; 1000–2000 ms investigate; 2000–3000 ms poor; >3000 ms bad; >10000 ms unacceptable without clear progress feedback
- Quantitative threshold: if DAX query time >1000 ms, treat as a model/DAX review candidate
- Quantitative threshold: if Other/queueing time >500 ms on repeated interaction, review page density/render order

### Row 70
- Check: Assess whether query-reduction features were considered where they would help (for example: Apply buttons on slicers, avoiding unnecessary sync/cross-highlighting, disabling auto page refresh unless needed).
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/buttons-apply-all-clear-all-slicers
- When applicable: the report has interactive controls that can generate unnecessary repeated queries
- Mark N/A when: the report has no interactive controls that would materially benefit
- Guidance: do not fail this item simply because a report has no need for query-reduction features
- Quantitative threshold: review Apply-button/query-reduction patterns when a page has 2 or more slicers commonly changed together
- Quantitative threshold: review when a single slicer change refreshes 5 or more visuals
- Quantitative threshold: auto page refresh intervals under 30 seconds require explicit justification

