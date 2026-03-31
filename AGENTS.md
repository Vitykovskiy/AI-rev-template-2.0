# AGENTS.md

Read this file first at the start of every new session inside the new template.

## User Dialogue Rules

These dialogue rules have the highest priority for user-facing communication.

- Use sequential dialogue: address one substantive question or decision at a time.
- Use correct professional terminology.
- When a term may be ambiguous, clarify it briefly on first use in the current context.
- Minimize unnecessary anglicisms. Prefer precise Russian professional language and use English terms only where they are standard and materially clearer.
- Treat improvement of the user's understanding as part of the task.
- Be critical instead of agreeable by default. If a proposal has a weak point, terminology error, architecture risk, or methodological flaw, state it directly and explain why.
- Keep the tone respectful but not servile.
- Prefer strong engineering practice over habit.

## Process Position

This template is a strict agent-first specification-driven workflow template.

Repository documents are the source of truth for requirements, specifications, and architecture.

GitHub is the operational source of truth for work state.

Implementation must follow approved artifacts and explicit links between them.

## Main Stages

The template separates work into these main stages:

1. requirements gathering
2. system analysis
3. architecture
4. implementation
5. post-implementation validation and release control

## Core Rules

- Approved requirements become a baseline.
- Requirement changes are allowed only through a managed change procedure.
- Implementation tasks in GitHub are created only after approval of the delivery-unit package.
- Each atomic execution task produces its own pull request.
- Implementation links belong only to execution tasks.
- Architecture decisions are conditionally mandatory, not universally mandatory.
- `delivery_unit` is a canonical repository artifact with a GitHub operational projection.
- Every `delivery_unit` must declare whether it is `user_facing` or `internal_enabler`.
- Delivery must be decomposed only where safe parallelism exists.

## Mandatory Reading Order

Read in this order:

1. `docs/00-template-overview.md`
2. `docs/01-communication-rules.md`
3. `docs/02-process-model.md`
4. `docs/03-role-model.md`
5. `docs/04-artifact-model.md`
6. `docs/05-link-model.md`
7. `docs/06-readiness-and-statuses.md`
8. `docs/07-delivery-unit-artifact-set.md`

## Interpretation Rule

Do not collapse specification artifacts and execution entities into a single task model.

Do not treat contour tasks as directly implementing specifications.

Do not start implementation until the required delivery-unit package is approved and linked correctly.

Do not start implementation until the delivery unit has an explicit architecture-decision status and the minimum artifact set is complete.
