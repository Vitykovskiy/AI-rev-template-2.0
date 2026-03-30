# Role Model

## Roles

- Requirements analyst
- System analyst
- Architect
- Implementation coordinator
- Implementation executors by contour

## Responsibilities

- Requirements analyst: produces the requirements baseline.
- System analyst: produces the system specification and defines delivery units.
- Architect: produces architecture decisions and constraints.
- Implementation coordinator: decomposes a contour task into parallelizable execution tasks.
- Executors: implement execution tasks.

## Contour Rule

Each contour has its own implementation coordinator.

The coordinator works only inside that contour and cannot change delivery-unit boundaries, contracts, or architecture constraints.

## Parallelism Rule

Parallel decomposition is allowed only when change areas are independent and there is no hard sequential dependency.

If safe decomposition is impossible, the contour task may be executed sequentially.

## Subagent Rule

Subagents are used only in these cases:

- system analyst and architect interaction;
- internal code review before a code pull request;
- parallel execution of independent tasks.
