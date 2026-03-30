# Internal Libraries

This file is the registry of approved usage contracts for shared internal modules, packages, SDKs, and reusable abstractions owned by the repository.

Each entry defines the public contract that downstream tasks may consume without reverse-engineering implementation details from source code. Source code and exported types still matter for verification, but they do not authorize using private internals or undocumented patterns.

## Approved Internal Library Usage Contracts

Create or update an entry when a bounded analysis slice or delivery task:

- introduces a new shared module, package, or reusable abstraction;
- changes the public contract of an existing internal library;
- starts consuming an existing internal library from a new contour, layer, or runtime boundary;
- formalizes repository-specific constraints that consumers must follow.

Record each approved contract with at least:

- module or package name and repository location;
- owning contour, team, or maintainer when known;
- approved public exports, types, and configuration surface;
- required initialization, provider, composition, or lifecycle rules;
- approved consumers, layers, or boundary constraints;
- business, data, or runtime invariants consumers must preserve;
- forbidden internals or unsupported usage patterns;
- verification reference: existing repo consumer, test, or explicit "none yet";
- last reviewed by task, issue, or date.

_No approved internal library usage contracts recorded yet. Populate this registry when shared modules are introduced or their public contract changes._

## Rules

- Treat this registry as the canonical approved public contract for internal library consumers.
- Check this file before consuming or changing any shared internal module.
- Then inspect exported types, source code, and working consumers to confirm the contract details.
- Do not assume internal library API from naming alone.
- Do not rely on private internals, incidental exports, or implementation details that are not approved here.
- If the contract is still unclear, mark uncertainty and avoid risky changes.

## Required Verification

Before changing code that depends on a shared internal module, verify:

- approved public exports and types;
- public signatures and config shape;
- required initialization, provider, or lifecycle pattern;
- package or layer boundary constraints;
- supported props, options, or extension points;
- repository-specific restrictions recorded in this registry.

## Source Of Truth

Use all applicable sources in this order:

1. the relevant approved contract entry in this file;
2. the library source code and its exported types;
3. an existing working repository consumer that matches the approved contract.

If these sources disagree, the approved contract in this file wins until analysis updates it.

## Missing Contract Rule

If a task materially depends on an internal library and the approved contract is missing or unclear:

- do not invent API;
- do not use unconfirmed exports or private internals;
- record the missing contract explicitly;
- route the missing contract to `system_analysis` when the allowed usage cannot be confirmed safely;
- otherwise make only the safest minimal change and update this registry before closing the task.

## Maintenance Rule

When a new shared module is created or an existing one changes its public contract, update this registry before closing the task.
