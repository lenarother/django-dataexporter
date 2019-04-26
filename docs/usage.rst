Usage
=====

The API of the Exporter class is subject to change and therefore not yet documented.


Admin actions
-------------

The example explains the usage in the best way.

.. code-block:: python

    from django_dataexporter.admin import export_csv_action_factory, export_excel_action_factory
    from django.contrib import admin

    from .models import User


    class UserAdmin(admin.ModelAdmin):
        export_fields = ('id', 'first_name', 'last_name')

        actions = [
                export_csv_action_factory(fields=export_fields, header=True, label='Export as CSV', ),
                export_excel_action_factory(fields=export_fields, header=True, label='Export as XLSX', ),
            ]
