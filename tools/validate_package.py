from __future__ import annotations

import argparse
from pathlib import Path

from sdd_validator import validate_package_dir


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--package",
        default=str(Path(__file__).resolve().parents[1] / "examples" / "end-to-end-package"),
    )
    args = parser.parse_args()
    errors = validate_package_dir(Path(args.package))
    if errors:
        for error in errors:
            print(error)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
