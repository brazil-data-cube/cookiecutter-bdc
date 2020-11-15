{% include 'template/header.rst' %}

{{ cookiecutter.package_name | upper }}
{{ '=' * (cookiecutter.package_name | length) }}


.. autoclass:: {{ cookiecutter.package_name }}.{{ cookiecutter.package_name }}::{{ cookiecutter.package_name | upper }}
    :members:
    :private-members:
    :special-members: __init__, __getitem__, __getattr__
    :member-order: bysource