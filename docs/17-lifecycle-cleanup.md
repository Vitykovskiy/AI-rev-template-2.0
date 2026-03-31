# Lifecycle Cleanup

## Principle

Cleanup removes stale operational residue without destroying canonical traceability.

It is a controlled lifecycle step, not an ad hoc housekeeping task.

## Cleanup Targets

- merged execution branches;
- closed or superseded GitHub projection items;
- obsolete handoff packets;
- stale blocker records;
- superseded runbook entries;
- retired validation evidence;
- obsolete delivery-unit projections after closure.

## Cleanup Rules

- Canonical documents are never deleted without a supersession record.
- Deletion is allowed only for disposable operational artifacts.
- Cleanup must preserve the ids and the lineage of retired work.
- Cleanup must not erase audit history required to explain the delivery path.

## Retirement Conditions

A delivery unit may be retired from active tracking only when:

- it is `Done` or intentionally `Cancelled`;
- all required validation evidence is recorded;
- all required release actions are complete;
- the GitHub projection is consistent with the canonical repository;
- no unresolved drift remains.

## Archival Rules

- Archive completed handoff packets.
- Archive obsolete projection items after closure.
- Retain canonical ids in archival records.
- If cleanup changes traceability, the change itself must be recorded as a canonical update.
