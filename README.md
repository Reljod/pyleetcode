# pyleetcode

## Requirements

- Python 3.13.X
- [uv](https://docs.astral.sh/uv/) - python package manager

## Setup

1. Install `uv` package manager [here.](https://docs.astral.sh/uv/getting-started/installation/)

```sh
# Check if uv is properly installed
uv
```

2. Install package:

```sh
# Create and activate virtual environment
uv venv  # This will create a .venv file
source .venv/bin/activate  # Make sure to activate virtual environment

# Syncs uv lock file to current environment
uv sync
```

## Execute script

```sh
# Activate virtual environment
# python -m <folder>.0XX_problem.py
#
# Note that we run via -m (module) since we want it to recognize top level
# custom libraries that we want to use.
#
# For example:
python -m binary_search.001_problem
```

## Execute Test

```sh
# Activate virtual environment
# pytest <folder>/0XX_problem.py -v
# For example:
python -m pytest binary_search/001_problem.py -v ## -v for more test verbosity
```
