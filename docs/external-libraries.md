# External Libraries

This file is the registry of approved dependency usage contracts for third-party libraries.

Each entry defines the project-approved subset of a dependency: the APIs, patterns, and constraints that delivery tasks may rely on without reopening analysis. Official documentation remains required for verification, but it does not override stricter project-specific limits recorded here.

## Approved External Dependency Usage Contracts

Create or update an entry when a bounded analysis slice or delivery task:

- introduces a new third-party dependency;
- upgrades a dependency version or changes the allowed version range;
- starts relying on a library capability that was not previously approved in this repository;
- tightens repository conventions beyond the library defaults.

Record each approved contract with at least:

- package name and approved version or version range;
- official documentation URL and version-specific reference when applicable;
- approved use cases in this repository;
- approved entrypoints, APIs, hooks, CLI commands, or configuration surface;
- required initialization, lifecycle, runtime, or environment constraints;
- repository-specific conventions that narrow or override the default docs;
- forbidden or restricted patterns;
- verification reference: existing repo example, test, or explicit "none yet";
- last reviewed by task, issue, or date.

_No approved external dependency usage contracts recorded yet. Populate this registry during system analysis or dependency-changing delivery work._

## Rules

- Treat this registry as the canonical project-approved contract for third-party dependency usage.
- Check this file before using or changing any external library.
- Verify the intended usage against official documentation and existing repository examples after checking this file.
- Do not assume that broadly documented library features are approved for this repository unless this registry or an approved follow-up explicitly allows them.
- Do not rely on memory, guesses, or "typical API".
- Do not use unconfirmed methods, parameters, lifecycle assumptions, or version-sensitive patterns.

## Required Verification

Before changing code that depends on an external library, verify:

- package version or supported version range;
- signatures and exported types;
- supported options and configuration keys;
- initialization or lifecycle rules;
- environment and runtime limitations;
- repository-specific restrictions recorded in this registry.

## Source Of Truth

Use all applicable sources in this order:

1. the relevant approved contract entry in this file;
2. official documentation for the approved library version;
3. an existing working repository example that matches the approved contract.

If these sources disagree, the repository-specific contract in this file wins until analysis updates it.

## Missing Contract Rule

If a task materially depends on an external library and no approved contract exists:

- do not make risky blind changes;
- do not broaden dependency usage based only on guesswork or generic docs;
- record the gap explicitly;
- route the missing contract to `system_analysis` when the allowed usage cannot be confirmed safely;
- otherwise make only the safest minimal change and update this registry before closing the task.

## Maintenance Rule

When a new external dependency is added, an existing one is upgraded, or the approved usage surface changes, update this registry before closing the task.
