# Process Model

## Process Shape

The template defines a strict specification-driven process with explicit merge points before implementation.

## Main Stages

1. Requirements gathering
2. System analysis
3. Architecture
4. Implementation
5. Post-implementation validation
6. Release and deployment control when required

## Merge Points

There are two main mandatory merge points:

1. merge after requirements gathering and approval
2. merge after agreement on a delivery unit package consisting of system artifacts plus any required architecture artifacts

## Implementation Entry Rule

Implementation starts only when:

- the delivery unit is approved;
- the specification package for that unit is approved;
- the architecture decision package for that unit is approved when the delivery unit declares it as required;
- participating contours are defined;
- contour tasks exist and are linked to required upstream artifacts;
- contour tasks are decomposed into execution tasks unless explicitly marked as non-decomposable;
- dependencies and readiness criteria are defined;
- no unresolved contradictions remain between requirements, specification, and architecture.

The delivery unit itself must explicitly record whether a separate architecture decision is required, not required, or deferred.

## Contradictions During Implementation

If implementation discovers a contradiction:

- the implementation agent calls system-analysis or architecture support;
- documentation changes are reflected in the relevant pull request;
- local changes do not require a separate impact assessment;
- non-local changes require an impact assessment.

## Blocking Model

- Only affected tasks are blocked.
- Blocking must be explicit.
- A blocked task must record the reason, the blocking change, and the unblock condition.

## Post-Implementation Rule

Implementation does not finish the delivery unit.

A delivery unit remains open until:

- integrated validation is complete;
- required fixes are delivered and retested;
- product acceptance is complete;
- release or deployment is complete when required.
