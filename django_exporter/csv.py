import csv
import io

from .base import Exporter


class CsvExporterMixin(object):
    filename_extension = 'csv'
    http_content_type = 'text/csv'

    def get_writer(self, fobj):
        if not fobj:
            fobj = io.StringIO()
        return csv.writer(fobj, dialect=csv.excel)

    def write_header(self, writer, queryset):
        writer.writerow([str(name) for name in self.get_header(queryset)])

    def write(self, queryset, fobj=None):
        """
        Generate CSV data. If fobj is provided, the content is written to that file
        object. If no fobj is provided, a csv.writer (with a attached io.StringIO)
        object is returned.
        """
        writer = self.get_writer(fobj)
        if self.header:
            self.write_header(writer, queryset)

        data_fields, data = self.get_data(queryset)
        for row in data:
            writer.writerow([
                self.get_value_repr(field, row.get(field, ''))
                for field in data_fields
            ])

        if fobj:
            return fobj

        return writer


class CsvExporter(CsvExporterMixin, Exporter):
    pass
