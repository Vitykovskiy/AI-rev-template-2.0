# Telemetry

## Principle

Telemetry measures process health and traceability.

It is not a substitute for canonical documents or GitHub projections.

## Telemetry Scope

The template tracks:

- stage transitions;
- approval latency;
- blocker duration;
- review turnaround;
- fix-loop count;
- integration failure count;
- release lead time;
- drift incidents;
- missing-link incidents;
- ownership disputes.

## Event Model

Each telemetry event should capture:

- event type;
- canonical artifact id;
- current state;
- timestamp;
- owning role;
- blocking reason if applicable;
- validation outcome if applicable.

## Required Event Types

- artifact created
- artifact approved
- artifact decomposed
- execution task opened
- execution task merged
- review requested
- review completed
- blocker recorded
- blocker cleared
- validation failed
- validation passed
- release started
- release completed
- cleanup completed

## Operational Rules

- Telemetry may summarize state, but it must not become the source of truth.
- Telemetry gaps are a validation defect.
- Telemetry should support auditability of decisions, not just progress reporting.
