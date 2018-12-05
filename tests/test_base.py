from datetime import date

import pytest

from django_exporter.base import Exporter
from tests.mockapp.models import DummyModel


@pytest.mark.django_db
class TestExporter:

    def test_init(self):
        exporter = Exporter()

        assert exporter.fields == ()
        assert exporter.header is True
        assert exporter.field_header_verbose_names == {}

    def test_init_with_kwargs(self):
        fields = ('foo',)
        header = False
        field_header_verbose_names = {'foo': 'bar'}
        exporter = Exporter(
            fields=fields, header=header, field_header_verbose_names=field_header_verbose_names)

        assert exporter.fields == fields
        assert exporter.header is header
        assert exporter.field_header_verbose_names == field_header_verbose_names

    def test_get_export_name(self):
        assert Exporter().export_name == 'Export'

    def test_get_filename(self):
        expected_name = '{0}-export.txt'.format(date.today().strftime('%Y-%m-%d'))

        assert Exporter().get_filename() == expected_name

    def test_get_header_with_queryset_without_fields(self):
        name = 'Foo'
        slug = 'bar'
        email = 'foo@bar.baz'
        DummyModel.objects.create(name=name, slug=slug, email=email)
        exporter = Exporter()

        assert exporter.get_header(DummyModel.objects.all()) == []

    def test_get_header_with_queryset_with_fields(self):
        name = 'Foo'
        slug = 'bar'
        email = 'foo@bar.baz'
        fields = ('name', 'slug', 'email')
        DummyModel.objects.create(name=name, slug=slug, email=email)
        exporter = Exporter(fields=fields)

        assert exporter.get_header(DummyModel.objects.all()) == list(fields)

    def test_get_header_without_queryset_with_fields(self):
        name = 'Foo'
        slug = 'bar'
        email = 'foo@bar.baz'
        fields = ('name', 'slug', 'email')
        DummyModel.objects.create(name=name, slug=slug, email=email)
        exporter = Exporter(fields=fields)

        assert exporter.get_header(None) == ['name', 'slug', 'email']

    def test_get_header_without_queryset_with_field_header_verbose_names(self):
        name = 'Foo'
        slug = 'bar'
        email = 'foo@bar.baz'
        fields = ('name', 'slug.Foo', 'email')
        field_header_verbose_names = {'name': 'Firstname', 'email': 'E-mail'}
        DummyModel.objects.create(name=name, slug=slug, email=email)
        exporter = Exporter(
            fields=fields, field_header_verbose_names=field_header_verbose_names)

        assert exporter.get_header(None) == ['Firstname', 'Foo', 'E-mail']

    def test_get_header_with_queryset_with_field_header_verbose_names(self):
        name = 'Foo'
        slug = 'bar'
        email = 'foo@bar.baz'
        fields = ('name', 'slug', 'email')
        field_header_verbose_names = {'name': 'Firstname', 'email': 'E-mail'}
        DummyModel.objects.create(name=name, slug=slug, email=email)
        exporter = Exporter(
            fields=fields, field_header_verbose_names=field_header_verbose_names)

        assert exporter.get_header(DummyModel.objects.all()) == ['Firstname', 'slug', 'E-mail']

    def test_get_header_with_queryset_with_field_header_verbose_names_dotted_fields(self):
        name = 'Foo'
        slug = 'bar'
        email = 'foo@bar.baz'
        fields = ('name', 'slug.lower', 'email')
        field_header_verbose_names = {'name': 'Firstname', 'email': 'E-mail'}
        DummyModel.objects.create(name=name, slug=slug, email=email)
        exporter = Exporter(
            fields=fields, field_header_verbose_names=field_header_verbose_names)

        assert exporter.get_header(DummyModel.objects.all()) == ['Firstname', 'lower', 'E-mail']

    def test_get_header_columns(self):
        assert Exporter().get_header_colums(DummyModel.objects.all()) == ()
