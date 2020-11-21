{% include 'template/header.py' -%}

"""{{ cookiecutter.project_title }}."""

from . import config


class {{ cookiecutter.package_name | upper }}:
    """{{ cookiecutter.package_name | upper }} extension."""

    def __init__(self, app=None, **kwargs):
        """Extension initialization."""
        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        """Initialize Flask application object."""
        self.init_config(app)
        app.extensions['{{ cookiecutter.package_name }}'] = self

    def init_config(self, app, **kwargs):
        """Initialize configuration."""
        conf = config.get_settings(kwargs['config_name'])

        app.config.from_object(conf)
