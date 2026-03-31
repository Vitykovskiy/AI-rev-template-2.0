# Delivery Unit Artifact Set

## Purpose

This document defines the minimum mandatory artifact set for one delivery unit.

Its purpose is to keep the process strict without forcing empty artifacts that exist only for form.

## Principle

Each delivery unit must have a complete and explicit artifact package before implementation starts.

The package must distinguish:

- mandatory artifacts
- conditionally mandatory artifacts
- control metadata that determines package completeness

## Minimum Mandatory Artifact Set

Every delivery unit must have:

1. one `delivery_unit`
2. at least one `specification`
3. at least one `contour_task` for each participating contour
4. at least one `execution_task` for each contour that is allowed to start work

Every delivery unit must also declare:

- `delivery_unit_type = user_facing` or `delivery_unit_type = internal_enabler`

## Conditionally Mandatory Artifact Set

`architecture_decision` is conditionally mandatory.

It is required when the delivery unit:

- introduces a new architectural constraint
- changes an existing architectural decision
- creates a cross-contour consequence
- changes a significant non-functional property
- introduces a failure or recovery strategy that cannot be treated as a local implementation detail

## Delivery Unit Control Metadata

The delivery unit must explicitly record the architectural completeness decision through these fields:

- `architecture_decision_status`
- `architecture_decision_refs`
- `architecture_decision_rationale`

Allowed values for `architecture_decision_status`:

- `required`
- `not_required`
- `deferred`

## Interpretation Rules

- `required` means implementation readiness is blocked until the referenced architecture decision package is approved.
- `not_required` means a separate architecture decision is intentionally unnecessary for this delivery unit and the rationale must explain why.
- `deferred` means an architectural question has been recognized but not resolved, so the delivery unit is not implementation-ready.

## Anti-Patterns

The template must reject these behaviors:

- creating empty architecture decisions only to satisfy process formality
- hiding architectural changes inside `specification` prose without an explicit architecture-decision decision
- allowing agents to infer architectural necessity implicitly from missing links or missing documents
- declaring an internal-only delivery unit without independently verifiable system-level or operational acceptance criteria

## Consequence For Ready State

A delivery unit cannot be considered ready unless its minimum artifact set is complete and its architectural status is explicitly resolved.

`internal_enabler` delivery units are allowed only as explicit exceptions and must define system-level acceptance criteria instead of user-facing acceptance criteria.
