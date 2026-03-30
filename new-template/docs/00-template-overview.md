# Template Overview

## Purpose

This document is the high-signal entry point for a new session in the new template.

## Product Definition

The template is designed for agent-first specification-driven development.

Its purpose is to keep knowledge artifacts and execution entities distinct while preserving strict operational routing through GitHub.

## Core Principles

- requirements, specifications, and architecture are repository artifacts;
- GitHub tracks operational work state;
- delivery units sit above task level;
- contour tasks belong to exactly one contour;
- execution tasks are the minimal executable and reviewable units;
- typed links replace free-form context reconstruction.

## Canonical Documents

- `AGENTS.md`
- `docs/01-communication-rules.md`
- `docs/02-process-model.md`
- `docs/03-role-model.md`
- `docs/04-artifact-model.md`
- `docs/05-link-model.md`
- `docs/06-readiness-and-statuses.md`
- `docs/07-delivery-unit-artifact-set.md`

## Delivery Unit Rule

Each delivery unit must define its minimum artifact package explicitly.

Architecture decisions are conditionally mandatory and their necessity must be recorded in the delivery-unit metadata instead of being inferred from prose.

## Current Boundary

This package defines documents and rules only.

It does not yet define bootstrap scripts, automation, repository scaffolding, or GitHub provisioning code.
