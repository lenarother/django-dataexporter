import io

import pytest

from django_dataexporter.excel import ExcelExporter


class TestExcelExporter:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.data = [{'foo': 'bar', 'lorem': 'ipsum'}, {'foo': 'bar2', 'lorem': 'ipsum2'}]

    def test_with_header(self):
        exporter, fobj = ExcelExporter(fields=('foo', 'lorem'), header=True).write(self.data)
        assert [[cell.value for cell in row] for row in exporter['Export'].iter_rows()] == [
            ['foo', 'lorem'],
            ['bar', 'ipsum'],
            ['bar2', 'ipsum2'],
        ]

    def test_with_fobj(self):
        fobj = io.BytesIO()
        ExcelExporter(
            fields=('foo', 'lorem'),
        ).write(self.data, fobj=fobj)
        assert len(fobj.getvalue()) > 0

    def test_without_header(self):
        exporter, fobj = ExcelExporter(fields=('foo', 'lorem'), header=False).write(self.data)
        assert [[cell.value for cell in row] for row in exporter['Export'].iter_rows()] == [
            ['bar', 'ipsum'],
            ['bar2', 'ipsum2'],
        ]
