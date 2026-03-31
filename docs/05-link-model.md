# Link Model

## Principle

Links between artifacts and tasks are mandatory typed relations.

Developers must not reconstruct the required context manually from the full document corpus.

The necessity of a separate architecture decision is governed by delivery-unit metadata, not by an inferred absence or presence of typed links alone.

## Typed Link Contract

Each link must declare:

- source artifact id;
- target artifact id;
- relation type;
- rationale when the relation is not obvious from the artifact names alone;
- status, if the relation is provisional.

## Allowed Typed Links

- `requirement -> requirement`: `supersedes`
- `requirement -> specification`: `refines`
- `requirement -> delivery_unit`: `decomposes_into`
- `specification -> specification`: `supersedes`
- `specification -> delivery_unit`: `decomposes_into`
- `architecture_decision -> architecture_decision`: `supersedes`
- `architecture_decision -> specification`: `constrains`
- `delivery_unit -> delivery_unit`: `depends_on`
- `delivery_unit -> contour_task`: `decomposes_into`
- `contour_task -> contour_task`: `depends_on`
- `contour_task -> execution_task`: `decomposes_into`
- `contour_task -> specification`: `depends_on`
- `contour_task -> architecture_decision`: `depends_on`
- `execution_task -> execution_task`: `depends_on`
- `execution_task -> specification`: `implements`
- `execution_task -> architecture_decision`: `implements`

## Forbidden Aggregate Implementation Links

- `contour_task -> specification`: `implements` is forbidden
- `delivery_unit -> specification`: `implements` is forbidden

`implements` belongs only to `execution_task`, because it is the minimal executable unit whose completion can be verified directly.

## Minimum Validity Rules

- `specification` must refine at least one `requirement`
- `delivery_unit` must be created from at least one upstream `requirement` or `specification`
- `contour_task` must have exactly one parent `delivery_unit`
- `contour_task` must depend on at least one `specification` or `architecture_decision`
- `execution_task` must have exactly one parent `contour_task`
- `execution_task` must implement at least one `specification` or `architecture_decision`

## Traceability Rules

- every non-root artifact must be linked to its upstream source of truth;
- every delivery unit must expose downstream decomposition links;
- every execution task must preserve the chain back to the specification or architecture decision it implements;
- every GitHub projection item must reference the canonical artifact ids it represents;
- orphan links are a validation failure, not a warning.

## Context Reconstruction Rule

Task context is reconstructed from typed links and canonical ids, not from ad hoc repository search.

Free-form search is allowed only to locate a known artifact whose canonical id is already known.

Additional delivery-unit validity rules:

- every `delivery_unit` must declare `architecture_decision_status`
- if `architecture_decision_status = required`, the `delivery_unit` must reference at least one `architecture_decision`
- if `architecture_decision_status = not_required`, the `delivery_unit` must contain a rationale for why a separate architecture decision is unnecessary
- if `architecture_decision_status = deferred`, the `delivery_unit` is incomplete and must not enter implementation
