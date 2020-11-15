{% include 'template/header.rst' %}

{{ cookiecutter.package_name | upper }} API
{{ '=' * (cookiecutter.package_name | length + 4) }}


.. automodule:: {{ cookiecutter.package_name }}.{{ cookiecutter.package_name }}


.. toctree::
    :maxdepth: 1
    :caption: Classes:

    class_{{ cookiecutter.package_name }}