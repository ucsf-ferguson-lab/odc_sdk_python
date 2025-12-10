# Technical Readme

## Local build

Must run in current working dir, can't use bash or makefile to run.

```shell
python3 -m build
```

https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

## Design decisions

1. Reduced number of 3rd party dependencies to bare-minimum. For example, used dataclasses (included with python install) over pydantic.
1. Multiple layers of abstraction. The target audience has beginner to intermediate Python knowledge. Very likely uncomfortable with reading self-documenting code or functions with many arguments.
1. Synchronous. Done to keep number of 3rd party dependencies to bare-minimum. Also for target audience.
1. Type annotations. These are included even if target audience not required to use it. Note Python is not a type-safe language: type checks not performed at runtime. Intend to be paired with linter.
1. Convert some responses to dataframe and keeping others as json. Data originally in tabular format (tidy format, .csv files) are converted to pandas dataframe to match original representation. Other data not easily represented in tabular format are kept as json. Converting non-tabular data to tabular format is possible but not best use of limited manpower (I'm the only developer working on this package).
