# PR Policy And Branch Strategy

## Principle

The branch model exists to preserve traceability and reviewability.

It must not become a second task model.

## Branch Strategy

- `main` is protected and represents the integrated baseline.
- One short-lived branch is created per execution task.
- Branch names should encode the execution-task id and a short slug.
- Contour tasks are not branch units.
- A branch may only carry one active execution task unless a linked fix task is explicitly created.

## Pull Request Policy

- Non-code PRs are allowed for approved requirements baseline and delivery-unit package agreement.
- Every atomic execution task produces its own pull request.
- The PR title must include the execution-task id.
- The PR body must list the canonical ids it implements.
- The PR body must list the validation evidence and any remaining risk.
- Review comments that change scope must be reflected back into the canonical documents.

## Merge Rules

- A pull request may merge only after the required approvals and checks succeed.
- A pull request may not merge while the delivery unit is blocked.
- A pull request may not merge if it introduces an unrecorded non-local change.
- A pull request may not bypass review by direct push to `main`.

## Recommended Naming Pattern

- Requirements baseline branch: `req/<requirement-id>-<slug>`
- Delivery-unit package branch: `du/<delivery-unit-id>-package`
- Execution branch: `et/<execution-task-id>-<slug>`
- Fix branch: `fix/<delivery-unit-id>-<slug>`
- Pull request title: `[<execution-task-id>] <short summary>`

## Traceability Rule

- If the PR is merged, the merge commit or squash commit must still preserve the execution-task id in the merged record.
- If the repository uses a different merge method, it must still preserve the canonical task reference.
