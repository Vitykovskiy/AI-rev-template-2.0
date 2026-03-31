# Canonical Ownership Map

## Principle

Canonical ownership is exclusive.

Only the canonical owner may redefine the source-of-truth rule class. Other layers may reference the rule, project it, or validate it, but they may not silently override it.

## Rule-Class Ownership

| Rule class | Canonical location | Projection or reference only |
| --- | --- | --- |
| Communication rules | `docs/01-communication-rules.md` | `AGENTS.md`, templates |
| Process model and merge points | `docs/02-process-model.md` | `README.md`, PR template |
| Role boundaries and subagent triggers | `docs/03-role-model.md` | task templates |
| Artifact shapes and storage rules | `docs/04-artifact-model.md` | `schemas/`, `templates/` |
| Typed links and traceability | `docs/05-link-model.md` | `schemas/`, `examples/`, `tools/` |
| Readiness and statuses | `docs/06-readiness-and-statuses.md` | `.github/`, `tools/` |
| Delivery-unit package | `docs/07-delivery-unit-artifact-set.md` | DU template, validator |
| GitHub projection | `docs/10-github-projection.md` | issue templates, PR template |
| Handoff protocol | `docs/11-handoff-protocol.md` | `templates/handoff.md` |
| PR policy and branch strategy | `docs/12-pr-policy-and-branch-strategy.md` | PR template, workflow |
| Impact assessment | `docs/13-impact-assessment.md` | impact template |
| Validation and anti-drift | `docs/14-validation-and-anti-drift.md` | `tools/` |
| Runbooks | `docs/15-runbooks.md` | operational notes |
| Telemetry | `docs/16-telemetry.md` | runtime logs |
| Cleanup and supersession | `docs/17-lifecycle-cleanup.md` | maintenance scripts |
| Baseline reconciliation | `docs/18-baseline-reconciliation.md` | TODO tracking |

## Artifact Ownership

| Artifact family | Canonical owner | Secondary steward | Approval gate |
| --- | --- | --- | --- |
| `requirement` | Requirements analyst | Delivery-unit owner | Requirements baseline approval |
| `specification` | System analyst | Architect | System-specification approval |
| `architecture_decision` | Architect | System analyst | Architecture approval |
| `delivery_unit` | System analyst or explicit delivery-unit owner | Architect | Delivery-unit package approval |
| `contour_task` | Implementation coordinator | Delivery-unit owner | Decomposition approval |
| `execution_task` | Executor | Reviewer | Merge approval |

## Change Rule

- Ownership may change only through an explicit canonical change.
- GitHub projections are never canonical owners.
- If ownership is disputed, the affected artifact remains blocked until the dispute is resolved.
