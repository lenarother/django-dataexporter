import io

from django_dataexporter.csv import CsvExporter


class TestCsvExporter:
    def setup(self):
        self.data = [{'foo': 'bar', 'lorem': 'ipsum'}, {'foo': 'bar2', 'lorem': 'ipsum2'}]

    def test_with_header(self):
        exporter, fobj = CsvExporter(fields=('foo', 'lorem'), header=True).write(self.data)
        assert fobj.getvalue().splitlines() == ['foo,lorem', 'bar,ipsum', 'bar2,ipsum2']

    def test_with_fobj(self):
        fobj = io.StringIO()

        CsvExporter(
            fields=('foo', 'lorem'),
        ).write(self.data, fobj=fobj)
        assert fobj.getvalue().splitlines() == ['foo,lorem', 'bar,ipsum', 'bar2,ipsum2']

    def test_without_header(self):
        exporter, fobj = CsvExporter(fields=('foo', 'lorem'), header=False).write(self.data)
        assert fobj.getvalue().splitlines() == ['bar,ipsum', 'bar2,ipsum2']
