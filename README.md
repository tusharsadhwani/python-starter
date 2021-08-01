# python-starter

A straightforward starter template for Python packages.

Includes things like:

- All necessary files and paths in `.gitignore`
- `setup.cfg` configuration
- Local development using `requirements.txt` and `requirements-dev.txt`
- Tools like `mypy`, `black` and `pytest` set up out of the box

## Setup

- Clone this repo and delete `.git`
- Rename `src/sample_package` folder to your package name
- Rename the package import in `tests/sample_test.py`
- Edit the marked fields in `setup.cfg`, and remove comments
- Edit `LICENSE`
- Setup and activate a [virtualenv](https://docs.python.org/3/tutorial/venv.html)
- Run `pip install -r requirements-dev.txt`
- That's it! See if it worked by running `mycommand` and `python -m <package name>`

## Testing

Run `pytest`

## Type Checking

Run `mypy .`

## Create and upload a package to PyPI

Make sure to bump the version in `setup.cfg`.

Then run the following commands:

```bash
rm -rf build dist
python setup.py sdist bdist_wheel
```

Then upload it to PyPI using [twine](https://twine.readthedocs.io/en/latest/#installation):

```bash
twine upload dist/*
```
