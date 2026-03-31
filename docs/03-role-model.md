# Role Model

## Roles

- Requirements analyst
- System analyst
- Architect
- Delivery-unit owner
- Implementation coordinator
- Executor
- Reviewer
- Validator

## Responsibilities

- Requirements analyst: produces and maintains the requirements baseline.
- System analyst: produces the system specification, defines delivery units, and manages specification-level change control.
- Architect: produces architecture decisions, constraints, and architecture-level change control.
- Delivery-unit owner: owns the delivery boundary and approves package completeness.
- Implementation coordinator: decomposes a contour task into parallelizable execution tasks.
- Executor: implements execution tasks.
- Reviewer: checks execution-task correctness before merge.
- Validator: confirms delivery-unit level readiness and integration results.

## Role Boundaries

- The system analyst cannot approve architecture decisions alone when `architecture_decision_status = required`.
- The architect cannot widen delivery-unit scope through architecture prose.
- The delivery-unit owner cannot rewrite execution details inside a contour task.
- The implementation coordinator cannot change delivery-unit boundaries, artifact ownership, or architecture constraints.
- The executor cannot redefine scope; it can only implement the approved execution task.

## Contour Rule

Each contour has its own implementation coordinator.

The coordinator works only inside that contour and cannot change delivery-unit boundaries, contracts, or architecture constraints.

## Parallelism Rule

Parallel decomposition is allowed only when change areas are independent and there is no hard sequential dependency.

If safe decomposition is impossible, the contour task may be executed sequentially.

## Subagent Triggers

Subagents are used only when a bounded specialist context is strictly cheaper than broad context reconstruction.

Allowed triggers:

- system analysis support for ambiguous requirements or missing specification detail;
- architecture support for non-local change evaluation;
- internal code or document review before a pull request is merged;
- parallel execution of independent tasks;
- validation support when a delivery unit must be checked as an assembled whole.

## Subagent Limits

- A subagent receives only the minimal artifact set required for its task.
- A subagent may not invent new scope.
- A subagent may not override canonical ownership.
- A subagent output is advisory until approved by the owning role.
