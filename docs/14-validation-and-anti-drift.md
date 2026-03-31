# Validation And Anti-Drift

## Reconciled Open Issue

The upstream snapshot did not contain a source TODO link for this document.

This document therefore defines the missing validation and anti-drift contract directly and treats the gap as reconciled.

## Validation Layers

Validation is layered and cumulative:

1. document validation
2. link validation
3. readiness validation
4. execution validation
5. integration validation
6. release validation when required

## Document Validation

Document validation checks:

- required documents exist;
- document indices are consistent;
- ownership is explicit;
- typed links are present where required;
- no contradictory statements remain unresolved.

## Link Validation

Link validation checks:

- every non-root artifact has upstream traceability;
- every delivery unit has downstream decomposition links;
- no forbidden `implements` link exists outside execution tasks;
- architecture-decision status and links are aligned.

## Readiness Validation

Readiness validation checks:

- the state machine is satisfied;
- the minimum artifact set is complete;
- the delivery unit is not deferred;
- blockers are explicitly resolved or recorded.

## Execution Validation

Execution validation checks:

- the execution task matches its canonical ids;
- the branch and PR are aligned;
- the change set is atomic;
- the PR includes validation evidence.

## Anti-Drift Rules

- No shadow requirements may be introduced in GitHub comments or PR discussion.
- No architectural change may be hidden inside specification prose.
- No ownership may be changed implicitly.
- No status may advance without the corresponding canonical update.
- No validation evidence may be accepted if it does not point back to canonical ids.
- No new document may be created outside the index without updating the stage document index.

## Drift Response

- If drift is detected, freeze the affected item.
- Reconcile the canonical source of truth first.
- Then update the GitHub projection and resume work.
