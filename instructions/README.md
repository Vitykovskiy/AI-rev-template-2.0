# Orchestration Instructions

This directory is the navigation layer for the multi-role workflow.

It does not redefine canonical roles, stages, artifact ownership, or approval gates.
It selects the next bounded role and points to the canonical documents that govern that decision.
It also reads the root workflow state contract in `../.ai-rev-template.workflow-state.json` as runtime input for orchestration decisions.

## Reading Order

1. `orchestration-router.md`
2. `../docs/03-role-model.md`
3. `../docs/09-stage-document-index.md`
4. `../docs/02-process-model.md`
5. `../docs/11-handoff-protocol.md`

## Canonical Sources

- `docs/03-role-model.md` defines role boundaries and subagent triggers.
- `docs/08-canonical-ownership-map.md` defines canonical ownership.
- `docs/09-stage-document-index.md` defines stage discovery and document routing.
- `docs/02-process-model.md` defines the workflow and merge points.
- `docs/11-handoff-protocol.md` defines transfer-of-responsibility rules.

## Role Prompt Targets

These files are behavioral projections of the canon, not replacements for it.

- `roles/requirements-analyst.md`
- `roles/system-analyst.md`
- `roles/architect.md`
- `roles/delivery-unit-owner.md`
- `roles/implementation-coordinator.md`
- `roles/executor.md`
- `roles/reviewer.md`
- `roles/validator.md`

## Use

- Start here when the next bounded action is unclear.
- Use the router to choose one primary role.
- Check the workflow-state contract before opening the matching role prompt.
- Open the matching role prompt target after the router resolves the role.
- Use the canonical documents to confirm the next artifact, stage, or handoff.
