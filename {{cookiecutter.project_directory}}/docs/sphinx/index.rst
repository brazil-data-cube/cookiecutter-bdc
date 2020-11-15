{% include 'template/header.rst' %}

.. include:: ../../README.rst
   :end-before: About


{{ cookiecutter.project_description }}.


.. toctree::
    :hidden:

    self


.. toctree::
    :maxdepth: 2
    :caption: Documentation:

    installation
    usage
    api
    repository
    history


.. toctree::
    :maxdepth: 1
    :caption: Additional Notes

    license