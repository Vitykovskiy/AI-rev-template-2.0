# Agent-First SDD Decisions

This document captures accepted requirements and design decisions for the future template being designed in this repository.

It does not change the operating rules of the current template. The current template remains governed by `AGENTS.md` and the existing canonical workflow documents.

The purpose of this document is to preserve the outcome of design discussions with the customer as input requirements and accepted process constraints for the new template.

The repository is therefore operating in two layers:

- the current template is the active orchestration mechanism for this repository;
- the new template is the separate product being specified.

Do not collapse these layers when interpreting user requests or repository changes.

## Communication Rules

- These communication rules have the highest priority for user-facing dialogue in the future template.
- Use sequential dialogue: ask or address one substantive question or decision at a time instead of unloading a long questionnaire.
- Use precise professional terminology.
- When a term may be ambiguous, give a brief clarification the first time you use it in the current context.
- Avoid unnecessary anglicisms in user-facing dialogue. Prefer precise Russian professional language and use English terms only when they are standard and materially clearer.
- Treat improvement of the user's understanding as part of the task. Do not merely mirror the user's wording if it weakens precision.
- Be critical instead of agreeable by default. If the user's proposal has a weak point, terminology error, architecture risk, or methodological flaw, state it directly and explain why.
- Keep the tone respectful but not servile. Do not soften away important criticism just to preserve comfort.
- Prefer strong engineering practice over habit. If the user's habit conflicts with a stronger practice, say so and propose the better alternative.
- Avoid filler, rhetorical framing, and empty recap sections.
- On narrow questions, answer directly first and add only minimal justification.

These rules belong to the future template's intended product behavior, not to the active rules of this repository unless they are later adopted into the canonical workflow.

## Core Process

- The process is strict.
- Development is specification-driven.
- The human does not manually route every step and instead reviews and approves pull requests.
- GitHub is the operational source of truth for work state.
- Repository documents are the source of truth for requirements, specifications, and architecture.
- Approved requirements become a baseline.
- Requirement changes are allowed only through a managed change procedure.

These statements are product requirements for the new template, not commentary about the current repository only.

## Main Stages

- Requirements gathering
- System analysis
- Architecture
- Implementation

## Roles

- Requirements analyst
- System analyst
- Architect
- Implementation coordinator
- Implementation executors by contour

The explicit separation of these roles is an accepted requirement for the new template.

## Role Responsibilities

- Requirements analyst: produces the requirements baseline.
- System analyst: produces the system specification and defines delivery units.
- Architect: produces architecture decisions and constraints.
- Implementation coordinator: decomposes a contour task into parallelizable execution tasks.
- Executors: implement execution tasks.

## Implementation Coordinator

- The role is explicit and separate.
- It is not a generic team lead role.
- Each contour has its own implementation coordinator.
- The coordinator works only within that contour.
- The coordinator cannot change delivery-unit boundaries, contracts, or architecture constraints.
- If safe parallel decomposition is impossible, the contour task may be executed sequentially.
- Returning the task upward is not a normal mechanism of this role.

## Delivery Units And Tasks

- A delivery unit is not the same thing as a task.
- A delivery unit is above task level.
- A delivery unit is the smallest independently implementable and independently acceptable change package.
- One delivery unit may require multiple contour tasks.
- A contour task may be further decomposed inside the contour.
- Internal contour decomposition is used to improve reviewability, verification, and execution clarity.
- By default, a delivery unit is centered on a user-visible effect or user-scenario outcome.
- A non-user-facing delivery unit is allowed only as an explicit exception when it has independently verifiable system-level or operational value, or when it is a mandatory enabling change for later user-facing delivery units.
- A delivery unit is a canonical repository artifact, not just a GitHub Issue.
- GitHub stores the operational projection of the delivery unit, not the canonical definition.

## Parallelism

- Decomposed tasks should run in parallel where this is safe.
- Parallelism must not be artificial.
- Parallel decomposition requires independent change areas and no hard sequential dependency.

## Subagent Use

Subagents are used only in these cases:

- system analyst <-> architect interaction;
- internal code review before a code pull request;
- parallel execution of independent tasks.

## Architecture Subagent

- It is required during preparation of a delivery unit.
- It may also be called during implementation when an architecture problem or contradiction is discovered.

## Review Subagent

- It is required only before code pull requests.
- It is not required for pull requests that contain requirements, specifications, or architecture decisions only.

## Pull Requests

- There must be pull requests for requirements.
- There must be pull requests for the agreed delivery-unit package after system-analysis and architecture work.
- The first pull request may be non-code.
- No extra human admission gate is required before implementation when the package is already approved.

This merge and approval behavior is an accepted requirement for the new template.

## Two Main Merge Points

- Merge after requirements gathering and approval.
- Merge after agreement on a delivery unit: system part plus architecture part.

## Contradictions Found During Implementation

