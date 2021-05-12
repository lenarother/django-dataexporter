from datetime import date

from django.core.exceptions import FieldDoesNotExist
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.utils.text import slugify


class Exporter(object):
    export_name = 'Export'

    fields = ()
    field_header_verbose_names = None
    header = True

    filename_template = '{date}-{name}.{ext}'
    filename_extension = 'txt'

    http_content_type = 'text/plain'

    def __init__(self, fields=None, header=None, field_header_verbose_names=None):
        """
        Initializes the exporter. Allows overwriting of most property-based configuration.
        """
        self.fields = fields or self.fields
        self.header = header if header is not None else self.header
        self.field_header_verbose_names = field_header_verbose_names or (
            self.field_header_verbose_names or {}
        )

    def get_export_name(self):
        return str(self.export_name)

    def get_filename(self):
        """
        Generate a filename based on a template.
        """
        return self.filename_template.format(
            date=date.today().strftime('%Y-%m-%d'),
            name=slugify(self.get_export_name().lower()),
            ext=self.filename_extension,
        )

    def get_header(self, queryset):
        """
        Helper to extract field header names from queryset. Special handling
        for 'dotted' fields. Tries to look up a better name in field header
        verbose names.
        """
        header_columns = []

        if isinstance(queryset, QuerySet):
            columns = self.get_header_columns_from_queryset(queryset)
        else:
            columns = self.get_header_colums(queryset)

        for field, column in zip(self.fields, columns):
            column = self.field_header_verbose_names.get(
                field, column.split('.')[-1] if field == column else column
            )
            header_columns.append(str(column))

        return header_columns

    def get_header_colums(self, queryset):
        """
        If no queryset is available, we assume that the fields names are used
        as header labels."
        """
        return self.fields

    def get_header_columns_from_queryset(self, queryset):
        base_obj = queryset[0]
        columns = []
        for field in self.fields:
            obj = base_obj
            parts = field.split('.')
            obj_path = parts[:-1]
            field_name = parts[-1]

            for part in obj_path:
                obj = getattr(obj, part)
            try:
                columns.append(str(obj._meta.get_field(field_name).verbose_name))
            except (AttributeError, FieldDoesNotExist):
                columns.append(field)

        return columns

    def get_data(self, queryset):
        """
        Usually, get_date expects a tuple with header fields and an iterable with
        data. We use a generator here to speed up generation and reduce memory
        consumption.
        """

        def data_generator():
            for record in queryset:
                yield dict(
                    [(field, self.get_data_value(record, field)) for field in self.fields]
                )

        return (self.fields, data_generator())

    def get_data_value(self, record, field):
        """
        Helper to extract data from record. If the field contains dots, a drill
        down is done to fetch data of nested objects or dictionaries.
        """
        fields = field.split('.')
        fields.reverse()
        while fields:
            if isinstance(record, dict):
                record = record.get(fields.pop(), None)
            else:
                record = getattr(record, fields.pop(), None)

            if not record:
                # No data available, cut the loop.
                return ''

            if callable(record):
                record = record()

        return record or ''

    def get_value_repr(self, field, value):
        """
        Convert data value to value for actual export file. By default, just cast to string.
        """
        return str(value)

    def write(queryset, fobj):
        raise NotImplementedError

    def get_http_response(self, request, queryset):
        response = HttpResponse(content_type=self.http_content_type)
        response['Content-Disposition'] = 'attachment; filename=%s' % self.get_filename()
        return self.write(queryset, response)
