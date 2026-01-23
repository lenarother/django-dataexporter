django-dataexporter
===================

.. image:: https://img.shields.io/pypi/v/django-dataexporter.svg
   :target: https://pypi.org/project/django-dataexporter/
   :alt: Latest Version

.. image:: https://github.com/stephrdev/django-tapeforms/workflows/Test/badge.svg?branch=master
   :target: https://github.com/lenarother/django-dataexporter/actions?workflow=Test
   :alt: CI Status

.. image:: https://codecov.io/gh/lenarother/django-dataexporter/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lenarother/django-dataexporter
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-dataexporter/badge/?version=latest
   :target: https://django-dataexporter.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status


*django-dataexporter* is a extensible helper to export Django QuerySets and other data to CSV and Excel.


Features
--------

* Exporter class to generate CSV and Excel files out of QuerySets and other iterables.
* Factory to generate Django ModelAdmin actions to trigger an export out of Django's famous admin interface.


Requirements
------------

django-dataexporter supports Python 3.10+ and Django 3.2+.
In addition, the Python package ``openpyxl`` needs to be installed.


Prepare for development
-----------------------

A Python 3.10+ interpreter is required in addition to uv.

Install uv:

.. code-block:: shell

    $ curl -LsSf https://astral.sh/uv/install.sh | sh
    # or
    $ pip install uv

Install dependencies:

.. code-block:: shell

    $ uv sync --extra dev

Set up pre-commit hooks (optional but recommended):

.. code-block:: shell

    $ uv run pre-commit install

Now you're ready to run the tests:

.. code-block:: shell

    $ uv run pytest

Run linting and formatting checks:

.. code-block:: shell

    $ uv run ruff check .
    $ uv run ruff format --check .

Run tests with coverage:

.. code-block:: shell

    $ uv run pytest --cov

Run tests across multiple Python and Django versions (includes linting):

.. code-block:: shell

    $ uv run tox

Format code with ruff:

.. code-block:: shell

    $ uv run ruff format .

Run pre-commit on all files:

.. code-block:: shell

    $ uv run pre-commit run --all-files


Resources
---------

* `Documentation <https://django-dataexporter.readthedocs.io>`_
* `Bug Tracker <https://github.com/lenarother/django-dataexporter/issues>`_
* `Code <https://github.com/lenarother/django-dataexporter/>`_
