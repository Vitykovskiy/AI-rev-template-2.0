# Handoff Protocol

## Principle

Handoff is an explicit transfer of responsibility between roles or agents.

It is not a casual comment, a chat message, or an implicit context swap.

## Handoff Triggers

Handoff is required when:

- a delivery unit changes stage;
- a contour task is transferred to a different coordinator;
- an execution task is transferred to a different executor or reviewer;
- a blocker requires escalation;
- validation fails and fix work is reassigned;
- ownership changes hands.

## Handoff Packet

Every handoff packet must contain:

- canonical artifact ids;
- current state;
- completed work summary;
- remaining work summary;
- blockers and unblock conditions;
- linked validation evidence;
- next owner;
- deadline or next checkpoint when applicable.

## Handoff Rules

- The sender must close the previous context to the smallest safe boundary.
- The receiver must confirm the next action before work continues.
- A handoff is incomplete until the receiver acknowledges the packet.
- If scope changed during the handoff, the change must be reflected in the canonical documents or the handoff is invalid.

## Reversal Rule

- If the receiver detects missing context, the task returns to the sender or to the canonical owner.
- The receiver must not guess the missing scope.
- If a handoff is repeatedly incomplete, the delivery unit is blocked until the source gap is fixed.
