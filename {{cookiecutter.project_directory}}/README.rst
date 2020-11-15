{% include 'template/header.rst' %}

{{ '=' * (cookiecutter.project_title | length) }}
{{ cookiecutter.project_title }}
{{ '=' * (cookiecutter.project_title | length) }}


.. image:: https://img.shields.io/badge/license-MIT-green
        :target: https://github.com//{{ cookiecutter.github_repository }}/blob/master/LICENSE
        :alt: Software License


{% if cookiecutter.use_travis == 'y' -%}
.. image:: https://travis-ci.org/{{ cookiecutter.github_repository }}.svg?branch=master
        :target: https://travis-ci.org/{{ cookiecutter.github_repository }}
        :alt: Build Status


.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_repository }}/badge.svg?branch=master
        :target: https://coveralls.io/github/{{ cookiecutter.github_repository }}?branch=master
        :alt: Code Coverage Test


{% endif -%}
{% if cookiecutter.use_readthedocs == 'y' -%}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest
        :target: https://{{ cookiecutter.package_name }}.readthedocs.io/en/latest/
        :alt: Documentation Status


{% endif -%}
.. image:: https://img.shields.io/badge/lifecycle-maturing-blue.svg
        :target: https://www.tidyverse.org/lifecycle/#maturing
        :alt: Software Life Cycle


.. image:: https://img.shields.io/github/tag/{{ cookiecutter.github_repository }}.svg
        :target: https://github.com/{{ cookiecutter.github_repository }}/releases
        :alt: Release


{% if cookiecutter.use_pypi == 'y' -%}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}
        :target: https://pypi.org/project/{{ cookiecutter.package_name }}/
        :alt: Python Package Index


{% endif -%}
.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord


About
=====


{{ cookiecutter.project_description }}