- The implementation agent calls a system-analysis or architecture subagent.
- Documentation changes are reflected in the relevant pull request.
- Local changes do not require a separate impact-assessment document.
- Non-local changes require an impact-assessment document.

## Impact Assessment

An impact assessment is required only when a change:

- affects other tasks;
- affects the delivery-unit package;
- makes the current decomposition invalid.

Its purpose is to:

- list affected tasks;
- decide which tasks continue;
- decide which tasks are blocked;
- decide which tasks must be redefined.

## Blocking Tasks

- Only affected tasks are blocked.
- Blocking means an explicit `Blocked` state.
- The task must record the reason for blocking.
- The task must link to the blocking change.
- The task must record the unblock condition.

## Links Between Artifacts

- Links between artifacts and tasks are a core part of the process.
- The system contains specifications, tasks, and typed links between them.
- Developers must not reconstruct context manually from the full document corpus.
- A task must contain links to the artifacts required for that task.
- The whole document corpus exists for the system, but each task should expose only the relevant linked subgraph.

## GitHub Task Creation

- Implementation tasks in GitHub are created only after approval of the delivery-unit package.
- Draft implementation tasks must not be created before the delivery-unit package is approved.

## Pull Request Granularity

- Each atomic execution task produces its own pull request.
- A contour task must not be delivered through a single shared pull request when it has already been decomposed into multiple atomic execution tasks.
- Pull request granularity is aligned to reviewability, not to the broader contour-task boundary.

## Delivery Unit Readiness For Implementation

A delivery unit is ready for implementation only when all of the following are true:

- the delivery unit itself is approved;
- the delivery-unit package is approved;
- the system specification for that delivery unit is approved;
- the architecture decision package for that delivery unit is approved when the delivery unit declares it as required;
- the participating contours are defined;
- a contour task exists for each participating contour;
- each contour task is linked to the required specifications and architecture decisions;
- each contour task is decomposed into atomic execution tasks, unless it is explicitly marked as non-decomposable;
- dependencies are defined for each execution task;
- readiness criteria are defined for each execution task;
- there are no open contradictions between requirements, specification, and architecture;
- there are no open blockers that prevent implementation from starting.

A delivery unit is not ready for implementation when:

- its architecture-decision status is `deferred`
- its architecture-decision status is `required` and the required architecture decision package is not approved

## Minimum Artifact Set Per Delivery Unit

The future template uses this minimum mandatory artifact set per delivery unit:

1. one `delivery_unit`
2. at least one `specification`
3. at least one `contour_task` for each participating contour
4. at least one `execution_task` for each contour that is allowed to start work

`architecture_decision` is conditionally mandatory, not universally mandatory.

It is required when the delivery unit:

- introduces a new architectural constraint
- changes an existing architectural decision
- creates a cross-contour consequence
- changes a significant non-functional property
- introduces a failure or recovery strategy that cannot be treated as a local implementation detail

Each `delivery_unit` must explicitly record:

- `architecture_decision_status`
- `architecture_decision_refs`
- `architecture_decision_rationale`

Allowed values for `architecture_decision_status`:

- `required`
- `not_required`
- `deferred`

Each `delivery_unit` must also declare its delivery-unit type:

- `user_facing`
- `internal_enabler`

`user_facing` is the default.

## Artifact Model

The future template uses six entity types:

- `requirement`
- `specification`
- `architecture_decision`
- `delivery_unit`
- `contour_task`
- `execution_task`

The intended terminology in Russian is:

- `delivery_unit` -> `единица поставки`
- `contour_task` -> `задача контура`
- `execution_task` -> `исполнительская задача`
- `typed links` -> `типизированные связи`

`architecture_decision` is a separate entity type and must not be collapsed into `specification`.

The model separates:

- knowledge artifacts: `requirement`, `specification`, `architecture_decision`
- execution entities: `delivery_unit`, `contour_task`, `execution_task`

## Allowed Typed Links

Allowed links in the future template are:

- `requirement -> requirement`: `supersedes`
- `requirement -> specification`: `refines`
- `requirement -> delivery_unit`: `decomposes_into`
- `specification -> specification`: `supersedes`
- `specification -> delivery_unit`: `decomposes_into`
- `architecture_decision -> architecture_decision`: `supersedes`
- `architecture_decision -> specification`: `constrains`
- `delivery_unit -> delivery_unit`: `depends_on`
- `delivery_unit -> contour_task`: `decomposes_into`
- `contour_task -> contour_task`: `depends_on`
- `contour_task -> execution_task`: `decomposes_into`
- `contour_task -> specification`: `depends_on`
- `contour_task -> architecture_decision`: `depends_on`
- `execution_task -> execution_task`: `depends_on`
- `execution_task -> specification`: `implements`
- `execution_task -> architecture_decision`: `implements`

The future template explicitly forbids implementation links at aggregate levels:

- `contour_task -> specification`: `implements` is forbidden
- `delivery_unit -> specification`: `implements` is forbidden

