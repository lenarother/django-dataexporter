Usage
=====

The API of the Exporter class is subject to change and therefore not yet documented.


Admin actions
-------------

The example explains the usage in the best way.

.. code-block:: python

    from django_dataexporter import action_export_factory
    from django.contrib import admin

    from .models import User


    class UserAdmin(admin.ModelAdmin):
        actions = (
            action_export_factory('xlsx')
        )

        export_fields = ('id', 'first_name', 'last_name')

        actions = [
            action_export_factory('csv', 'Export as CSV', export_fields),
            action_export_factory('xlsx', 'Export as XLSX', export_fields)
        ]

