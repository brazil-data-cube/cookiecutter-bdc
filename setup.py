#
# This file is part of Brazil Data Cube Cookiecutter.
# Copyright (C) 2020 INPE.
#
# Brazil Data Cube Cookiecutter is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Brazil Data Cube Cookiecutter."""

from setuptools import setup

readme = open('README.rst').read()

history = open('CHANGES.rst').read()

docs_require = [
    'Sphinx>=2.2',
    'sphinx_rtd_theme',
    'sphinx-copybutton',
]

tests_require = [
    'pytest>=5.2',
    'pytest-cookies>=0.5',
    'pytest-pep8>=1.0',
    'pydocstyle>=4.0',
    'isort>4.3',
    'check-manifest>=0.40',
]

examples_require = [
]

extras_require = {
    'docs': docs_require,
    'examples': examples_require,
    'tests': tests_require,
}

extras_require['all'] = [req for _, reqs in extras_require.items() for req in reqs]

setup_requires = [
    'pytest-runner>=5.2',
]

install_requires = [
    'cookiecutter>=1.7',
]

packages = []

g = {}
with open('version.py', 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='cookiecutter-bdc',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    long_description_content_type = 'text/x-rst',
    keywords=['Template', 'Brazil Data Cube'],
    license='MIT',
    author='Brazil Data Cube Team',
    author_email='brazildatacube@inpe.br',
    url='https://github.com/brazil-data-cube/cookiecutter-bdc',
    project_urls={
        'Repository': 'https://github.com/brazil-data-cube/cookiecutter-bdc',
        'Issues': 'https://github.com/brazil-data-cube/cookiecutter-bdc/issues',
        'Documentation': 'https://cookiecutter-bdc.readthedocs.io/en/latest/'
    },
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
