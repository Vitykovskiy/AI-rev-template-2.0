# Execution Task Template

## Metadata
- Execution Task ID: `ET-XX-###-##`
- Title: `<execution task title>`
- Status: `Draft | Ready for Approval | Approved | Ready for Implementation | In Implementation | In Review | Ready for Integration Testing | In Integration Testing | Waiting for Fix | Ready for Acceptance | Accepted | Ready for Release | Released | Done | Blocked | Cancelled`

## Parent Contour Task
- `CT-XX-###`

## Responsibility
- `<atomic implementation responsibility>`

## Inputs
- `<input artifact, code path, or decision>`

## Outputs
- `<expected output>`

## Implements
- `SPEC-###`

## Depends On
- `<another execution task, if any>`

## Readiness Criteria
- `<what must be true before work starts>`

## Definition of Done
- `<what must be true before closure>`

## Typed Links
- `contour_task -> execution_task : decomposes_into`
- `execution_task -> specification : implements`
- `execution_task -> architecture_decision : implements`

