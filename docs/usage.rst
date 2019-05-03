Usage
=====

The API of the Exporter class is subject to change and therefore not yet documented.


Admin actions
-------------

The library provides admin action factories for csv and xlsx formats.

.. code-block:: python

    from django.contrib import admin
    from django_dataexporter.admin import export_csv_action_factory, export_excel_action_factory

    from .models import User


    class UserAdmin(admin.ModelAdmin):
        export_fields = ('id', 'first_name', 'last_name')
        actions = [
            export_csv_action_factory(fields=export_fields, header=True, label='Export as CSV'),
            export_excel_action_factory(fields=export_fields, header=True, label='Export as XLSX'),
        ]


The dataexporter classes can be also used inside an admin function.
It is especially handy when defining a custom dataexporter class.

.. code-block:: python

    from django.contrib import admin
    from django_dataexporter.csv import CsvExporter
    from django_dataexporter.excel import ExcelExporter

    from .models import User


    class CustomExporter(CsvExporter):
        export_name = 'Custom'
        fields = ['first_name', 'last_name']
        field_header_verbose_names = {'last_name': 'Surname'}
        filename_extension = 'txt'

        def get_data_value(self, record, field):
            record = super().get_data_value(record, field)
            return record or 'Sorry, no data here.'


    class UserAdmin(admin.ModelAdmin):
        export_fields = ('id', 'first_name', 'last_name')
        actions = ['csv_export', 'excel_export', 'custom_export']

        def csv_export(self, request, queryset):
            exporter = CsvExporter(fields=self.export_fields, header=True)
            return exporter.get_http_response(request, queryset)
        csv_export.short_description = 'Export surveys as CSV'

        def excel_export(self, request, queryset):
            exporter = ExcelExporter(fields=self.export_fields, header=True)
            return exporter.get_http_response(request, queryset)
        excel_export.short_description = 'Export surveys as XLSX'

        def custom_export(self, request, queryset):
            exporter = CustomExporter()
            return exporter.get_http_response(request, queryset)
        custom_export.short_description = 'Export name and surname only'
