..
    This file is part of Brazil Data Cube Cookiecutter.
    Copyright (C) 2020 INPE.

    Brazil Data Cube Cookiecutter is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


==========================================
Cookiecutter for Brazil Data Cube Packages
==========================================


.. image:: https://img.shields.io/badge/license-MIT-green
        :target: https://github.com//brazil-data-cube/cookiecutter-bdc/blob/master/LICENSE
        :alt: Software License


.. image:: https://travis-ci.org/brazil-data-cube/cookiecutter-bdc.svg?branch=master
        :target: https://travis-ci.org/brazil-data-cube/cookiecutter-bdc
        :alt: Build Status


.. image:: https://readthedocs.org/projects/cookiecutter-bdc/badge/?version=latest
        :target: https://cookiecutter-bdc.readthedocs.io/en/latest/
        :alt: Documentation Status


.. image:: https://img.shields.io/badge/lifecycle-maturing-blue.svg
        :target: https://www.tidyverse.org/lifecycle/#maturing
        :alt: Software Life Cycle


.. image:: https://img.shields.io/github/tag/brazil-data-cube/cookiecutter-bdc.svg
        :target: https://github.com/brazil-data-cube/cookiecutter-bdc/releases
        :alt: Release


.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord


About
=====


This `Cookiecutter template <https://github.com/cookiecutter/cookiecutter>`_ is designed to help you to bootstrap a new Python package for Brazil Data Cube software stack.


Using the Template
==================


**1.** Install the latest version of `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_ if you haven't installed it yet::

    pip install cookiecutter


**2.** Open your terminal and go to the directory where you would like to create the Python package project.


**3.** At the command line, run the ``cookiecutter`` command, passing in the link to this template::

    cookiecutter https://github.com/brazil-data-cube/cookiecutter-bdc


.. note::

    If you have used this template before, then you will be prompted to update your local copy of the template::

        You've downloaded /home/gribeiro/.cookiecutters/cookiecutter-bdc before. Is it okay to delete and re-download it? [yes]:


    Just type 'yes' and confirm the update.


.. note::

    The ``cookiecutter-bdc`` template will be cloned into ``~/.cookiecutters/`` (or an equivalent folder on Windows).


**4.** You will be prompted for some information regarding your new package:

- **project_name:** A short title, preferable in lower case with hyphenated characters (project name for machines).

- **project_title:** Title of your project with space allowed (project name for humans).

- **project_description:** Short description of the project.

- **project_directory:** The name of the repository for the new package.

- **github_repository:** The full name of the repository under the user or organization.

- **package_name:** The name of the package as understood by Python modules and packages.

- **initial_version:** The initial version of the package.

- **copyright_year:** The current year.

- **use_travis:** If ``y`` (yes), the package will have a hook file for `Travis CI <https://travis-ci.org/>`_ (``.travis.yml``).

- **use_readthedocs:** If ``y`` (yes), the package will have a hook file for `Read the Docs  <https://readthedocs.org/>`_ (``.readthedocs.yml``).

- **use_pypi:** If ``y`` (yes), the package will have a defined section in `Travis CI <https://travis-ci.org/>`_ hook file for deploying the package in the `Python Package Index <https://pypi.org/>`_.


Some of the information above can be filled with default values::

    project_name [wtss.py]: WLTS
    project_title [Python Client Library for WTSS]: Python Cliente Library for Web Land Trajectory Service
    project_description [A client library in Python for the Web Time Series Service (WTSS).]: Python Cliente Library for Web Land Trajectory Service is ...
    project_directory [wlts]:
    github_repository [brazil-data-cube/wlts]:
    package_name [wlts]:
    initial_version [0.1.0]:
    copyright_year [2020]:
    use_travis [y]:
    use_readthedocs [y]:
    use_pypi [y]:


**5.** The project will be created under the folder indicated by the ``project_directory`` entry. In the above example, the ``wlts`` directory will contain the following files and subfolders::

    CHANGES.rst
    docs
    examples
    LICENSE
    MANIFEST.in
    pytest.ini
    README.rst
    run-tests.sh
    setup.cfg
    setup.py
    tests
    wlts


License
=======


.. admonition::
    Copyright (C) 2020 INPE.

    Brazil Data Cube Cookiecutter is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.
