# Artifact Model

## Entity Types

The template uses six entity types:

- `requirement`
- `specification`
- `architecture_decision`
- `delivery_unit`
- `contour_task`
- `execution_task`

## Separation Rule

The model separates:

- knowledge artifacts: `requirement`, `specification`, `architecture_decision`
- execution entities: `delivery_unit`, `contour_task`, `execution_task`

`architecture_decision` is a separate entity type and must not be collapsed into `specification`.

## Delivery Unit Rule

`delivery_unit` is a separate canonical artifact.

It is not just a GitHub Issue.

The canonical source of truth for `delivery_unit` lives in the repository.

GitHub stores only the operational projection of the same entity for status tracking, assignment, comments, handoff, and pull-request linkage.

Every `delivery_unit` must declare its type:

- `user_facing`
- `internal_enabler`

`user_facing` is the default.

`internal_enabler` is allowed only when the unit has independently verifiable system-level or operational value, or when it is a mandatory enabling change for later user-facing delivery units.

## Identifier Scheme

The template uses stable identifiers with type prefixes and type-local sequential numbering:

- `REQ-001`
- `SPEC-001`
- `ADR-001`
- `DU-001`
- `CT-FE-001`
- `ET-FE-001-01`

## Contour Codes

- `BA` = business analysis
- `SA` = system analysis
- `AR` = architecture
- `FE` = frontend
- `BE` = backend
- `DO` = devops
- `QA` = qa-e2e

## Identifier Rule

Identifiers are stable keys only.

Business meaning, release context, and version semantics must live in fields and typed links, not inside the identifier body.

## Delivery Unit Control Metadata

Each `delivery_unit` must carry explicit control metadata for package completeness.

Minimum required fields:

- `delivery_unit_id`
- `title`
- `purpose`
- `scope`
- `delivery_unit_type`
- `parent_requirement_refs`
- `specification_refs`
- `participating_contours`
- `architecture_decision_status`
- `architecture_decision_refs`
- `architecture_decision_rationale`
- `dependencies`
- `definition_of_ready`
- `definition_of_done`

`architecture_decision_status` is a mandatory field with these allowed values:

- `required`
- `not_required`
- `deferred`

The field exists to prevent agents from inferring architectural necessity from prose.
