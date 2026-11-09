# Report Design and Interactions Checklist

Focused standards for page layout, navigation, chart choice, filters, drill behavior, tooltips, and consistency.

Use each item as **Pass / Needs Work / N/A**.

## Visualizations, UX, and layout

### Row 50
- Check: Assess whether page layout follows a consistent grid, spacing, and alignment standard.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-display-settings
- When applicable: the report has multiple visuals or multiple pages intended for repeated use
- Guidance: review alignment, spacing rhythm, and whether similar visuals are placed consistently across pages
- Quantitative threshold: 0 overlapping visuals
- Quantitative threshold: review when 3 or more visuals are visibly off-grid or inconsistently aligned on the same page

### Row 51
- Check: Assess whether a theme is applied intentionally for colors, fonts, palettes, and formatting consistency.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes
- When applicable: the report is shared, branded, or expected to follow organizational design standards
- Mark N/A when: the report is truly ad hoc and not intended for repeat distribution
- Guidance: prefer one approved or deliberately chosen theme rather than ad hoc formatting on every visual
- Quantitative threshold: 1 approved or intentionally documented theme expected for shared/production reports
- Quantitative threshold: 0 conflicting color systems or font systems across the report unless justified

### Row 52
- Check: Assess whether report navigation is intuitive, discoverable, and accessible.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/button-navigators
- When applicable: the report has multiple pages, sections, states, or bookmarked navigation paths
- Mark N/A when: the report is a single simple page with no navigation need
- Guidance: review whether users can move through the report without guessing or getting stuck
- Quantitative threshold: 2 or more sections/pages with custom navigation = review navigation controls
- Quantitative threshold: 0 dead-end pages or hidden navigation paths without obvious access

### Row 53
- Check: Assess whether canvas size and aspect ratio fit the intended devices and display context.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-display-settings
- When applicable: the report is designed for a known display target such as laptop, widescreen, kiosk, or embedded view
- Guidance: review whether the page design matches the intended consumption device and whether pages stay usable without awkward scrolling or clipping
- Quantitative threshold: 1 primary target aspect ratio should be used consistently unless page purpose differs
- Quantitative threshold: review mixed canvas sizes across pages unless clearly justified

### Row 54
- Check: Assess whether persistent filters and default/reset behavior are designed intentionally.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-settings
- When applicable: the report uses slicers, bookmarks, or shared starting states that affect user experience
- Guidance: review whether the report should preserve user state, reset to authored defaults, or expose both behaviors clearly
- Quantitative threshold: 1 explicit decision should exist for persistent filters on production reports using slicers/bookmarks

### Row 55
- Check: Assess whether each visual type matches the analytical intent of the question it answers.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview
- When applicable: the report contains charts used for comparison, distribution, trend, ranking, or part-to-whole analysis
- Guidance: review whether the chosen chart supports the question clearly and avoids avoidable distortion or clutter
- Quantitative threshold: part-to-whole visuals with more than 5 categories = review chart choice
- Quantitative threshold: trend visuals should use a true ordered time/category axis when showing change over sequence

### Row 56
- Check: Assess whether titles, labels, and legends are concise, descriptive, and not misleading.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-format-visual-titles
- When applicable: the report includes visuals that require interpretation by end users
- Guidance: remove placeholder text and make titles describe what the visual actually shows
- Quantitative threshold: 0 placeholder or ambiguous auto-generated titles on production visuals

### Row 57
- Check: Assess whether units and scales are consistent where users are expected to compare visuals, and whether dual axes are avoided unless truly needed.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualizations-overview
- When applicable: the report shows the same or related metrics across multiple visuals
- Guidance: review scale consistency, display units, and whether any dual-axis design is clearly labeled and justified
- Quantitative threshold: 0 unlabeled dual-axis visuals
- Quantitative threshold: 100% of repeated comparable metrics should use consistent display units unless justified

### Row 58
- Check: Assess whether conditional formatting is used intentionally, consistently, and accessibly.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-conditional-formatting
- When applicable: the report uses color, icons, or state formatting to communicate meaning
- Guidance: review semantic consistency of colors and avoid relying only on color for important meaning
- Quantitative threshold: no more than 2 semantic color systems should be used across one report unless justified
- Quantitative threshold: 0 critical states should be communicated by color alone without label/icon support

### Row 59
- Check: Assess whether KPI thresholds are clear and color semantics are consistent across the report.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-conditional-formatting
- When applicable: the report includes KPI or status visuals
- Mark N/A when: the report does not use KPI-style threshold logic
- Guidance: review whether threshold meaning is documented and whether the same colors always mean the same thing
- Quantitative threshold: 100% of KPI states should map to documented thresholds
- Quantitative threshold: 0 conflicting red/green semantics across KPI visuals unless explicitly explained

