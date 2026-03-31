# AGENTS.md

Read this file first at the start of every new session inside the new template.

## User Dialogue Rules

These dialogue rules have the highest priority for user-facing dialogue.

- Use sequential dialogue: address one substantive question or decision at a time.
- Use correct professional terminology.
- When a term may be ambiguous, clarify it briefly on first use in the current context.
- Minimize unnecessary anglicisms. Prefer precise Russian professional language and use English terms only when they are standard and materially clearer.
- Treat improvement of the user's understanding as part of the task.
- Be critical instead of agreeable by default. If a proposal has a weak point, terminology error, architecture risk, or methodological flaw, state it directly and explain why.
- Keep the tone respectful but not servile.
- Prefer strong engineering practice over habit.

## Process Position

This template is a strict agent-first, specification-driven workflow template.

Repository documents are the source of truth for requirements, specifications, architecture, artifact ownership, and traceability.

GitHub is the operational source of truth for work state only.

Implementation must follow approved artifacts and explicit typed links between them.

## Navigation Layer

The orchestration router is the first navigation decision for multi-role work.

Read `instructions/README.md` and `instructions/orchestration-router.md` before the canonical document order below.
The router consumes `./.ai-rev-template.workflow-state.json` as runtime input alongside the canonical documents.

## Main Stages

The template separates work into these canonical stages:

1. Business analysis
2. System specification
3. Decomposition
4. Task model
5. Agent workflow design
6. Validation layer

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
- Ownership, stage, validation, and reconciliation rules are defined in `docs/08-18`.

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
9. `docs/08-canonical-ownership-map.md`
10. `docs/09-stage-document-index.md`
11. `docs/10-github-projection.md`
12. `docs/11-handoff-protocol.md`
13. `docs/12-pr-policy-and-branch-strategy.md`
14. `docs/13-impact-assessment.md`
15. `docs/14-validation-and-anti-drift.md`
16. `docs/15-runbooks.md`
17. `docs/16-telemetry.md`
18. `docs/17-lifecycle-cleanup.md`
19. `docs/18-baseline-reconciliation.md`

## Interpretation Rule

Do not collapse specification artifacts and execution entities into a single task model.

Do not treat contour tasks as directly implementing specifications.

Do not start implementation until the required delivery-unit package is approved and linked correctly.

Do not start implementation until the delivery unit has an explicit architecture-decision status and the minimum artifact set is complete.

If an upstream TODO or link references `docs/13` or `docs/14` and the source reference is absent, record the mismatch as a reconciled open issue in the new documents rather than silently dropping it.
