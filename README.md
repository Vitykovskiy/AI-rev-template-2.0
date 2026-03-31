# New Template

This directory contains the isolated document package for the agent-first, specification-driven template.

It is a separate product under design. It does not redefine the active workflow of the current repository orchestrator.

## Purpose

The template supports:

- strict specification-driven delivery;
- repository artifacts as the source of truth for requirements, specifications, architecture, and traceability;
- GitHub as the operational source of truth for execution state;
- explicit decomposition from delivery units to contour tasks to execution tasks;
- agent-led execution with human review at pull-request boundaries.

## Priority Layers

- `P0` means the mandatory canonical baseline required for delivery-unit execution.
- `P2` means the governance and operational layer that projects canonical state into GitHub, validation, telemetry, and lifecycle control.

## Directory Layout

- `AGENTS.md` - session rules and routing model for the template
- `docs/00-template-overview.md` - concise orientation for a new session
- `docs/01-communication-rules.md` - user dialogue rules with highest priority
- `docs/02-process-model.md` - canonical process model
- `docs/03-role-model.md` - roles, boundaries, and subagent triggers
- `docs/04-artifact-model.md` - artifact types, identifiers, and control metadata
- `docs/05-link-model.md` - typed links and traceability constraints
- `docs/06-readiness-and-statuses.md` - readiness gates and state machine
- `docs/07-delivery-unit-artifact-set.md` - minimum mandatory artifact set per delivery unit
- `docs/08-canonical-ownership-map.md` - canonical ownership and stewardship map
- `docs/09-stage-document-index.md` - stage-to-document index and reconciliation notes
- `docs/10-github-projection.md` - GitHub operational projection model
- `docs/11-handoff-protocol.md` - explicit handoff protocol
- `docs/12-pr-policy-and-branch-strategy.md` - branch and pull-request policy
- `docs/13-impact-assessment.md` - impact assessment contract
- `docs/14-validation-and-anti-drift.md` - validation layer and anti-drift controls
- `docs/15-runbooks.md` - standard operational runbooks
- `docs/16-telemetry.md` - process telemetry and evidence model
- `docs/17-lifecycle-cleanup.md` - cleanup, archival, and retirement rules
- `docs/18-baseline-reconciliation.md` - baseline reconciliation and unresolved source gaps

## Current State

This package now defines the canonical document shell for the template.

Further expansion should stay within the approved source-of-truth documents and the explicit link model.
