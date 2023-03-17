"""Support executing the CLI by doing `python -m {{cookiecutter.package_name}}`."""
from {{cookiecutter.package_name}}.cli import cli

if __name__ == "__main__":
    cli()
