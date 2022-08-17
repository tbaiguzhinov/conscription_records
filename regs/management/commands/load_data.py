from django.core.management.base import BaseCommand
import pandas as pd


class Command(BaseCommand):
    help = 'Загрузить данные из Excel'

    def add_arguments(self, parser):
        parser.add_argument('--file_path', type=str, default="Список военно обязанных_1178.xls")


    def handle(self, *args, **options):
        file_path = options['file_path']

        df_main = pd.read_excel(file_path, sheet_name='MainReport', header=1).fillna("")
        df_secondary = pd.read_excel(file_path, sheet_name='Sheet1').fillna("")

