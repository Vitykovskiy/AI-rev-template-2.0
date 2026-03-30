# AI Dev Template

Template repository for AI-assisted delivery that uses a guarded bootstrap stage and then runs execution through GitHub Issues, GitHub Project state, explicit owner contours, and canonical repository docs.

`README.md` is the human entry point. The workflow source of truth is `AGENTS.md` plus the documents in `docs/`.

## What This Template Implements

- A 2-stage operating model tracked in `.ai-dev-template.workflow-state.json`:
  - `setup`
  - `issue_driven`
- A 2-mode session model tracked in the same file:
  - `dialogue`
  - `execution`
- Issue-driven delivery through explicit task metadata, dependencies, owner contours, and GitHub Project status.
- A canonical analysis package under `docs/analysis/` that gates implementation.
- Local execution telemetry written to `.agent-work/telemetry/` with the tracked schema and helpers in `runtime/telemetry/`.
- Repository-side GitHub assets: issue forms, PR template, and validation workflows in `.github/`.

Current template defaults:

- `.ai-dev-template.workflow-state.json` starts in `setup` + `dialogue`
- `.ai-dev-template.config.json` ships with `workflow.execution_mode = "autonomous"`
- PR flow is enabled and requires human review by default

## Operating Model

The repository lifecycle is fixed:

1. `setup`
2. `issue_driven`

During `setup`, the technical agent prepares the repository, aligns workflow assets to `.ai-dev-template.config.json`, validates or creates GitHub-side operating artifacts, and seeds the starting backlog.

After setup, all work is routed through GitHub Issues and GitHub Project. The canonical post-setup task chain is:

1. `business_analysis`
2. `infrastructure`
3. one or more bounded `system_analysis` issues
4. `block_delivery`
5. contour-owned `implementation` issues
6. `deploy` when rollout is required
7. `e2e` when integrated validation is required

Key workflow rules:

- one task has exactly one owner contour;
- implementation starts only from implementation-ready analysis inputs;
- `system_analysis` remains the canonical source of truth for specifications and decomposition;
- `Ready` is the only universal claimable status for new work;
- `In Progress` is the canonical active execution signal;
- setup may complete in local-first degraded mode if GitHub bootstrap is temporarily unavailable, but that deferred reconciliation must be recorded.

## Repository Map

### Core Control Files

- `AGENTS.md` - session router and task-selection guardrail
- `.ai-dev-template.workflow-state.json` - current stage and session mode
- `.ai-dev-template.config.json` - repository-local workflow and delivery policy
- `.env.example` - bootstrap environment variable skeleton

### Canonical Documents

- `docs/00-project-overview.md` - high-signal orientation for a new session
- `docs/01-product-vision.md` to `docs/03-scope-and-boundaries.md` - intake and scope docs
- `docs/04-tech-stack.md` and `docs/05-architecture.md` - technical and structural map
- `docs/06-decision-log.md` - material decisions
- `docs/07-workflow.md` - canonical workflow policy
- `docs/09-integrations.md` - GitHub, environment, and external integration map
- `docs/11-workflow-configuration.md` - fixed vs configurable workflow policy
- `docs/12-observability.md` - telemetry rules
- `docs/analysis/` - implementation-gating analysis package
- `docs/delivery/` - contour handoff and decomposition artifacts
- `docs/runbooks/` - deployment and e2e runbooks
- `docs/internal-libraries.md` and `docs/external-libraries.md` - approved library registry

### Agent Instructions

- `instructions/setup/` - setup router and technical-agent rules
- `instructions/intake/` - business-analysis routing
- `instructions/analysis/` - system-analysis routing
- `instructions/delivery/` - delivery router plus role-specific instructions
- `instructions/deploy/` - deploy flow
- `instructions/e2e-test/` - legacy redirect area retained for compatibility

### GitHub Assets

- `.github/ISSUE_TEMPLATE/` - forms for `initiative`, `business_analysis`, `system_analysis`, `infrastructure`, `block_delivery`, `implementation`, `deploy`, `e2e`, and bug intake
- `.github/PULL_REQUEST_TEMPLATE.md` - PR contract
- `.github/workflows/` - repository checks for PR/body/title and text/UTF-8 conventions

### Runtime And Scratch Areas

- `runtime/telemetry/` - tracked telemetry schema, catalog, session template, and helper script
- `.agent-work/telemetry/` - gitignored runtime traces produced during execution
- `tasks/` - temporary local notes and scratch files only
- `templates/` - reusable markdown templates for docs and workflow artifacts

## How To Start A New Project

1. Create a repository from this template and clone it.
2. Review and adjust `.ai-dev-template.config.json`.
3. Keep `.ai-dev-template.workflow-state.json` in `setup` until bootstrap exit conditions are met.
4. Start every session from `AGENTS.md`.
5. During setup, validate or create the GitHub operating backbone:
   - required labels
   - issue forms
   - repository-linked GitHub Project
   - required project fields and statuses
   - one open `initiative`
   - one open initial `business_analysis` issue in `Ready`
6. Record GitHub access gaps as deferred reconciliation if the environment blocks bootstrap.
7. Switch `current_stage` to `issue_driven` only after the local bootstrap path is complete.

## Task Model

Supported post-setup task types:

- `initiative`
- `business_analysis`
- `infrastructure`
- `system_analysis`
- `block_delivery`
- `implementation`
- `deploy`
- `e2e`

Required project statuses:

- `Inbox`
- `Ready`
- `In Progress`
- `Blocked`
- `Waiting for Testing`
- `Testing`
- `Waiting for Fix`
- `In Review`
- `Done`

Required owner contours:

- `business-analyst`
- `system-analyst`
- `frontend`
- `backend`
- `devops`
- `qa-e2e`

## Telemetry

This template separates tracked telemetry definitions from disposable runtime traces:

- tracked spec and helpers: `runtime/telemetry/`
- actual session logs: `.agent-work/telemetry/`

Telemetry is append-only UTF-8 JSONL and is intended to capture task selection, tool usage, failures, retries, blockers, workarounds, handoffs, and delivery-policy decisions.

## Configuration Notes

The effective policy always comes from the repository-local committed `.ai-dev-template.config.json`.

The template currently exposes configuration for:

- execution pacing (`manual` or `autonomous`)
- documentation and workflow language
- PR and review policy
- GitHub token scope expectations
- frontend architecture policy via `architecture.use_fsd`

Template updates do not retroactively rewrite repositories that were already created from it.

## Where To Read Next

- Need the runtime router: `AGENTS.md`
- Need canonical workflow rules: `docs/07-workflow.md`
- Need to understand configuration: `docs/11-workflow-configuration.md`
- Need the telemetry contract: `docs/12-observability.md`
- Need the session entry map: `docs/00-project-overview.md`
