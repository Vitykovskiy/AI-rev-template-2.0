# Impact Assessment

## Reconciled Open Issue

The upstream snapshot did not contain a source TODO link for this document.

This document therefore defines the missing impact-assessment contract directly and treats the gap as reconciled.

## Principle

Impact assessment decides whether a change remains local or expands beyond the original execution task boundary.

## When Required

Impact assessment is required when a change:

- crosses contour boundaries;
- changes requirements, specification, or architecture;
- changes the delivery-unit metadata;
- changes the GitHub projection model;
- changes runtime behavior, non-functional behavior, or release behavior;
- changes telemetry, validation, runbooks, or cleanup policy;
- affects more than one execution task.

## Local Versus Non-Local

- Local change: stays within one execution task and does not alter canonical boundaries or projection rules.
- Non-local change: affects another artifact family, another contour, or the delivery-unit contract.

If the classification is uncertain, the change is treated as non-local.

## Assessment Output

Every impact assessment must record:

- change summary;
- affected artifact ids;
- affected stage;
- affected contours;
- risk level;
- rollback or fallback path;
- additional approvals required;
- documentation updates required;
- validation updates required.

## Decision Rule

- If the impact is local, the execution task may proceed with the change and the PR must note the scope.
- If the impact is non-local, the relevant canonical documents must be updated and approved before implementation continues.
- If the impact is unresolved, the item is blocked.
