# Code Style

This file defines the minimum enforceable baseline for any touched code in this repository.

When a language-specific formatter, linter, or repository convention already exists, follow that stricter rule.

## Baseline Rules

- Match the prevailing style of the touched area before introducing a new local convention.
- Keep each file, module, class, component, or function focused on one named responsibility.
- Split code when a unit mixes unrelated concerns, hides side effects, or becomes hard to review as one change.
- Use explicit, domain-meaningful names; avoid abbreviations that are not already standard in the codebase.
- Keep public contracts explicit: inputs, outputs, error paths, and configuration assumptions must be visible in code or adjacent docs.
- Update nearby tests, contracts, or docs in the same task when behavior or interfaces change.

## Forbidden Patterns

- dead code, commented-out code blocks, or placeholder implementations left in production paths;
- silent fallback behavior that hides missing configuration, missing data, or failed operations;
- drive-by refactors unrelated to the task's declared scope;
- mixing formatting-only churn with behavioral changes when they can be separated cleanly.

## Repository-Specific Rules

- If `.ai-dev-template.config.json` sets `architecture.use_fsd = true`, frontend changes must preserve Feature-Sliced Design layer boundaries and import directions.
- If the repository has an automated formatter or linter for the touched area, run it on the affected scope or explicitly record why it was not run.
