# python-starter

A straightforward starter template for Python packages.

Includes things like:

- All necessary files and paths in `.gitignore`
- `setup.cfg` configuration
- Local development using `requirements.txt` and `requirements-dev.txt`
- Tools like `mypy`, `black`, `pytest` and `tox` set up out of the box

## Usage

Install [cookiecutter](https://pypi.org/p/cookiecutter) and run the following:

```text
cookiecutter gh:tusharsadhwani/py
```

Or if you have `pipx` installed, you can use it directly like so:

```text
pipx run cookiecutter gh:tusharsadhwani/py
```

Cookiecutter will ask you information like the project name, your email and
GitHub username, and then it will produce the following tree structure:

```text
.
├── src
│   └── <project name>
│       ├── __init__.py
│       ├── __main__.py
│       └── py.typed
├── tests
│   └── <project name>_test.py
├── LICENSE
├── mypy.ini
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── setup.cfg
├── setup.py
└── tox.ini
```

Now create and activate a virtual environment, and run:

```text
pip install -r requirements-dev.txt
```

You're ready to start writing code!

To ensure that the project installation was correct:

- Run `pytest` to run the sample test case, and ensure it passes.
- Type the name of your project in the terminal, to run the sample CLI command.
