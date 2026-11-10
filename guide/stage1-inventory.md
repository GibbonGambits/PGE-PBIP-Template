# Stage 1 inventory table

This is the complete list of every file and folder in the repository, as found in Stage 1 of building this guide. It was the checklist used to make sure the guide covers every item. Appendix A of the guide presents the same items grouped by folder.

- **Safety** is the fill colour from the legend in Start here: Green = safe to edit, Amber = edit with care, Red = do not edit (you may still read or run it).
- **AI file** = Yes means an AI agent (GitHub Copilot or Claude) reads the file as instructions. In diagrams these items have a blue dashed outline.
- Paths are relative to the repository root. Folders end with `/`.

| # | Path | Type | Purpose | Safety | AI file |
|---:|---|---|---|---|---|
| 1 | `.env.example` | Env template | Blank list of database/email secret names | Amber |  |
| 2 | `.github/` | Folder | GitHub + Copilot configuration | Amber | Yes |
| 3 | `.github/agents/` | Folder | Copilot custom agent modes | Amber | Yes |
| 4 | `.github/agents/power-bi-data-modeling-expert.agent.md` | Agent mode | Star-schema modelling expert persona | Amber | Yes |
| 5 | `.github/agents/power-bi-dax-expert.agent.md` | Agent mode | DAX formula expert persona | Amber | Yes |
| 6 | `.github/agents/power-bi-visualization-expert.agent.md` | Agent mode | Report design expert persona | Amber | Yes |
| 7 | `.github/CODEOWNERS` | GitHub config | Who must review which folders | Amber |  |
| 8 | `.github/copilot-instructions.md` | AI steering | Primary Copilot policy, auto-loaded | Amber | Yes |
| 9 | `.github/instructions/` | Folder | Rules that load by file type | Amber | Yes |
| 10 | `.github/instructions/power-bi-custom-visuals-development.instructions.md` | Scoped rules | Custom visual coding (TS/JS/LESS files) | Amber | Yes |
| 11 | `.github/instructions/power-bi-devops-alm-best-practices.instructions.md` | Scoped rules | CI/CD and deployment (YAML/PS1/JSON) | Amber | Yes |
| 12 | `.github/instructions/power-bi-security-rls-best-practices.instructions.md` | Scoped rules | Row-level security patterns | Amber | Yes |
| 13 | `.github/ISSUE_TEMPLATE/` | Folder | Issue forms | Green |  |
| 14 | `.github/ISSUE_TEMPLATE/bug_report.md` | GitHub template | Bug report form | Green |  |
| 15 | `.github/ISSUE_TEMPLATE/feature_request.md` | GitHub template | Feature request form | Green |  |
| 16 | `.github/PULL_REQUEST_TEMPLATE.md` | GitHub template | Pre-filled pull request form | Green |  |
| 17 | `.github/skills/` | Folder | Copilot skills (step-by-step recipes) | Amber | Yes |
| 18 | `.github/skills/power-bi-model-design-review/` | Folder | Skill: model audit | Amber | Yes |
| 19 | `.github/skills/power-bi-model-design-review/SKILL.md` | Skill | Audit a model against checklists | Amber | Yes |
| 20 | `.github/skills/power-bi-performance-troubleshooting/` | Folder | Skill: speed triage | Amber | Yes |
| 21 | `.github/skills/power-bi-performance-troubleshooting/SKILL.md` | Skill | Diagnose slow visuals with thresholds | Amber | Yes |
| 22 | `.github/skills/powerbi-dashboard-header/` | Folder | Skill: page header | Amber | Yes |
| 23 | `.github/skills/powerbi-dashboard-header/SKILL.md` | Skill | Standard header band and page chrome | Amber | Yes |
| 24 | `.github/skills/powerbi-fieldparameter/` | Folder | Skill: field parameters | Amber | Yes |
| 25 | `.github/skills/powerbi-fieldparameter/fieldparam_reportbuilder.md` | Skill boilerplate | Fill-in-the-blanks file templates | Amber | Yes |
| 26 | `.github/skills/powerbi-fieldparameter/SKILL.md` | Skill | Build table/bar toggle page, 11 steps | Amber | Yes |
| 27 | `.github/skills/powerbi-modeling/` | Folder | Skill: modelling | Amber | Yes |
| 28 | `.github/skills/powerbi-modeling/SKILL.md` | Skill | Build/review measures and relationships | Amber | Yes |
| 29 | `.github/skills/powerbi-pbiviz-custom-visuals/` | Folder | Skill: custom visuals kit | Amber | Yes |
| 30 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/` | Folder | Starter-kit code | Amber | Yes |
| 31 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/project/` | Folder | Base project files | Amber | Yes |
| 32 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/project/assets/` | Folder | Icon folder | Amber | Yes |
| 33 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/project/assets/icon.png` | Image | 20x20 visual icon | Green | Yes |
| 34 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/project/eslint.config.mjs` | Lint config | Code-style checker settings | Red | Yes |
| 35 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/project/package.json` | npm manifest | Pinned visual dependencies | Red | Yes |
| 36 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/project/pbiviz.json` | Visual manifest | Name/GUID/author placeholders | Red | Yes |
| 37 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/project/tsconfig.json` | TS config | TypeScript compiler settings | Red | Yes |
| 38 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/` | Folder | Shared visual library | Amber | Yes |
| 39 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/base.less` | Stylesheet | Shared fonts and colours | Red | Yes |
| 40 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/dom.ts` | TypeScript | Safe HTML/SVG element builders | Red | Yes |
| 41 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/format.ts` | TypeScript | Number/percent/month formatting | Red | Yes |
| 42 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/interaction.ts` | TypeScript | Click, tooltip, render events | Red | Yes |
| 43 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/paths.ts` | TypeScript | Bar/donut/pin shape drawing | Red | Yes |
| 44 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/props.ts` | TypeScript | Format-pane settings reader/builder | Red | Yes |
| 45 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/scale.ts` | TypeScript | Value-to-pixel scales, ticks | Red | Yes |
| 46 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/text.ts` | TypeScript | Measure/truncate label text | Red | Yes |
| 47 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/shared/tokens.ts` | TypeScript | Design colour tokens | Red | Yes |
| 48 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/` | Folder | Three starter visuals | Amber | Yes |
| 49 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/blank/` | Folder | Minimal skeleton visual | Amber | Yes |
| 50 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/blank/capabilities.json` | Visual contract | Fields and format options | Red | Yes |
| 51 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/blank/src/` | Folder | Source code | Amber | Yes |
| 52 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/blank/src/visual.ts` | TypeScript | Simple bar visual | Red | Yes |
| 53 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/blank/style/` | Folder | Styles | Amber | Yes |
| 54 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/blank/style/visual.less` | Stylesheet | Imports shared base | Red | Yes |
| 55 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceChart/` | Folder | Period chart visual | Amber | Yes |
| 56 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceChart/capabilities.json` | Visual contract | Fields and format options | Red | Yes |
| 57 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceChart/src/` | Folder | Source code | Amber | Yes |
| 58 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceChart/src/visual.ts` | TypeScript | Columns/line + variance strip | Red | Yes |
| 59 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceChart/style/` | Folder | Styles | Amber | Yes |
| 60 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceChart/style/visual.less` | Stylesheet | Imports shared base | Red | Yes |
| 61 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceTable/` | Folder | Statement table visual | Amber | Yes |
| 62 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceTable/capabilities.json` | Visual contract | Fields and format options | Red | Yes |
| 63 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceTable/src/` | Folder | Source code | Amber | Yes |
| 64 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceTable/src/visual.ts` | TypeScript | P&L-style variance table | Red | Yes |
| 65 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceTable/style/` | Folder | Styles | Amber | Yes |
| 66 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/templates/varianceTable/style/visual.less` | Stylesheet | Table layout styles | Red | Yes |
| 67 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/tools/` | Folder | Kit scripts | Amber | Yes |
| 68 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/tools/new_visual.py` | Python | Scaffold a new visual + GUID | Red | Yes |
| 69 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/tools/pbir_helpers.py` | Python | Write visual.json bindings safely | Red | Yes |
| 70 | `.github/skills/powerbi-pbiviz-custom-visuals/assets/tools/sync-visuals.mjs` | Node script | Build, embed, register visuals | Red | Yes |
| 71 | `.github/skills/powerbi-pbiviz-custom-visuals/references/` | Folder | Deep-dive docs | Amber | Yes |
| 72 | `.github/skills/powerbi-pbiviz-custom-visuals/references/CAPABILITIES-AND-DATAVIEW.md` | Doc | Designing fields and data shape | Amber | Yes |
| 73 | `.github/skills/powerbi-pbiviz-custom-visuals/references/DESIGN-IBCS.md` | Doc | Finance chart design conventions | Amber | Yes |
| 74 | `.github/skills/powerbi-pbiviz-custom-visuals/references/FORMATTING-PANE.md` | Doc | Adding format-pane options | Amber | Yes |
| 75 | `.github/skills/powerbi-pbiviz-custom-visuals/references/INTERACTIVITY.md` | Doc | Selection, tooltips, highlight | Amber | Yes |
| 76 | `.github/skills/powerbi-pbiviz-custom-visuals/references/PBIP-EMBEDDING.md` | Doc | Payload/registration/reference triad | Amber | Yes |
| 77 | `.github/skills/powerbi-pbiviz-custom-visuals/references/REPLACING-LICENSED-VISUALS.md` | Doc | Playbook to replace paid visuals | Amber | Yes |
| 78 | `.github/skills/powerbi-pbiviz-custom-visuals/references/TEMPLATES.md` | Doc | What each starter visual does | Amber | Yes |
| 79 | `.github/skills/powerbi-pbiviz-custom-visuals/references/TROUBLESHOOTING.md` | Doc | Symptom -> cause -> fix tables | Amber | Yes |
| 80 | `.github/skills/powerbi-pbiviz-custom-visuals/SKILL.md` | Skill | Build/embed own custom visuals (9 steps) | Amber | Yes |
| 81 | `.github/skills/powerbi-theme-governance/` | Folder | Skill: themes | Amber | Yes |
| 82 | `.github/skills/powerbi-theme-governance/SKILL.md` | Skill | Turn Theme.json into deployable copy | Amber | Yes |
| 83 | `.github/skills/powerbi-visual-verify/` | Folder | Skill: screenshot review | Amber | Yes |
| 84 | `.github/skills/powerbi-visual-verify/SKILL.md` | Skill | Review rendered screenshots | Amber | Yes |
| 85 | `.github/skills/README.md` | Doc | Index of the 8 skills | Green | Yes |
| 86 | `.github/workflows/` | Folder | GitHub Actions automation | Red |  |
| 87 | `.github/workflows/ai-testing.yml` | CI workflow | AI test on push to test branch | Red |  |
| 88 | `.gitignore` | Git config | Files Git must never track | Amber |  |
| 89 | `AGENTS.md` | AI steering | Short rulebook digest for AI agents | Amber | Yes |
| 90 | `CODE_OF_CONDUCT.md` | Community doc | Behaviour rules for contributors | Green |  |
| 91 | `CONTRIBUTING.md` | Community doc | How to add skills, specs, tests | Green |  |
| 92 | `copilot-instructions.md` | AI reference | Deep PBIP rulebook (727 lines) | Amber | Yes |
| 93 | `docs/` | Folder | Human guides and standards | Green |  |
| 94 | `docs/AI-CONTEXT.md` | Doc | Why steering/specs/hooks are separate | Green |  |
| 95 | `docs/checklists/` | Folder | Six quality checklists | Green |  |
| 96 | `docs/checklists/accessibility-and-performance.md` | Checklist | Rows 21-22, 67-70 | Green |  |
| 97 | `docs/checklists/dax-and-measures.md` | Checklist | Rows 28-39 | Green |  |
| 98 | `docs/checklists/power-query-and-data-sources.md` | Checklist | Rows 2-10 | Green |  |
| 99 | `docs/checklists/README.md` | Doc | Index of checklist rows 2-80 | Green |  |
| 100 | `docs/checklists/report-design-and-interactions.md` | Checklist | Rows 50-66, 71-75 | Green |  |
| 101 | `docs/checklists/security-governance-testing-documentation.md` | Checklist | Rows 40-49, 76-80 | Green |  |
| 102 | `docs/checklists/semantic-model-and-relationships.md` | Checklist | Rows 11-20, 23-27 | Green |  |
| 103 | `docs/CICD-SETUP.md` | Doc | Dev/Test/Prod branch + secrets setup | Green |  |
| 104 | `docs/REPOSITORY-GUIDE.md` | Doc | Repo map, what to edit, upstream sync | Green |  |
| 105 | `docs/STARTER-PACK-CHECKLIST.md` | Doc | Roll-out checklist | Green |  |
| 106 | `docs/theme/` | Folder | Theme source and output | Amber |  |
| 107 | `docs/theme/README.md` | Doc | Theme promotion rules | Green |  |
| 108 | `docs/theme/Theme.deployable.json` | Theme output | Cleaned, schema-safe copy | Amber |  |
| 109 | `docs/theme/Theme.json` | Theme source | Editable PGEColors palette | Amber |  |
| 110 | `LICENSE` | Legal | MIT open-source licence | Red |  |
| 111 | `python/` | Folder | Optional Python how-to guides | Green |  |
| 112 | `python/db_alerts/` | Folder | Alert email guide | Green |  |
| 113 | `python/db_alerts/ALERT_EMAIL_INSTRUCTIONS.md` | Doc | DB-triggered alert email recipe | Green |  |
| 114 | `python/email_reporting/` | Folder | Report email guide | Green |  |
| 115 | `python/email_reporting/emal_style_instructions.md` | Doc | Email report + DAX-to-Python rules | Green |  |
| 116 | `python/README.md` | Doc | Build-your-own value validator | Green |  |
| 117 | `README.md` | Doc | Front page: goals, setup, guardrails | Green |  |
| 118 | `scripts/` | Folder | PowerShell checks and bridge loop | Red |  |
| 119 | `scripts/Get-PbipLoadError.ps1` | PowerShell | Reads Desktop error pop-ups | Red |  |
| 120 | `scripts/hooks/` | Folder | Hook wrapper scripts | Red |  |
| 121 | `scripts/hooks/pbip-session-brief.ps1` | Hook | Prints rules + bridge status | Red |  |
| 122 | `scripts/hooks/pbip-stop-hook.ps1` | Hook | Forces screenshot review | Red |  |
| 123 | `scripts/hooks/pbip-validate-hook.ps1` | Hook | Checks each file as written | Red |  |
| 124 | `scripts/hooks/pbip-write-guard.ps1` | Hook | Blocks writes to protected paths | Red |  |
| 125 | `scripts/Invoke-PbipRefresh.ps1` | PowerShell | Clicks Refresh in Desktop | Red |  |
| 126 | `scripts/Invoke-PbipVerify.ps1` | PowerShell | Validate, reload, screenshot loop | Red |  |
| 127 | `scripts/PbipBridge.Common.ps1` | PowerShell | Shared helper functions | Red |  |
| 128 | `scripts/run-ai-md-test.ps1` | PowerShell | Sends PBIP to AI model for audit | Red |  |
| 129 | `scripts/Test-PbipBridge.ps1` | PowerShell | Preflight: is everything installed? | Red |  |
| 130 | `scripts/Test-PbipSemantics.ps1` | PowerShell | Finds load errors in source | Red |  |
| 131 | `scripts/validate-json.ps1` | PowerShell | Checks every JSON parses | Red |  |
| 132 | `scripts/validate-pbip.ps1` | PowerShell | Checks PBIP folder wiring | Red |  |
| 133 | `specs/` | Folder | One plan per dashboard/page | Green |  |
| 134 | `specs/EXAMPLE-sales-overview.md` | Example | Filled-in sample spec | Green |  |
| 135 | `specs/README.md` | Doc | What a spec is, when needed | Green |  |
| 136 | `specs/TEMPLATE.md` | Template | Blank 8-section spec to copy | Green |  |
| 137 | `Template.pbip` | PBIP entry | Double-click file that opens the project | Red |  |
| 138 | `Template.Report/` | Folder | The report (pages, visuals, themes) | Amber |  |
| 139 | `Template.Report/.platform` | Fabric metadata | Report type, name, ID for Fabric Git | Red |  |
| 140 | `Template.Report/definition/` | Folder | Report definition (PBIR) | Amber |  |
| 141 | `Template.Report/definition.pbir` | Report pointer | Links report to semantic model | Red |  |
| 142 | `Template.Report/definition/pages/` | Folder | One subfolder per page | Amber |  |
| 143 | `Template.Report/definition/pages/6e86f24a804ae4a905eb/` | Folder | The single starter page | Amber |  |
| 144 | `Template.Report/definition/pages/6e86f24a804ae4a905eb/page.json` | Page config | 'Page 1', 1280x720, white | Amber |  |
| 145 | `Template.Report/definition/pages/pages.json` | Report config | Page order and active page | Amber |  |
| 146 | `Template.Report/definition/report.json` | Report config | Themes, resources, report settings | Amber |  |
| 147 | `Template.Report/definition/version.json` | Report config | PBIR format version (exact) | Red |  |
| 148 | `Template.Report/StaticResources/` | Folder | Images and themes | Amber |  |
| 149 | `Template.Report/StaticResources/RegisteredResources/` | Folder | Your themes/SVGs (registered) | Amber |  |
| 150 | `Template.Report/StaticResources/RegisteredResources/Theme.deployable.json` | Theme | Live PGEColors theme copy | Amber |  |
| 151 | `Template.Report/StaticResources/SharedResources/` | Folder | Microsoft-supplied resources | Red |  |
| 152 | `Template.Report/StaticResources/SharedResources/BaseThemes/` | Folder | Base themes | Red |  |
| 153 | `Template.Report/StaticResources/SharedResources/BaseThemes/CY26SU02.json` | Theme | Microsoft default base theme | Red |  |
| 154 | `Template.SemanticModel/` | Folder | The data model (TMDL) | Amber |  |
| 155 | `Template.SemanticModel/.platform` | Fabric metadata | Model type, name, ID for Fabric Git | Red |  |
| 156 | `Template.SemanticModel/definition/` | Folder | TMDL model files | Amber |  |
| 157 | `Template.SemanticModel/definition.pbism` | Model pointer | Semantic model format settings | Red |  |
| 158 | `Template.SemanticModel/definition/cultures/` | Folder | Language settings | Red |  |
| 159 | `Template.SemanticModel/definition/cultures/en-US.tmdl` | TMDL | English (US) culture | Red |  |
| 160 | `Template.SemanticModel/definition/database.tmdl` | TMDL | Compatibility level 1600 | Red |  |
| 161 | `Template.SemanticModel/definition/model.tmdl` | TMDL | Model settings; tables get ref'd here | Amber |  |
| 162 | `Template.SemanticModel/diagramLayout.json` | Layout | Model diagram positions (empty) | Amber |  |
| 163 | `tests/` | Folder | Test prompts and results | Green |  |
| 164 | `tests/prompts/` | Folder | Reusable AI test prompts | Amber | Yes |
| 165 | `tests/prompts/PBIP_Documentation_Page.md` | AI prompt | Generate a Documentation page | Amber | Yes |
| 166 | `tests/prompts/PowerBI_Test.md` | AI prompt | Measure Killer-style + BPA audit | Amber | Yes |
| 167 | `tests/prompts/Python_Data_Value_Test.md` | AI prompt | Plan a SQL value checker | Amber | Yes |
| 168 | `tests/README.md` | Doc | How to run tests | Green |  |
| 169 | `tests/results/` | Folder | Test outputs (generated) | Red |  |
| 170 | `tests/results/history/` | Folder | Timestamped past results | Red |  |
| 171 | `tests/results/history/.gitkeep` | Placeholder | Keeps empty folder in Git | Red |  |
| 172 | `tests/results/history/test_results_20260417_124749.md` | Generated | Run at 12:47:49 UTC (skipped) | Red |  |
| 173 | `tests/results/history/test_results_20260417_124810.md` | Generated | Run at 12:48:10 UTC (skipped) | Red |  |
| 174 | `tests/results/latest_run.json` | Generated | Last run metadata (skipped) | Red |  |
| 175 | `tests/results/README.md` | Doc | Explains result files | Green |  |
| 176 | `tests/results/test_results.md` | Generated | Latest AI test report (skipped) | Red |  |

**Total: 176 items = 122 files + 54 folders.** The hidden `.git/` folder (Git's own database) and the new `guide/` folder are not counted.
