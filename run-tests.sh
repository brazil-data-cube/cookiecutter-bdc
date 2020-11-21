#!/usr/bin/env bash
#
# This file is part of Brazil Data Cube Cookiecutter.
# Copyright (C) 2020 INPE.
#
# Brazil Data Cube Cookiecutter is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle tests setup.py version.py && \
isort setup.py version.py tests --check-only --diff && \
check-manifest --ignore ".travis-*" --ignore ".readthedocs.*" && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest #&& \
pytest
