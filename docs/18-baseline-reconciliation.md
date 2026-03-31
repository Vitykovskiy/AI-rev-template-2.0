# Baseline Reconciliation

## Source Check

`TODO` referenced these source-of-truth inputs:

- `docs/13-agent-first-sdd-decisions.md`
- `docs/14-process-design-status.md`
- current `TODO`
- current `AI-rev-template-2.0/docs/*`

Observed state in the provided workspace:

| Source | Reconciliation state | Note |
| --- | --- | --- |
| `docs/13-agent-first-sdd-decisions.md` | `missing` | Referenced by `TODO`, absent in workspace |
| `docs/14-process-design-status.md` | `missing` | Referenced by `TODO`, absent in workspace |
| `TODO` | `integrated` | Used as active implementation contract |
| Existing template docs | `integrated` | Expanded into canonical document set `docs/00-17` |

## Accepted Baseline Decisions Mapped

| Decision | State | Canonical location |
| --- | --- | --- |
| Delivery unit is the central managed unit | `integrated` | `docs/04-artifact-model.md`, `docs/07-delivery-unit-artifact-set.md` |
| Architecture decision necessity must be explicit | `integrated` | `docs/04-artifact-model.md`, `docs/06-readiness-and-statuses.md` |
| Implementation is performed only by execution tasks | `integrated` | `docs/03-role-model.md`, `docs/05-link-model.md` |
| Typed links are the context-reconstruction mechanism | `integrated` | `docs/05-link-model.md` |
| GitHub is an operational projection, not repository canon | `integrated` | `docs/10-github-projection.md` |
| Handoffs and blockers must be explicit | `integrated` | `docs/11-handoff-protocol.md` |
| PR and branch rules are deterministic | `integrated` | `docs/12-pr-policy-and-branch-strategy.md` |
| Validation and anti-drift must be operational | `integrated` | `docs/14-validation-and-anti-drift.md`, `tools/` |

## Remaining Open Questions

| Question | State | Reason |
| --- | --- | --- |
| Exact missing content of upstream `docs/13` and `docs/14` | `open` | Not recoverable from current workspace |
| Provider-specific GitHub project-field automation | `deferred` | Template defines mapping contract, not provisioning |
| Bootstrap scripts for real-project adoption | `deferred` | Template establishes contract and scaffolding only |
