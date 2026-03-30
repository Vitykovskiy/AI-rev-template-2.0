# Integrations

## GitHub Project

- URL: `https://github.com/users/Vitykovskiy/projects/25`
- Board type: `GitHub Project v2`
- Required statuses present: `yes`
- Required fields present: `Status`, `Task Type`, `Owner Contour`, `Priority`
- Project item creation verified: `yes`
- Setup validation status: `Completed`
- Notes: Repository-linked project `AI-rev-template-2.0 delivery` was created during setup and linked to `Vitykovskiy/AI-rev-template-2.0`. Required custom fields were created and the default `Status` field was updated to the workflow status vocabulary.

## GitHub Issues

- Initiative issue creation verified: `yes`
- Initial seeded `business_analysis` issue verified: `yes`
- Operational issue templates verified: `yes`
- Required task metadata captured by forms: `yes`
- Ready -> In Progress claim/start flow verified: `yes`
- Labels prepared for workflow use: `yes`
- Notes: Seeded initiative `#3` is in `In Progress` and seeded `business_analysis` issue `#4` is in `Ready`. Duplicate bootstrap issues `#1` and `#2` were closed to preserve a single canonical starting backlog.

## Effective Workflow Policy

- Effective `.ai-dev-template.config.json` committed and pushed: `yes`
- Notes: Effective setup policy comes from the committed repo-local config: `workflow.execution_mode = autonomous`, `project_tracking = github_project`, and `pull_requests.enabled = true`. Setup ran in normal GitHub-backed mode, not local-first fallback mode.

## Bootstrap Access Variables

These variables describe the raw VPS access that DevOps receives at Stage 0. They are inputs, not published app credentials.

| Variable | Required | Purpose | Stage first needed | Status |
| --- | --- | --- | --- | --- |
| `VPS_HOST` | yes | Raw VPS host or IP for Stage 0 bootstrap | `setup` | Unknown |
| `VPS_USER` | yes | Raw VPS login user for Stage 0 bootstrap | `setup` | Unknown |
| `VPS_PORT` | no | SSH port for Stage 0 bootstrap | `setup` | 22 |
| `VPS_PASSWORD` | one of | Password auth for Stage 0 bootstrap | `setup` | Unknown |
| `VPS_SSH_PRIVATE_KEY_PATH` | one of | Local path to SSH private key for Stage 0 bootstrap | `setup` | Unknown |
| `VPS_SSH_PRIVATE_KEY` | one of | Secret-backed SSH key material for Stage 0 bootstrap | `setup` | Unknown |

## Published Runtime And Validation Contract

These variables are produced or published by DevOps after Stage 0. They are not required for setup.

| Variable | Required | Purpose | Stage first needed | Status |
| --- | --- | --- | --- | --- |
| `TARGET_URL` | no | Published target environment URL | `deploy/e2e` | Unknown |
| `TARGET_LOGIN` | no | Authenticated access for validation or operations | `deploy/e2e` | Unknown |
| `TARGET_PASSWORD` | no | Authenticated access for validation or operations | `deploy/e2e` | Unknown |

## Tokens And Secrets

| Secret | Where It Lives | Purpose | Stage first needed | Status |
| --- | --- | --- | --- | --- |
| `gh` auth token | GitHub CLI auth store | Issues and Project automation | `setup` | Validated |

## GitHub Token Scope Baseline

Required scopes:

- `repo`
- `project`

Recommended scopes:

- `read:org`
- `workflow`

Validation note:

- token scopes are necessary but not sufficient;
- repository membership, project write access, and branch protection rules must still be validated separately;
- record actual validation results in this file during `setup`;
- report setup or later GitHub-side workflow steps complete after the corresponding side effects are verified.

## Runtime And External Integrations

Document every external system that matters to development, deploy, or e2e validation.

| Integration | Purpose | Stage first needed | Status | Notes |
| --- | --- | --- | --- | --- |
| `GitHub Issues` | Canonical task records and dependency chain | `setup` | `Connected` | Seeded issues `#3` and `#4` created successfully. |
| `GitHub Project v2` | Canonical delivery status board | `setup` | `Connected` | Project `25` is linked to the repository and contains the seeded starting backlog. |

## Integration Status

- GitHub repository access: `Validated`
- GitHub Project access: `Validated`
- Deployment environment access: `Unknown`
- E2E environment readiness: `Unknown`

## Runbook References

- Deployment runbook: `docs/runbooks/deployment-runbook.md`
- E2E validation runbook: `docs/runbooks/e2e-validation-runbook.md`

## Setup Notes

- Update this file as integrations are connected or changed.
- During `setup`, validate GitHub Issues access and GitHub Project access, and record the actual result here.
- Record verification evidence for the GitHub operating model prepared in `setup`, including project readiness, issue creation ability, and required labels or project fields.
- Keep the runbook documents in `docs/runbooks/` aligned with the actual deployment and test environments.
- Do not store production secrets in committed files.
- If the project uses a separate secret manager, document the reference location here.
