{% include 'template/header.rst' %}

{{ cookiecutter.package_name | upper }}
{{ '=' * (cookiecutter.package_name | length) }}


{%- if cookiecutter.project_flavour == 'Client Web Service' -%}
.. autoclass:: {{ cookiecutter.package_name }}.{{ cookiecutter.package_name }}::{{ cookiecutter.package_name | upper }}
    :members:
    :private-members:
    :special-members: __init__, __getitem__, __getattr__
    :member-order: bysource
{%- endif %}

{% if cookiecutter.project_flavour == 'Flask Web Service' %}
.. autoclass:: {{ cookiecutter.package_name }}.ext::{{ cookiecutter.package_name | upper }}
    :members:
    :private-members:
    :special-members: __init__
    :member-order: bysource
{%- endif %}