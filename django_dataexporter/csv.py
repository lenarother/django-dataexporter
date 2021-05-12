import csv
import io

from .base import Exporter


class CsvExporterMixin(object):
    filename_extension = 'csv'
    http_content_type = 'text/csv'

    def get_writer(self, fobj):
        if not fobj:
            fobj = io.StringIO()
        writer = csv.writer(fobj, dialect=csv.excel)
        return (writer, fobj)

    def write_header(self, writer, queryset):
        writer.writerow([str(name) for name in self.get_header(queryset)])

    def write(self, queryset, fobj=None):
        """
        Generate CSV data. If fobj is provided, the content is written to that file
        object. If no fobj is provided, a csv.writer (with a attached io.StringIO)
        object and the StringIO fobj is returned.
        """
        writer, writer_fobj = self.get_writer(fobj)
        if self.header:
            self.write_header(writer, queryset)

        data_fields, data = self.get_data(queryset)
        for row in data:
            writer.writerow(
                [self.get_value_repr(field, row.get(field, '')) for field in data_fields]
            )

        if fobj:
            return fobj

        return (writer, writer_fobj)


class CsvExporter(CsvExporterMixin, Exporter):
    pass