### Row 60
- Check: Assess whether drill paths are available where useful and obvious enough for users to discover.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-drillthrough
- When applicable: the report contains natural hierarchies, deeper levels, or drillthrough destinations
- Mark N/A when: the report is intentionally flat and no deeper navigation is needed
- Guidance: review whether drill affordances, labels, or instructions make the deeper path discoverable
- Quantitative threshold: 2 or more natural hierarchy levels or detail destinations = review drill path design

## Interactivity and filters

### Row 61
- Check: Assess whether cross-filtering and cross-highlighting behaviors are intentional and whether unexpected interactions are disabled.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/service-reports-visual-interactions
- When applicable: multiple visuals on a page can interact with one another
- Guidance: review interaction behavior on each major visual and disable interactions that confuse the page story
- Quantitative threshold: 0 unexpected visual interactions on the page

### Row 62
- Check: Assess whether slicers are synced across pages where that improves continuity and whether slicers are organized clearly.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-slicers
- When applicable: the same filter concept appears on 2 or more pages
- Mark N/A when: pages intentionally require different independent filter states
- Guidance: review repeated slicers and whether sync improves rather than harms the page workflow
- Quantitative threshold: the same slicer concept on 2 or more pages = review sync slicers
- Quantitative threshold: 0 duplicated repeated slicers left unsynced without a reason

### Row 63
- Check: Assess whether the report has an intentional default filter state and a clear way to return to it.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-bookmarks
- When applicable: the report uses slicers, complex filter states, or bookmarks that change the page state
- Mark N/A when: the report has no meaningful filter state to reset
- Guidance: review entry-state behavior and whether users can reliably get back to the authored default
- Quantitative threshold: 1 clear reset/default path expected for reports with meaningful user-adjustable filter state

### Row 64
- Check: Assess whether drillthrough pages include clear instructions and back navigation.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/report-drillthrough
- When applicable: the report uses drillthrough pages
- Mark N/A when: the report has no drillthrough pages
- Guidance: review whether users understand how to enter/leave drillthrough and what context the page expects
- Quantitative threshold: 100% of drillthrough pages should include back navigation
- Quantitative threshold: 100% of drillthrough pages should make their expected context obvious

### Row 65
- Check: Assess whether field parameters are used where user-controlled switching would reduce page sprawl or improve flexibility.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-field-parameters
- When applicable: users need to switch among 2 or more alternate metrics or dimensions in the same visual area
- Mark N/A when: the report is clearer with fixed visuals and does not benefit from parameter switching
- Guidance: consider field parameters when they reduce duplicate visuals or duplicate pages without harming clarity
- Quantitative threshold: 2 or more alternate metric/dimension choices competing for the same page space = review field parameters

### Row 66
- Check: Assess whether tooltips provide useful context rather than repeating what is already obvious on the visual.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-tooltips
- When applicable: the report uses standard or report-page tooltips
- Mark N/A when: the report does not use tooltip enhancements
- Guidance: prioritize explanatory context, supporting detail, or related metrics that help the hovered value make sense
- Quantitative threshold: report-page tooltips should usually provide 3 or more context fields/metrics beyond the base hovered value

## Consistency and standards

### Row 71
- Check: Assess whether typography is consistent across titles, subtitles, body text, and footnotes.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/report-themes-create-custom
- When applicable: the report uses multiple text elements across one or more pages
- Guidance: review font families, weight hierarchy, and text-size bands so similar text roles look the same everywhere
- Quantitative threshold: no more than 4 text-style roles should be used unless justified
- Quantitative threshold: 0 conflicting title/body styles for the same semantic role

### Row 72
- Check: Assess whether number formatting is consistent across visuals for repeated or comparable metrics.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/report-themes-create-custom
- When applicable: the report shows the same metrics in multiple places or compares related metrics side by side
- Guidance: review decimal precision, display units, separators, currency symbols, and percentage formatting
- Quantitative threshold: 100% of repeated comparable metrics should display with consistent format unless justified

### Row 73
- Check: Assess whether visible date formats match audience expectations and the organization’s standard.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types
- When applicable: the report displays dates or date-like labels to end users
- Guidance: prefer one audience-appropriate visible date style unless different formats are intentionally required for different use cases
- Quantitative threshold: 100% of visible dates should follow one audience-appropriate standard unless justified

### Row 74
- Check: Assess whether page names are clear, user-friendly, and free of unnecessary jargon.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/button-navigators
- When applicable: the report has multiple pages or a broad end-user audience
- Guidance: use names that describe the page purpose rather than internal project language where possible
- Quantitative threshold: 0 page names should rely only on unexplained internal jargon or cryptic abbreviations for end-user audiences

### Row 75
- Check: Assess whether branding assets follow organizational standards and remain visually clean.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/create-reports/report-themes-create-custom
- When applicable: the report is branded or customer-facing
- Mark N/A when: the report intentionally avoids branding
- Guidance: review logo quality, color compliance, and whether brand elements help rather than distract
- Quantitative threshold: 0 stretched or visibly pixelated logo/image assets
- Quantitative threshold: 100% branded colors should match approved palette where branding is required

