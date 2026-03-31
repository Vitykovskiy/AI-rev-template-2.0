# Readiness And Statuses

## Delivery Unit Readiness

A delivery unit is ready for implementation only when all of the following are true:

- the delivery unit itself is approved;
- the delivery-unit package is approved;
- the system specification for that delivery unit is approved;
- the architecture decision package for that delivery unit is approved when `architecture_decision_status = required`;
- the participating contours are defined;
- a contour task exists for each participating contour;
- each contour task is linked to the required specifications and architecture decisions;
- each contour task is decomposed into atomic execution tasks, unless explicitly marked as non-decomposable;
- dependencies are defined for each execution task;
- readiness criteria are defined for each execution task;
- there are no open contradictions between requirements, specification, and architecture;
- there are no open blockers that prevent implementation from starting.

A delivery unit is not ready for implementation when:

- `architecture_decision_status = deferred`
- `architecture_decision_status = required` and no linked architecture decision is approved

## Task Readiness Assumptions

- a `delivery_unit` is not ready for execution until at least one `contour_task` exists
- a `contour_task` is not ready for execution until at least one `execution_task` exists, unless an explicit undecomposed exception is allowed

## Project Statuses

The template uses this closed project-status model:

- `Draft`
- `Ready for Approval`
- `Approved`
- `Ready for Decomposition`
- `Decomposed`
- `Ready for Implementation`
- `In Implementation`
- `In Review`
- `Ready for Integration Testing`
- `In Integration Testing`
- `Waiting for Fix`
- `Ready for Acceptance`
- `Accepted`
- `Ready for Release`
- `Released`
- `Done`
- `Blocked`
- `Cancelled`

## State Machine

The canonical state machine is:

1. `Draft`
2. `Ready for Approval`
3. `Approved`
4. `Ready for Decomposition`
5. `Decomposed`
6. `Ready for Implementation`
7. `In Implementation`
8. `In Review`
9. `Ready for Integration Testing`
10. `In Integration Testing`
11. `Waiting for Fix` if validation fails
12. back to `Ready for Implementation` after fixes are linked
13. `Ready for Acceptance`
14. `Accepted`
15. `Ready for Release` when release is required
16. `Released`
17. `Done`

Non-terminal overlay states:

- `Blocked` may be applied from any non-terminal state when an explicit blocker prevents progress;
- `Cancelled` is terminal and removes the item from the active workflow.

## Status Meanings

- `Draft` means the artifact or delivery unit exists but is still being prepared.
- `Ready for Approval` means it is ready for formal review at the current stage.
- `Approved` means the current-stage approval is complete.
- `Ready for Decomposition` means the approved delivery-unit package may be decomposed into contour tasks.
- `Decomposed` means contour tasks and execution tasks exist.
- `Ready for Implementation` means all readiness conditions are satisfied.
- `In Implementation` means implementation work is active.
- `In Review` means review activity still blocks forward movement.
- `Ready for Integration Testing` means all required execution-task changes are merged and the delivery unit is assembled.
- `In Integration Testing` means the full delivery unit is under integrated QA validation.
- `Waiting for Fix` means integration testing found defects or contradictions that require follow-up implementation work.
- `Ready for Acceptance` means integration testing passed and the unit is awaiting final product acceptance.
- `Accepted` means the delivery unit is accepted from a product perspective.
- `Ready for Release` means accepted and waiting for release or deployment.
- `Released` means the required release or deployment action is complete.
- `Done` means the delivery unit is fully complete.
- `Blocked` means progress is impossible because of an explicit blocker.
- `Cancelled` means the unit is intentionally terminated.

## Transition Guards

- a state transition must not skip required approvals;
- a blocked item may only move when the blocker is explicitly cleared;
- `Waiting for Fix` requires a linked fix artifact for the same delivery unit;
- `Ready for Release` is only valid when release or deployment is required by the delivery unit;
- `Done` is only valid when all required acceptance, release, and cleanup criteria are satisfied.

## Post-Implementation Flow

The closed post-implementation flow is:

1. `Ready for Implementation`
2. `In Implementation`
3. `In Review`
4. `Ready for Integration Testing`
5. `In Integration Testing`
6. if defects exist -> `Waiting for Fix` -> back to `Ready for Implementation`
7. if testing passes -> `Ready for Acceptance`
8. `Accepted`
9. if release is required -> `Ready for Release` -> `Released` -> `Done`
10. if release is not required -> `Accepted` -> `Done`

## Testing Rule

Integration testing is performed at delivery-unit level, not at isolated execution-task level.

The testing target is the assembled delivery-unit result after all required execution-task changes are merged.

Defects found in integration testing create linked fix work for the same delivery unit.
