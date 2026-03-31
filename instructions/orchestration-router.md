# Orchestration Router

## Purpose

This document is the explicit routing contract for the multi-role agent workflow.

It maps a request to one primary role, the relevant canonical stage, and the next bounded action.
It does not change role ownership or stage canon.

The router also consumes the runtime state contract in `../.ai-rev-template.workflow-state.json` as operational input before applying canonical routing rules.

## Inputs

The router considers, in order:

1. the runtime state contract in `../.ai-rev-template.workflow-state.json`;
2. the affected canonical artifact, if one already exists;
3. the explicit stage named by the request;
4. the request intent;
5. blocker, handoff, or validation context;
6. whether the change is local or non-local.

## Routing Precedence

1. If a canonical artifact exists, route by artifact ownership from `docs/08-canonical-ownership-map.md`.
2. If the request targets an explicit stage, route by the stage-to-role mapping below.
3. If the request is still ambiguous, route by request intent.
4. If the request touches a blocker, handoff, or validation failure, route to the current owning role and do not reclassify scope until the blocker is resolved.
5. If the change is non-local or architecture-sensitive, route to `Architect` regardless of the earlier match.

## Artifact Routing

| Artifact kind | Primary role | Typical bounded action |
| --- | --- | --- |
| `requirement` | Requirements analyst | baseline capture, scope clarification, acceptance intent |
| `specification` | System analyst | behavior definition, dependency tracing, delivery-unit shaping |
| `architecture_decision` | Architect | constraint definition, non-local impact evaluation |
| `delivery_unit` | Delivery-unit owner | package completeness, readiness, stage transition |
| `contour_task` | Implementation coordinator | contour split, dependency ordering, handoff packet |
| `execution_task` | Executor | atomic implementation, local fix, merge-ready change |

## Stage Routing

| Stage | Primary role | Reason |
| --- | --- | --- |
| Business analysis | Requirements analyst | problem definition, stakeholder intent, acceptance framing |
| System specification | System analyst | system behavior, scope closure, package shaping |
| Decomposition | Implementation coordinator | contour and execution slicing |
| Task model | Delivery-unit owner | stable task hierarchy and GitHub projection |
| Agent workflow design | System analyst | routing rules, handoff protocol, branch policy |
| Validation layer | Validator | readiness gates and assembled-unit checks |

## Intent Routing

If no artifact or stage is explicit, route by request intent:

- requirements discovery or problem framing -> Requirements analyst;
- system behavior, boundary, or traceability -> System analyst;
- architecture decision or non-local consequence -> Architect;
- delivery boundary, package approval, or readiness gate -> Delivery-unit owner;
- decomposition or handoff packaging -> Implementation coordinator;
- implementation or local fix -> Executor;
- review before merge -> Reviewer;
- integrated validation or acceptance evidence -> Validator.

## Fallback Rules

- If the request is ambiguous between requirements and specification, prefer `Requirements analyst` when the problem is still being framed and `System analyst` when the system behavior is already constrained.
- If the request is ambiguous between implementation and review, prefer `Executor` for change production and `Reviewer` for correctness assessment.
- If the request has no reliable signal, route to `System analyst` for clarification unless the issue is explicitly pre-specification, in which case route to `Requirements analyst`.

## Guardrails

- The router must not invent new roles.
- The router must not bypass canonical ownership.
- The router must not collapse stage routing into person-specific assignment.
- The router must not send work directly to execution if the delivery-unit package is not ready.
- The router must treat the workflow-state file as runtime input, not as a replacement for canonical repository documents.
