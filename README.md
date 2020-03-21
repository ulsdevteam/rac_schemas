# rac_schemas

JSON schemas and validation helpers

## To Use

### Requirements
*   Python 3.4 or higher
*   [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)
*   [tox](https://tox.readthedocs.io/) (for running tests)
*   [pre-commit](https://pre-commit.com/) (for running linters before committing)
    *   After installing pre-commit, install the git-hook scripts:

    ```
    $ pre-commit install
    ```

### Installation

The recommended way to install this package is using `pip`:

```
pip install rac_schemas
```

### Usage

*Write usage instructions, including configuration details, settings or arguments available.*

#### Tests

`rac_schemas` comes with unit tests as well as linting. The easiest way to make sure all tests pass is to run `tox` from the root of the repository. This will execute all tests, and will also run `autopep8` and `flake8` linters against the codebase.s

### License

See`LICENSE.md`.