`implements` belongs only to `execution_task`, because it is the minimal executable unit whose completion can be verified directly.

## Identifier Scheme

The future template uses stable identifiers with type prefixes and type-local sequential numbering:

- `REQ-001`
- `SPEC-001`
- `ADR-001`
- `DU-001`
- `CT-FE-001`
- `ET-FE-001-01`

Contour codes currently assumed in the design are:

- `BA` = business analysis
- `SA` = system analysis
- `AR` = architecture
- `FE` = frontend
- `BE` = backend
- `DO` = devops
- `QA` = qa-e2e

Identifiers are stable keys only. Business meaning, release context, and version semantics must live in fields and typed links, not inside the identifier body.

When a GitHub Issue or Project item represents one of these entities operationally, the canonical identifier must be carried explicitly in the title or body rather than replaced by the GitHub numeric issue id.

## GitHub Project Status Model

The future template uses this closed GitHub Project status model:

- `Draft`
- `Ready for Approval`
- `Approved`
- `Ready for Decomposition`
- `Decomposed`
- `Ready for Implementation`
- `In Implementation`
- `In Review`
- `Ready for Integration Testing`
- `In Integration Testing`
- `Waiting for Fix`
- `Ready for Acceptance`
- `Accepted`
- `Ready for Release`
- `Released`
- `Done`
- `Blocked`
- `Cancelled`

These statuses are part of the accepted baseline for the future template.

## Post-Implementation Workflow

The future template uses this closed delivery-unit flow after implementation begins:

1. `Ready for Implementation`
2. `In Implementation`
3. `In Review`
4. `Ready for Integration Testing`
5. `In Integration Testing`
6. if testing finds defects or contradictions -> `Waiting for Fix` -> back to `Ready for Implementation`
7. if testing passes -> `Ready for Acceptance`
8. `Accepted`
9. if release is required -> `Ready for Release` -> `Released` -> `Done`
10. if release is not required -> `Accepted` -> `Done`

Integration testing is performed at delivery-unit level against the assembled delivery-unit result after all required execution-task changes are merged.

Defects found in integration testing create linked fix work for the same delivery unit and keep the parent delivery unit open until the fix path is merged and retested.

## Mandatory Link Rules

The future template assumes these minimum validity rules:

- `requirement` may exist without inbound links; a replacement version must reference the prior version through `supersedes`
- `specification` must refine at least one `requirement`
- `architecture_decision` may exist without inbound links; a replacement decision must reference the prior decision through `supersedes`
- `delivery_unit` must be created from at least one upstream `requirement` or `specification`
- `contour_task` must have exactly one parent `delivery_unit`
- `contour_task` must depend on at least one `specification` or `architecture_decision`
- `execution_task` must have exactly one parent `contour_task`
- `execution_task` must implement at least one `specification` or `architecture_decision`
- every `delivery_unit` must declare `architecture_decision_status`
- if `architecture_decision_status = required`, the `delivery_unit` must reference at least one `architecture_decision`
- if `architecture_decision_status = not_required`, the `delivery_unit` must record a rationale for why a separate architecture decision is unnecessary
- if `architecture_decision_status = deferred`, the `delivery_unit` is not implementation-ready
- every `delivery_unit` must declare whether it is `user_facing` or `internal_enabler`
- `internal_enabler` delivery units must define independently verifiable system-level or operational acceptance criteria

Additional readiness assumptions in the future template:

- a `delivery_unit` is not ready for execution until at least one `contour_task` exists
- a `contour_task` is not ready for execution until at least one `execution_task` exists, unless the future workflow explicitly allows an undecomposed contour task as an exception

## Requirement Status

The following items should be treated as already clarified and accepted for the future template unless the customer explicitly reopens them:

- the product being designed is a new template for agent-first specification-driven development
- workflow design discussion is part of requirements elicitation for that new template
- the accepted role model includes requirements analyst, system analyst, architect, implementation coordinator, and implementation executors by contour
- `architecture_decision` is a separate artifact type
- `architecture_decision` is conditionally mandatory at delivery-unit level and is governed by explicit delivery-unit metadata
- `delivery_unit` is the smallest independently implementable and independently acceptable change package
- `delivery_unit` is a canonical repository artifact with a GitHub operational projection
- the future template uses a closed GitHub Project status model for delivery-unit flow
- the future template uses a strict typed-link model rather than a free-form graph
- `implements` belongs only to `execution_task`
- `delivery_unit` is discussed as `единица поставки`
- identifier prefixes use established engineering terms such as `ADR`
- discussed artifact, link, and identifier choices are requirements and accepted design decisions for the future template, not edits to the active workflow of the current template

## Open Questions

- What exact repository artifact shape should be used for canonical `delivery_unit`, `contour_task`, and `execution_task` documents?
- What exact branch strategy should be used for delivery-unit assembly before integration testing?
