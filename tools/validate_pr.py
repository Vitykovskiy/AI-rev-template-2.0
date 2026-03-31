from __future__ import annotations

import argparse
import os
from pathlib import Path

from sdd_validator import validate_pr


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", default=os.environ.get("PR_TITLE", ""))
    parser.add_argument("--body", default=os.environ.get("PR_BODY", ""))
    parser.add_argument("--body-file", default="")
    args = parser.parse_args()

    body = args.body
    if args.body_file:
        body = Path(args.body_file).read_text(encoding="utf-8")

    errors = validate_pr(args.title, body)
    if errors:
        for error in errors:
            print(error)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
