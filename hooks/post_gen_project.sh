#!/usr/bin/env bash
#
# This file is part of Brazil Data Cube Cookiecutter.
# Copyright (C) 2020 INPE.
#
# Brazil Data Cube Cookiecutter is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

set -eou pipefail


echo ""
echo "Cookiecutter pos-processing..."
echo ""


#
# Remove folder template and all its content
#
echo -n "Removing template folder... "
rm template/header.py
rm template/header.txt
rm template/header.rst
rmdir template
echo "OK!"


#
# If Travis CI is not used, remove its hook file.
#
{%- if cookiecutter.use_travis != 'y' %}
echo -n "Not using Travis CI... "
rm .travis.yml
echo "OK!"
{%- endif %}


#
# If Read the Docs is not used, remove its hook file.
#
{%- if cookiecutter.use_readthedocs != 'y' %}
echo -n "Not using Travis CI... "
rm .readthedocs.yml
echo "OK!"
{%- endif %}

echo ""
echo "pos-processing finished!"
echo ""