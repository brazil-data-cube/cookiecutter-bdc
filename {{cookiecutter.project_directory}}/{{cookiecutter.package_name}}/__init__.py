{% include 'template/header.py' -%}

"""{{ cookiecutter.project_title }}."""

{% if cookiecutter.project_flavour == 'Flask Web Service' -%}
import os

from flask import Flask

from .ext import {{ cookiecutter.package_name | upper }}
{%- endif %}
from .version import __version__

{% if cookiecutter.project_flavour == 'Flask Web Service' %}
def create_app(config_name='DevelopmentConfig'):
    """Create the Flask application from a given config object type.

    Args:
        config_name (string): Config instance name.

    Returns:
        Flask Application with config instance scope.
    """
    app = Flask(__name__)

    {{cookiecutter.package_name | upper}}(app, config_name=config_name)

    return app


app = create_app(os.environ.get('{{ cookiecutter.package_name | upper }}_ENVIRONMENT', 'DevelopmentConfig'))
{%- endif %}

__all__ = (
    '__version__',

    {%- if cookiecutter.project_flavour == 'Flask Web Service' %}
    'create_app',
    {%- endif %}
)
