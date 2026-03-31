# Runbooks

## Purpose

This document defines the standard operational runbooks for the template.

## Runbook: Create Delivery Unit

Trigger: a requirements baseline is approved and a system-level change boundary is needed.

Steps:

1. create or update the `delivery_unit`;
2. assign canonical ownership;
3. record `delivery_unit_type`;
4. record `architecture_decision_status`;
5. link upstream requirements and specifications;
6. mark readiness and done criteria.

## Runbook: Decompose Delivery Unit

Trigger: the delivery-unit package is approved.

Steps:

1. define participating contours;
2. create contour tasks;
3. link contour tasks to specifications and architecture decisions;
4. split each contour task into execution tasks when safe parallelism exists;
5. record dependencies and readiness criteria.

## Runbook: Resolve Contradiction

Trigger: an implementation or validation step finds a contradiction.

Steps:

1. classify the contradiction as local or non-local;
2. if non-local, run impact assessment;
3. update the canonical document set;
4. update the affected GitHub projection;
5. unblock only the affected tasks.

## Runbook: Handle Blocker

Trigger: a task cannot progress.

Steps:

1. record the blocker explicitly;
2. define the unblock condition;
3. identify the owning role;
4. decide whether escalation is required;
5. move the item only after the blocker is resolved.

## Runbook: Integration Validation

Trigger: all required execution-task changes are merged.

Steps:

1. assemble the delivery-unit result;
2. validate the integrated behavior;
3. record defects or contradictions if found;
4. create linked fix work when needed;
5. advance to acceptance only when validation passes.

## Runbook: Release And Cleanup

Trigger: the delivery unit is accepted and release or deployment is required.

Steps:

1. verify release readiness;
2. execute release or deployment;
3. confirm post-release status;
4. archive obsolete operational projections;
5. close the delivery unit only after cleanup criteria are met.
