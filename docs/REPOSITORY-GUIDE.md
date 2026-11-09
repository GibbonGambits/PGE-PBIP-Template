# Repository Guide (GitHub Copilot)

This repository is a Power BI PBIP starter designed for **GitHub Copilot-first** workflows.

## What Copilot reads automatically

- **Auto-loaded policy:** [`.github/copilot-instructions.md`](../.github/copilot-instructions.md)
- **Conditionally loaded rules (by file type):** [`.github/instructions/`](../.github/instructions/)
- **On-demand procedures (skill routing):** [`.github/skills/`](../.github/skills/)

Reference material (not the primary auto-loaded policy):
- [`copilot-instructions.md`](../copilot-instructions.md)
- [`AGENTS.md`](../AGENTS.md)
- [`docs/`](./)

## Repository map: what to reuse vs customize

| Path | Purpose | Reusable across reports | Customize per report |
|---|---|---|---|
| [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) | Primary Copilot policy | Yes | Rarely |
| [`.github/instructions/`](../.github/instructions/) | Scoped rules by `applyTo` | Yes | Rarely |
| [`.github/skills/`](../.github/skills/) | Reusable procedures/checklists | Yes | Add/extend only if needed |
| [`copilot-instructions.md`](../copilot-instructions.md) | Deep PBIP reference | Yes | Rarely |
| [`AGENTS.md`](../AGENTS.md) | Compact repository digest | Yes | Occasionally |
| [`specs/`](../specs/) | One spec per dashboard/page | Template only | **Yes** |
| [`docs/checklists/`](./checklists/) | Focused quality standards | Yes | Usually no |
| [`docs/theme/Theme.json`](./theme/Theme.json) | Theme source input | Yes | Often |
| [`docs/theme/Theme.deployable.json`](./theme/Theme.deployable.json) | Deployable theme output | Yes | Generated/updated |
| [`Template.pbip`](../Template.pbip) | PBIP entry point | No | **Yes** (project-specific) |
| [`Template.Report/`](../Template.Report/) | Report PBIR/pages/visuals/resources | No | **Yes** |
| [`Template.SemanticModel/`](../Template.SemanticModel/) | TMDL model/tables/measures | No | **Yes** |
| [`scripts/`](../scripts/) | Validation + verification automation | Yes | Usually no |
| [`tests/`](../tests/) | Prompt/testing conventions and outputs | Yes | Per run/results |
| [`python/`](../python/) | Optional Python utilities | Often | If used |

## Files users should not edit directly

- [`tests/screenshots/`](../tests/screenshots/) (generated verification output)
- `**/.pbi/` cache files (Desktop local cache/settings)
- [`.github/.pbip-state/`](../.github/.pbip-state/) (verification bookkeeping)
- [`Proposals/`](../Proposals/) (non-deliverable client material)

Prefer editing **source PBIP/TMDL/build scripts**, not generated outputs.

## Normal workflow: add an existing PBIP report

1. In Power BI Desktop, save/export the report as PBIP.
2. Add the PBIP project at repo root (`<Project>.pbip`, `<Project>.Report/`, `<Project>.SemanticModel/`).
3. Ensure only one active root PBIP project is targeted by validation scripts at a time.
4. Create a spec from [`specs/TEMPLATE.md`](../specs/TEMPLATE.md).
5. Align report/model rules to [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) and checklist standards in [`docs/checklists/`](./checklists/).
6. Run validation and render verification (below).
7. Fix source files, then re-run until clean.

## How to run validation

```powershell
powershell -NoProfile -File scripts\validate-json.ps1
powershell -NoProfile -File scripts\validate-pbip.ps1
powershell -NoProfile -File scripts\Test-PbipSemantics.ps1
powershell -NoProfile -File scripts\Test-PbipBridge.ps1
powershell -NoProfile -File scripts\Invoke-PbipVerify.ps1 -Mode Review
```

## How to update from upstream

```powershell
git remote add upstream https://github.com/<upstream-owner>/<upstream-repo>.git   # once
git fetch upstream
git checkout main
git merge upstream/main    # or: git rebase upstream/main
```

Then re-run validation commands and resolve conflicts in:
- [`.github/copilot-instructions.md`](../.github/copilot-instructions.md)
- [`.github/skills/`](../.github/skills/)
- [`scripts/`](../scripts/)
- PBIP project files.
