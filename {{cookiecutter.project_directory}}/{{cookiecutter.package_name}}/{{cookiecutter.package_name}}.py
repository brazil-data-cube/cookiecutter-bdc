{% include 'template/header.py' -%}

"""{{ cookiecutter.project_title }}."""

class {{ cookiecutter.package_name | upper }}:
    """Implement a client for {{ cookiecutter.package_name | upper }}."""

    def __init__(self):
        """Create a {{ cookiecutter.package_name | upper }} client."""
        #: str: URL for the WTSS server.
        pass
