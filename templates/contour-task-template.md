# Contour Task Template

## Summary

- Task type: `implementation`
- Owner contour: `<frontend/backend/devops/qa-e2e>`
- Initiative: `<epic or parent issue>`
- Parent block task: `<block_delivery issue>`
- GitHub Issue: `<issue id or URL>`
- GitHub Project status: `<Inbox/Ready/In Progress/Blocked/Waiting for Testing/Testing/Waiting for Fix/In Review/Done>`

## Goal

`<what this contour task must deliver>`

## Canonical Inputs

- `<analysis artifact>`
- `<analysis artifact or upstream dependency>`
- `<relevant entry in docs/external-libraries.md / docs/internal-libraries.md or explicit none>`

## Dependencies

- `<task or contract dependency>`

## Definition Of Ready

- [ ] `<all upstream tasks complete>`
- [ ] `<canonical inputs exist>`
- [ ] `<required approved library contracts are linked or explicitly none>`

## Definition Of Done

- [ ] `<criterion>`
- [ ] `<criterion>`

## Blocker Rule

If the task cannot be completed from the listed inputs, or a required approved external/internal library contract is missing, mark it `Blocked` and route it to `system_analysis` for explicit behavior clarification.

## Tracking Rule

This template represents exactly one atomic contour-owned implementation task and must map to exactly one GitHub Issue under exactly one parent `block_delivery` issue.
