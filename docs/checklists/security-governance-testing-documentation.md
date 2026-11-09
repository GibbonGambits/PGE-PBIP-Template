# Security, Governance, Testing, and Documentation Checklist

Focused standards for access controls, governance, operational readiness, QA evidence, and user-facing documentation.

Use each item as **Pass / Needs Work / N/A**.

## Security and governance

### Row 40
- Check: Assess whether Row-Level Security roles are defined and tested wherever row filtering is required by audience or policy.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/rls-guidance
- When applicable: different audiences should see different data rows from the same model
- Mark N/A when: the dataset is intentionally open to all intended consumers and row filtering is not required
- Guidance: test roles in both Desktop and Service where deployment behavior matters
- Quantitative threshold: 100% of required RLS roles should be tested
- Quantitative threshold: 1 or more test cases per role should validate expected row access

### Row 41
- Check: Assess whether Object-Level Security is used when columns or tables must be truly hidden for security reasons.
- Microsoft Learn: https://learn.microsoft.com/en-us/fabric/security/service-admin-object-level-security
- When applicable: sensitive columns or tables must be inaccessible to certain audiences
- Mark N/A when: Report-view hiding is sufficient because the need is usability rather than security
- Guidance: do not confuse Report-view hiding with security; use OLS when data must not be accessible at all
- Quantitative threshold: 1 or more sensitive columns/tables requiring true restriction = review OLS

### Row 42
- Check: Assess whether Dynamic RLS is implemented where identity-based row access is needed across multiple users or groups.
- Microsoft Learn: https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security
- When applicable: the same model serves multiple audiences with identity-driven row restrictions
- Mark N/A when: static roles are sufficient or row security is not needed
- Guidance: review identity mapping, group logic, and fallback behavior for unmatched users
- Quantitative threshold: 2 or more audiences sharing one model with identity-based row filtering = review Dynamic RLS
- Quantitative threshold: 100% of dynamic RLS mappings should be tested with representative identities

### Row 43
- Check: Assess whether sensitivity labels and endorsement/certification status are applied according to governance expectations.
- Microsoft Learn: https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-security-apply-data-sensitivity-labels
- When applicable: the report or dataset is shared broadly, governed, or used as a reusable semantic asset
- Mark N/A when: the asset is ad hoc/personal and not subject to governance requirements
- Guidance: use the organization’s governance standard for labeling and endorsement rather than applying labels inconsistently
- Quantitative threshold: 100% of governed production datasets should have intentional endorsement/certification status
- Quantitative threshold: 100% of datasets subject to sensitivity policy should have the required label

### Row 44
- Check: Assess whether dataset permissions follow least-privilege principles and avoid unnecessary Build access.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-permissions
- When applicable: the dataset is shared with report consumers, authors, or downstream self-service users
- Guidance: grant Build only to audiences who truly need semantic-model reuse or new-report authoring
- Quantitative threshold: 0 broad-audience Build grants unless justified
- Quantitative threshold: 100% of Build recipients should have a real authoring or downstream-use need

### Row 45
- Check: Assess whether lineage is accurate and dependencies are documented where lineage view alone is insufficient.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-data-lineage
- When applicable: the asset is part of a governed reporting chain with upstream/downstream dependencies
- Guidance: review whether the published dependency picture matches the real delivery path of the report and semantic model
- Quantitative threshold: 100% of upstream/downstream production dependencies should be visible in lineage or documented elsewhere

### Row 46
- Check: Assess whether refresh cadence, failure alerting, and recovery/runbook guidance are appropriate for the report’s SLA.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh
- When applicable: the dataset is refreshed on a schedule or is operationally important
- Mark N/A when: the dataset is manual/ad hoc and not expected to refresh automatically
- Guidance: review schedule frequency, ownership, alerting, and recovery instructions
- Quantitative threshold: 100% of production scheduled datasets should have an owner and alert path
- Quantitative threshold: 1 or more documented recovery/runbook steps should exist for refresh failure handling

