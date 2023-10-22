"""Support executing the CLI by doing `python -m {{cookiecutter.package_name}}`."""
from __future__ import annotations

from {{cookiecutter.package_name}}.cli import cli

if __name__ == "__main__":
    raise SystemExit(cli())
