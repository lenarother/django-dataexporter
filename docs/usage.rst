Usage
=====

The API of the Exporter class is subject to change and therefore not yet documented.


Admin actions
-------------

The library provides action factories.

.. code-block:: python

    from django.contrib import admin
    from django_dataexporter.admin import export_csv_action_factory, export_excel_action_factory

    from .models import User


    class UserAdmin(admin.ModelAdmin):
        export_fields = ('id', 'first_name', 'last_name')
        actions = [
            export_csv_action_factory(fields=export_fields, header=True, label='Export as CSV'),
            export_excel_action_factory(fields=export_fields, header=True, label='Export as XLSX')]


The dataexporter classes can be also used inside an admin function.
It is especially handy when defining a custom dataexporter class.

.. code-block:: python

    from django.contrib import admin
    from django_dataexporter.csv import CsvExporter
    from django_dataexporter.excel import ExcelExporter

    from .models import User


    class UserAdmin(admin.ModelAdmin):
        export_fields = ('id', 'first_name', 'last_name')
        actions = ['csv_export', 'excel_export']

        def csv_export(self, request, queryset):
            exporter = CsvExporter(fields=self.export_fields, header=True)
            return exporter.get_http_response(request, queryset)
        csv_export.short_description = _('Export surveys as CSV')

        def excel_export(self, request, queryset):
            exporter = ExcelExporter(fields=self.export_fields, header=True)
            return exporter.get_http_response(request, queryset)
        excel_export.short_description = _('Export surveys as XLSX')
