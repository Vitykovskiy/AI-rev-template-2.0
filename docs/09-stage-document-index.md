# Stage Document Index

## Reconciled Open Issue

The upstream repository snapshot did not contain source TODO links to `docs/13` and `docs/14`.

This gap is reconciled here by treating those documents as canonical endpoints for impact assessment and validation/anti-drift instead of omitting them.

## Stage Index

| Stage | Primary documents | Canonical outputs | Exit condition |
| --- | --- | --- | --- |
| Business analysis | `01`, `02`, `04`, `05`, `08`, `09`, `13` | requirements baseline, scope boundary, ownership candidate | requirements are explicit and traceable |
| System specification | `02`, `04`, `05`, `06`, `07`, `08`, `09`, `13` | specification package, delivery-unit candidates, architecture status | delivery-unit package is internally complete |
| Decomposition | `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `11`, `12` | contour tasks, execution tasks, handoff packet | every participating contour is represented |
| Task model | `04`, `05`, `06`, `07`, `10`, `12` | stable task hierarchy and GitHub projection | each atomic execution task is reviewable |
| Agent workflow design | `03`, `09`, `10`, `11`, `12`, `16` | routing rules, handoff protocol, branch policy | every agent knows the next bounded action |
| Validation layer | `06`, `13`, `14`, `15`, `16`, `17` | readiness gate, validation evidence, cleanup criteria | no unresolved contradiction remains |

## Document Index Notes

- `docs/00` is the entry summary, not a control document.
- `docs/01` controls dialogue behavior.
- `docs/02` controls lifecycle and decomposition.
- `docs/03` controls roles and subagent triggers.
- `docs/04` controls artifact taxonomy and metadata.
- `docs/05` controls typed links and traceability.
- `docs/06` controls readiness and state transitions.
- `docs/07` controls the minimum delivery-unit package.
- `docs/08` controls ownership.
- `docs/09` controls stage routing and document discovery.
- `docs/10` controls GitHub projection.
- `docs/11` controls handoff.
- `docs/12` controls branch and PR policy.
- `docs/13` controls impact assessment.
- `docs/14` controls validation and anti-drift.
- `docs/15` controls runbooks.
- `docs/16` controls telemetry.
- `docs/17` controls cleanup and retirement.
