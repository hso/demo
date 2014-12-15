from django.core.management.base import BaseCommand, CommandError
from petl.fluent import fromcsv
from django.db import connection


class Command(BaseCommand):
    args = '<filename>'
    help = 'Loads initial product data from csv'

    def handle(self, *args, **options):
        try:
            filename = args[0]
        except IndexError:
            raise CommandError('You must provide a filename')
        else:
            table = fromcsv(filename, delimiter=';').rename({'COD_LOCAL': 'retail_code',
                                                             'CodMaterial': 'material_code',
                                                             'DESCRIPCION': 'description',
                                                             'Instock': 'in_stock',
                                                             'CodInterno': 'internal_code'})
            table.progress().todb(connection.cursor(), 'stock_product')
            self.stdout.write('Successfully loaded product data')
