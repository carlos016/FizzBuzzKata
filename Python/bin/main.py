"""
main.py
=======

Command-line interface for running the FizzBuzz game.

This script allows the user to run the FizzBuzz game interactively,
setting a custom limit and displaying the results in the terminal.

Example:
    ...\FizzBuzzKata\Python$ python -m bin.main
"""

import argparse
import sys

from src.fizzbuzz import FizzBuzz


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the FizzBuzz sequence to a given limit.")
    parser.add_argument(
        "limit",
        nargs="?",
        type=int,
        help="Optional positive integer limit (default: 100)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point for the FizzBuzz CLI.

    Returns 0 on success, non-zero on error. `argv` is provided for testability.
    """
    argv = argv if argv is not None else sys.argv[1:]
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        fb = FizzBuzz()
        if args.limit is not None:
            fb.limit = args.limit
        print(fb.play_to_text())
        return 0
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())