from django.utils.translation import gettext_lazy as _

from .csv import CsvExporter
from .excel import ExcelExporter


def export_action_factory(cls, fields=None, header=None, label=None):
    def export_view(self, request, queryset):
        exporter = cls(fields=fields, header=header)
        return exporter.get_http_response(request, queryset)

    export_view.short_description = label or _('Export selected records')
    export_view.__name__ = cls.__name__.lower()

    return export_view


def export_csv_action_factory(**kwargs):
    return export_action_factory(CsvExporter, **kwargs)


def export_excel_action_factory(**kwargs):
    return export_action_factory(ExcelExporter, **kwargs)