## Quality, testing, and documentation

### Row 47
- Check: Assess whether null handling, outlier handling, and any approved business exceptions are documented.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-query/best-practices
- When applicable: the report logic treats blanks, nulls, exclusions, outliers, overrides, or capped values specially
- Mark N/A when: the report has no material special handling for nulls or outliers
- Guidance: focus on business-critical fields and metrics where special handling changes interpretation
- Quantitative threshold: 100% of critical null/outlier handling rules should be documented
- Quantitative threshold: 1 or more approval references should exist for manual overrides or approved exception rules

### Row 48
- Check: Assess whether a changelog is maintained for production changes to the report or semantic model.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-tmdl-view
- When applicable: the asset is shared, production, or governed
- Mark N/A when: the asset is disposable/ad hoc and not maintained as a production artifact
- Guidance: track what changed, why, who changed it, and who approved it where applicable
- Quantitative threshold: 100% of production releases/changes should have a dated changelog entry with owner/reason
- Quantitative threshold: 1 or more approval references should be captured for governed changes

### Row 49
- Check: Assess whether KPI and dimension definitions are documented in a place users or support staff can find them.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-description
- When applicable: the report exposes business terms, KPIs, or dimensions that are not universally understood
- Mark N/A when: the audience is extremely narrow and the business meaning is genuinely obvious
- Guidance: definitions can live in model descriptions, report help pages, dataset descriptions, or controlled documentation
- Quantitative threshold: 100% of business-critical KPIs should have documented definitions
- Quantitative threshold: 100% of non-obvious business dimensions should have a documented definition path

## Validation and user readiness

### Row 76
- Check: Assess whether known limitations and usage caveats are surfaced on an Info/Help page or equivalent user-facing location.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data
- When applicable: the report has refresh latency, known caveats, exclusions, delayed data, or operational constraints users should understand
- Mark N/A when: the report truly has no meaningful caveats to communicate
- Guidance: include practical limitations such as refresh cadence, data latency, as-of timing, and last refreshed context where useful
- Quantitative threshold: 100% of material user-facing limitations should be documented in a discoverable place

### Row 77
- Check: Assess whether QA was completed with representative target users and whether the feedback loop is documented.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/guidance/power-bi-optimization
- When applicable: the report is intended for production or repeated use by a defined audience
- Mark N/A when: the report is a personal/ad hoc artifact with no shared audience
- Guidance: seek at least one representative tester per major audience where practical
- Quantitative threshold: 1 or more representative testers per major audience should review production reports before release

### Row 78
- Check: Assess whether important export scenarios such as Excel and PDF were tested where those outputs matter.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/collaborate-share/end-user-pdf
- When applicable: users are expected to export, print, or circulate snapshots of report content
- Mark N/A when: the report is not intended to be exported or printed
- Guidance: test the pages and visuals that matter most to downstream consumers
- Quantitative threshold: 100% of critical export/print scenarios should be tested where export is part of the user workflow

### Row 79
- Check: Assess whether audience access was validated across apps, workspaces, and permissions before release.
- Microsoft Learn: https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-permissions
- When applicable: the report is shared or published to any audience beyond the author
- Guidance: verify that the intended users can access the report and that unintended users cannot
- Quantitative threshold: 100% of intended audience groups should be access-tested before release

## Optional add-ons

### Row 80
- Check: Assess whether there is a decommission plan for legacy reports or datasets replaced by this asset.
- Microsoft Learn: https://learn.microsoft.com/en-us/fabric/governance/endorsement-overview
- When applicable: the report or model replaces older production content
- Mark N/A when: the asset is net-new and does not replace anything
- Guidance: identify which assets are being replaced, who owns them, and when they will be retired
- Quantitative threshold: 100% of replaced legacy assets should have an owner and retirement path documented

