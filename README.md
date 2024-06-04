# pyleetcode

## Requirements
- Python 3.11.X
- Poetry - python package manager
- Pyenv (Optional) - For managing python versions and using virtual environments

## Setup
```sh
# Activate virtual environment
# In your virtual environment install poetry
pip install setuptools
pip install poetry

poetry install  ## This will install packages from poetry.lock
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
