django-exporter
===============

.. image:: https://img.shields.io/pypi/v/django-exporter.svg
   :target: https://pypi.org/project/django-exporter/
   :alt: Latest Version

.. image:: https://codecov.io/gh/moccu/django-exporter/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/moccu/django-exporter
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-exporter/badge/?version=latest
   :target: https://django-exporter.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/moccu/django-exporter.svg?branch=master
   :target: https://travis-ci.org/moccu/django-exporter


*django-exporter* is a extensible helper to export Django QuerySets and other data to CSV and Excel.


Features
--------

* Exporter class to generate CSV and Excel files out of QuerySets and other iterables.
* Factory to generate Django ModelAdmin actions to trigger an export out of Django's famous admin interface.


Requirements
------------

django-exporter supports Python 3 only and requires at least Django 1.11.
In addition, the Python package ``openpyxl`` needs to be installed.


Prepare for development
-----------------------

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6 --dev
    $ pipenv shell
    $ pip install -e .


Now you're ready to run the tests:

.. code-block:: shell

    $ pipenv run py.test


Resources
---------

* `Documentation <https://django-exporter.readthedocs.io>`_
* `Bug Tracker <https://github.com/moccu/django-exporter/issues>`_
* `Code <https://github.com/moccu/django-exporter/>`_
