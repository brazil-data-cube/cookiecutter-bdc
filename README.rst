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


This `Cookiecutter template <https://github.com/cookiecutter/cookiecutter>`_ is designed to help you to bootstrap a new Python package for the Brazil Data Cube software stack.


Using the Template
==================


**1.** Install the latest version of `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_ if you haven't installed it yet::

    pip install cookiecutter


**2.** Open your terminal and go to the directory where you would like to create the Python package project.


**3.** At the command line, run the ``cookiecutter`` command, passing in the link to this template::

    cookiecutter https://github.com/brazil-data-cube/cookiecutter-bdc

    or,

    cookiecutter gh:brazil-data-cube/cookiecutter-bdc


.. note::

    If you have used this template before, then you will be prompted to update your local copy of the template::

        You've downloaded /home/gribeiro/.cookiecutters/cookiecutter-bdc before. Is it okay to delete and re-download it? [yes]:


    Just type 'yes' and confirm the update.


.. note::

    The ``cookiecutter-bdc`` template will be cloned into ``~/.cookiecutters/`` (or an equivalent folder on Windows).


**4.** You will be prompted for some information regarding your new package:

- **project_flavour:**  The intended type of Python package.

- **project_name:** A short title, preferable in lower case with hyphenated characters (project name for machines).

- **project_title:** Title of your project with space allowed (project name for humans).

- **project_description:** Short description of the project.

- **project_directory:** The name of the repository for the new package.

- **github_repository:** The full name of the repository under the user or organization.

- **package_name:** The name of the package as understood by Python modules and packages.

- **initial_version:** The initial version of the package.

- **copyright_year:** The current year.

- **use_drone:** If ``y`` (yes), the package will have a hook file for `Drone <https://drone.dpi.inpe.br>`_ (``.drone.yml``).

- **use_travis:** If ``y`` (yes), the package will have a hook file for `Travis CI <https://travis-ci.org/>`_ (``.travis.yml``).

- **use_readthedocs:** If ``y`` (yes), the package will have a hook file for `Read the Docs  <https://readthedocs.org/>`_ (``.readthedocs.yml``).

- **use_pypi:** If ``y`` (yes), the package will have a defined section in `Travis CI <https://travis-ci.org/>`_'s or `Drone <https://drone.dpi.inpe.br>`_'s hook file for deploying the package in the `Python Package Index <https://pypi.org/>`_.


Some of the information above can be filled with default values::

    project_flavour:
        Select project_flavour:
        1 - Client Web Service
        2 - Flask Web Service
        3 - Library
        Choose from 1, 2, 3 [1]:
    project_name [wtss.py]: wlts.py
    project_title [Python Client Library for WTSS]: Python Client Library for Web Land Trajectory Service
    project_description [A client library in Python for the Web Time Series Service (WTSS)]: Web Land Trajectory Service is ...
    project_directory [wlts.py]:
    github_repository [brazil-data-cube/wlts.py]:
    package_name [wlts]:
    initial_version [0.1.0]:
    copyright_year [2020]:
    use_drone [y]:
    use_travis [n]:
    use_readthedocs [y]:
    use_pypi [y]:


**5.** The project will be created under the folder indicated by the ``project_directory`` entry. In the above example, the ``wlts.py`` directory will contain the following files and subfolders::

    docs
    examples
    tests
    wlts
    CHANGES.rst
    LICENSE
    MANIFEST.in
    pytest.ini
    README.rst
    run-tests.sh
    setup.cfg
    setup.py


.. note::

    Sometimes it is useful to have a user config file to keep some basic settings. For instance, you could create a file name ``my-config.yaml`` with the folowwing content:


    .. code-block:: yaml
        :caption: A user config file named ``my-config.yaml``.
        :linenos:

        default_context:
            project_flavour: "Client Web Service"
            initial_version: "1.0.0"
        abbreviations:
            bdc: https://github.com/brazil-data-cube/cookiecutter-bdc.git
            gh: https://github.com/{0}.git


    Then, you could call ``cookiecutter`` as::

        cookiecutter --config-file my-config.yaml bdc


Create a Git Repository
=======================


After creating the source tree of your new package, you can initialize a Git repository in it with the ``git init`` command::

    cd wlts.py

    git init


Configure the user ``name`` and ``email``::

    git config user.name <user-name>
    git config user.email <user-email>


Add the source files in the tree with ``git add``::

    git add .


Record changes to the repository with ``git commit``::

    git commit -m "Prepare wlts.py package."


If you do not have a GitHub repository yet, create a new empty one under the `Brazil Data Cube organization <https://github.com/brazil-data-cube>`_. Let's assume you have created one named `brazil-data-cube/wlts.py <https://github.com/brazil-data-cube/wlts.py>`_. Add the remote address with ``git remote``::

    git remote add origin https://github.com/brazil-data-cube/wlts.py.git


And finally, push your local copy to the remote::

    git push origin master


Congratulations! You should have the structure of your new package in GitHub!


.. _readme_license:

License
=======


.. admonition::
    Copyright (C) 2020 INPE.

    Brazil Data Cube Cookiecutter is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.
