#
# This file is part of Brazil Data Cube Cookiecutter.
# Copyright (C) 2020 INPE.
#
# Brazil Data Cube Cookiecutter is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for Brazil Data Cube Cookiecutter."""

import datetime
from contextlib import contextmanager

import pytest


@contextmanager
def bake(cookies, *args, **kwargs):
    """Define a wrapper over ``cookie.bake`` method that allows it to be used in ``with`` statements.

    Args:
        cookies (pytest_cookies.Cookies): cookie to be baked.
    """
    result = cookies.bake(*args, **kwargs)

    try:
        yield result
    finally:
        pass


def test_copyright_year_compute_in_license_file(cookies):
    """Test copyright year compute."""
    with bake(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        license_file_path = result.project.join('LICENSE')
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()

    with bake(cookies, extra_context={'copyright_year': '2018-2019'}) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        license_file_path = result.project.join('LICENSE')
        assert '2018-2019' in license_file_path.read()


@pytest.mark.parametrize(
    'option, file_name', [
        ('use_travis', '.travis.yml'),
        ('use_readthedocs', '.readthedocs.yml'),
    ]
)
def test_files_not_generated(cookies, option, file_name):
    """Test if the ``.travis.yml`` and other type of files are not generated."""
    with bake(cookies, extra_context={option: 'no'}) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        travis_ci_file_path = result.project.join(file_name)
        assert not travis_ci_file_path.check()

