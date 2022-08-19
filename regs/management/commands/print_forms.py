import os

from django.core.management.base import BaseCommand
from django.template.loader import get_template

from regs.models import Personnel

from regs.management.commands.load_data import loader

class Command(BaseCommand):
    help = 'Распечатать формы воинского учета'

    def add_arguments(self, parser):
        parser.add_argument('--noload', action='store_true', help='Не загружать данные')
        parser.add_argument('--overwrite', action='store_true', help='Заново выгрузить все формы')
        parser.add_argument('--employee_id', type=int, nargs='*', help='Табельный номер сотрудника')
        parser.add_argument('--file_path', type=str, default="Список военно обязанных_1178.xls")

    def handle(self, *args, **options):
        if not options['noload']:
            try:
                loader(options['file_path'])
            except FileNotFoundError:
                print('Файл не найден: проверьте, что файл помещен в папку с кодом и правильно называется')
                return

        if options['employee_id']:
            staff = Personnel.objects.filter(employee_id__in=options['employee_id'])
        else:
            staff = Personnel.objects.all()
        
        print("Сохраняем формы ...")

        for employee in staff.iterator():
            context = {
                "personnel": employee
            }
            template = get_template('card-template.html')
            html  = template.render(context)
            
            if not os.path.exists('records'):
                os.makedirs('records')

            file_name = f"{employee.employee_id} - {employee}.html"
            if not options['overwrite'] and os.path.exists(f'records/{file_name}'):
                continue

            with open(f'records/{file_name}', 'w', encoding='utf8') as file:
                file.write(html)

            print(f"   ... {employee}")
