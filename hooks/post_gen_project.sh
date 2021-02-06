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
# Some files are specific to a project flavour
#
echo -n "Removing unused files for flavour {{ cookiecutter.project_flavour }}... "

{%- if cookiecutter.project_flavour == 'Library' %}
rm docs/sphinx/class_{{cookiecutter.package_name}}.rst
{%- endif %}

{%- if cookiecutter.project_flavour != 'Client Web Service' %}
rm {{cookiecutter.package_name}}/{{cookiecutter.package_name}}.py
{%- endif %}

{%- if cookiecutter.project_flavour != 'Flask Web Service' %}
rm {{cookiecutter.package_name}}/ext.py
{%- endif %}

echo "OK!"


#
# If Travis CI is not used, remove its hook file.
#
{%- if cookiecutter.use_travis == 'n' %}
echo -n "Not using Travis CI... "
rm .travis.yml
echo "OK!"
{%- endif %}


#
# If Drone is not used, remove its hook file.
#
{%- if cookiecutter.use_drone != 'y' %}
echo -n "Not using Drone... "
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
