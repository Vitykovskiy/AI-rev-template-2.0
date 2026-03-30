# New Template

This directory contains the isolated document package for the new agent-first specification-driven template.

It is a separate product under design.

It does not redefine the active workflow of the current repository orchestrator.

## Purpose

The template defined here is intended to support:

- strict specification-driven delivery;
- repository artifacts as the source of truth for requirements, specifications, and architecture;
- GitHub as the operational source of truth for execution state;
- explicit decomposition from delivery units to contour tasks to execution tasks;
- agent-led execution with human review at pull request boundaries.

## Directory Layout

- `AGENTS.md` - session rules and routing model for the new template
- `docs/00-template-overview.md` - concise orientation for a new session
- `docs/01-communication-rules.md` - user dialogue rules with highest priority
- `docs/02-process-model.md` - lifecycle and control flow
- `docs/03-role-model.md` - roles and role boundaries
- `docs/04-artifact-model.md` - artifact types and identifiers
- `docs/05-link-model.md` - typed links and validity constraints
- `docs/06-readiness-and-statuses.md` - readiness gates and project statuses
- `docs/07-delivery-unit-artifact-set.md` - minimum mandatory artifact set per delivery unit

## Current State

This package is the first isolated documentation baseline.

It should be expanded into a full standalone template only after the remaining open workflow questions are closed.
