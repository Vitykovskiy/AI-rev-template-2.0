# GitHub Projection

## Principle

GitHub is the operational source of truth for work state.

The repository remains the canonical source of truth for requirements, specifications, architecture, and delivery-unit metadata.

GitHub stores projections of canonical state, not replacements for it.

## Projection Map

| Canonical artifact | GitHub projection | Parent-child model |
| --- | --- | --- |
| `delivery_unit` | issue or project item | parent of contour-task issues |
| `contour_task` | issue or project item | child of one delivery-unit issue |
| `execution_task` | issue + branch + pull request | child of one contour-task issue |
| Fix work after integration testing | issue + PR | child of the same delivery unit as the failed validation target |
| `requirement`, `specification`, `architecture_decision` | reference issue or linked discussion only when operationally useful | never replace repository canon |

## Projection Fields

Every GitHub projection item should include:

- canonical artifact id;
- title;
- current state;
- owner;
- blocker status;
- next action;
- upstream links;
- downstream links;
- validation status when relevant.

## Mapping Contract

| Canonical field | GitHub field |
| --- | --- |
| `id` | issue title prefix or dedicated custom field |
| `status` | project status field or label |
| `owner` | assignee |
| `depends_on` | linked issue dependency |
| `parent_*_ref` | parent issue reference |
| `definition_of_done` evidence | PR body and linked validation comment |
| `architecture_decision_status = deferred` | `Blocked` plus blocker reason field |

## Status Projection Rules

- GitHub labels or project columns are derived from canonical states.
- Canonical state may be more specific than the visible GitHub column.
- A GitHub item may not advance state without the corresponding canonical artifact change.
- If GitHub and the canonical repository disagree, the repository wins and the projection is corrected.

## Operational Rules

- One execution task maps to at most one active pull request.
- Non-code PRs are allowed for requirements baselines and delivery-unit package approval.
- A delivery unit may aggregate many GitHub issues, but those issues remain projections of the canonical structure.
- Comments in GitHub are operational evidence, not a substitute for source-of-truth documentation.
- If a projection item has no canonical id, it is not part of the template workflow.

## Non-Goals

- GitHub is not the canonical storage for architecture decisions.
- GitHub is not the canonical storage for requirements or specifications.
- GitHub labels are not the canonical workflow model.
