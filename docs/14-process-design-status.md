# Process Design Status

## Purpose

This file tells a new agent where the repository design work currently stands.

Read this file before continuing any design discussion about the future agent-first specification-driven workflow.

This file describes the design state of a separate new template. It does not redefine the active workflow of the current repository orchestrator.

## Current Design Goal

Design a new strict agent-first specification-driven development workflow where:

- agents perform the main delivery work;
- a human reviews and approves pull requests;
- requirements, specifications, and architecture are merged as repository artifacts before implementation;
- operational work state is tracked in GitHub;
- implementation follows approved artifacts and explicit links between them.

The current repository is using its existing template workflow to orchestrate that design work.

## Current Step

The current design step is:

- translate the accepted baseline into canonical standalone template documents and artifact shapes.

The artifact-link model, identifier scheme, minimum link validity rules, minimum artifact set per delivery unit, delivery-unit status model, and post-implementation workflow shape have already been discussed and recorded in `docs/13-agent-first-sdd-decisions.md`.

## Accepted Decisions

Accepted decisions are recorded in:

- `docs/13-agent-first-sdd-decisions.md`

That file is the current baseline and must be treated as the repository memory of the design discussion.

## Open Questions

Open questions are currently recorded in:

- `docs/13-agent-first-sdd-decisions.md` under `Open Questions`

The most important currently open questions are:

- the exact canonical file shape for repository artifacts such as `delivery_unit`;
- the exact branch strategy for delivery-unit assembly before integration testing.

## Practical Rule For New Sessions

If a new session starts and the user asks to continue the design work, the agent should:

1. read `AGENTS.md`;
2. read `.ai-dev-template.workflow-state.json`;
3. read `docs/14-process-design-status.md`;
4. read `docs/13-agent-first-sdd-decisions.md`;
5. treat the accepted content of `docs/13-agent-first-sdd-decisions.md` as requirements and accepted decisions for the future template;
6. keep the current orchestrator and the separate new template conceptually separate;
7. continue from the remaining open questions instead of restarting the design from scratch.
