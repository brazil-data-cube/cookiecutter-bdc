{% include 'template/header.py' -%}

"""Configuration options for {{ cookiecutter.project_title }}."""

import os

_BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_settings(env):
    """Get the given enviroment configuration."""
    return CONFIG.get(env)

class Config:
    """Base Configuration."""

    DEBUG = False
    TESTING = False

    SECRET_KEY = 'secret-key'

    {{ cookiecutter.package_name | upper }}_BASE_PATH_TEMPLATES = os.getenv('{{ cookiecutter.package_name | upper }}_BASE_PATH_TEMPLATES', 'templates')

    {{ cookiecutter.package_name | upper }}_SMTP_PORT = os.getenv('{{ cookiecutter.package_name | upper }}_SMTP_PORT', 587)
    {{ cookiecutter.package_name | upper }}_SMTP_HOST = os.getenv('{{ cookiecutter.package_name | upper }}_SMTP_HOST', None)

    {{ cookiecutter.package_name | upper }}_EMAIL_ADDRESS = os.getenv('{{ cookiecutter.package_name | upper }}_EMAIL_ADDRESS', None)
    {{ cookiecutter.package_name | upper }}_EMAIL_PASSWORD = os.getenv('{{ cookiecutter.package_name | upper }}_EMAIL_PASSWORD', None)

    {{ cookiecutter.package_name | upper }}_APM_APP_NAME = os.environ.get('BDC_AUTH_APM_APP_NAME', None)
    {{ cookiecutter.package_name | upper }}_APM_HOST = os.environ.get('BDC_AUTH_APM_HOST', None)
    {{ cookiecutter.package_name | upper }}_APM_SECRET_TOKEN = os.environ.get('BDC_AUTH_APM_SECRET_TOKEN', None)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:postgres@localhost:5432/{{ cookiecutter.package_name }}')

    OAUTH2_REFRESH_TOKEN_GENERATOR = True

    # Default OAuth 2.0 client app for Brazil Data Cube
    {{ cookiecutter.package_name | upper }}_DEFAULT_APP = 'bdc-auth'

    # Base path used in production (with proxy)
    APPLICATION_ROOT = os.getenv('{{ cookiecutter.package_name | upper }}_PREFIX', '/')
    SESSION_COOKIE_PATH = os.getenv('SESSION_COOKIE_PATH', '/')

    # Logstash configuration
    BDC_LOGSTASH_URL = os.getenv('BDC_LOGSTASH_URL', 'localhost')
    BDC_LOGSTASH_PORT = os.getenv('BDC_LOGSTASH_PORT', 5044)


class ProductionConfig(Config):
    """Production Mode."""


class DevelopmentConfig(Config):
    """Development Mode."""

    DEVELOPMENT = True


class TestingConfig(Config):
    """Testing Mode (Continous Integration)."""

    TESTING = True
    DEBUG = True


CONFIG = {
    "DevelopmentConfig": DevelopmentConfig(),
    "ProductionConfig": ProductionConfig(),
    "TestingConfig": TestingConfig()
}