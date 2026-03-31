# Artifact Model

## Entity Types

The template uses six canonical entity types:

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

It is not just a GitHub issue.

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

Business meaning, release context, ownership, and version semantics must live in fields and typed links, not inside the identifier body.

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

## Canonical Artifact Rules

- every artifact must have an owner defined in the ownership map;
- every artifact must have at least one typed upstream link when it is non-root;
- every artifact must be traceable to a delivery-unit boundary or a managed baseline;
- no artifact may be used as both the source of truth and the operational projection of a different artifact family.

## Canonical Storage Map

| Entity | Canonical path | File naming rule |
| --- | --- | --- |
| `requirement` | `requirements/` | `REQ-XXX-<slug>.md` |
| `specification` | `specifications/` | `SPEC-XXX-<slug>.md` |
| `architecture_decision` | `architecture/` | `ADR-XXX-<slug>.md` |
| `delivery_unit` | `delivery-units/` | `DU-XXX-<slug>.md` |
| `contour_task` | `tasks/contour/` | `CT-<CONTOUR>-XXX-<slug>.md` |
| `execution_task` | `tasks/execution/` | `ET-<CONTOUR>-XXX-YY-<slug>.md` |

## Exact Canonical File Shape

Each canonical file must contain:

1. machine-checkable metadata conforming to `schemas/canonical-artifact-model.schema.json`;
2. structured body sections from the corresponding template in `templates/`;
3. explicit typed-link references to upstream and downstream entities;
4. readiness and done criteria when the entity participates in implementation flow.

## Minimal Completeness And Transition Rules

| Entity | Minimal completeness | Ready for next stage when | Done when |
| --- | --- | --- | --- |
| `requirement` | problem, stakeholders, constraints, success criteria explicit | approved baseline exists | merged or superseded |
| `specification` | functional, non-functional, interface, and state rules explicit | linked delivery units can be approved | approved and linked |
| `architecture_decision` | context, decision, alternatives, consequences explicit | linked DUs satisfy architecture gate | approved or superseded |
| `delivery_unit` | control metadata, scope, acceptance type, upstream refs explicit | package approved and decomposition complete | accepted and released when required |
| `contour_task` | one parent DU, one contour, dependencies, readiness explicit | child execution tasks exist or `non_decomposable` is justified | all child work completed |
| `execution_task` | one parent contour task, scope, dependencies, evidence explicit | PR can be opened | PR merged and evidence linked |
