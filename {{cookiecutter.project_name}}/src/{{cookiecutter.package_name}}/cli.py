"""CLI interface for {{cookiecutter.package_name}}."""
from __future__ import annotations

import argparse

from {{cookiecutter.package_name}} import greet


class CLIArgs:
    name: str


def cli(argv: list[str] | None = None) -> int:
    """CLI interface."""
    parser = argparse.ArgumentParser()
    parser.add_argument("name", default="world")
    args = parser.parse_args(argv, namespace=CLIArgs)

    greet(args.name)
    return 0
