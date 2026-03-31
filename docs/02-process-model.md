# Process Model

## Business Analysis

Business analysis defines the problem space, the user or system need, and the acceptance intent.

Outputs:

- requirements baseline;
- scope boundary;
- affected stakeholder set;
- change classification.

Business analysis does not define implementation tasks.

## System Specification

System specification translates approved requirements into explicit system behavior, constraints, and delivery units.

Outputs:

- specification artifacts;
- delivery-unit candidates;
- dependency graph;
- explicit architecture-decision status per delivery unit.

Specification must not collapse architecture decisions into prose.

## Decomposition

Decomposition splits an approved delivery unit into contour tasks and then execution tasks.

Rules:

- decomposition happens only after the delivery-unit package is approved;
- contour tasks are created per contour, not per person;
- execution tasks are created only when the change can be reviewed and merged atomically;
- safe parallelism is allowed only when there is no hard sequential dependency and no shared mutable boundary;
- if safe parallelism is uncertain, the default is sequential execution;
- a contour task may remain undecomposed only when the exception is explicit and justified.

## Task Model

The task model is a strict hierarchy:

1. `delivery_unit`
2. `contour_task`
3. `execution_task`

Rules:

- a delivery unit owns the delivery boundary;
- a contour task owns one contour within one delivery unit;
- an execution task owns one atomic change set;
- implementation links belong only to execution tasks;
- task identifiers remain stable and are not overloaded with semantics.

## Agent Workflow Design

The canonical agent workflow is:

1. intake and classification
2. requirements or specification analysis
3. architecture review when required
4. delivery-unit approval
5. decomposition
6. execution-task implementation
7. code review
8. integration validation
9. acceptance
10. release control when required

The workflow may branch by contour, but the canonical source of truth remains the same delivery unit.

## Validation Layer

Validation is layered and must not be skipped:

- document validation checks completeness and link closure;
- readiness validation checks state-machine guards;
- execution validation checks the atomic change set;
- integration validation checks the assembled delivery-unit result;
- release validation checks operational completion when release is required.

## Merge Points

There are two mandatory merge points:

1. merge after requirements gathering and approval;
2. merge after agreement on a delivery-unit package consisting of system artifacts plus any required architecture artifacts.

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
