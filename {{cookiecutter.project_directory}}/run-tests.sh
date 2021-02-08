#!/usr/bin/env bash
{% include 'template/header.txt' -%}

pydocstyle {{ cookiecutter.package_name }} examples tests setup.py && \
isort {{ cookiecutter.package_name }} examples tests setup.py --check-only --diff && \
check-manifest --ignore ".travis.yml,.drone.yml,.readthedocs.yml" && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest && \
pytest
