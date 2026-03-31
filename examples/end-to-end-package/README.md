# End-to-End Package Example

This directory contains a machine-checkable example package for the template.

The canonical artifact is `manifest.json`.

Validation commands:

```bash
python tools/validate_package.py --package examples/end-to-end-package
python tools/validate_repo.py
python tools/validate_pr.py --title "scaffolding: add canonical package validation" --body-file .github/pull_request_template.md
```

