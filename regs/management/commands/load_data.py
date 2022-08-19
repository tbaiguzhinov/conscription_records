from django.core.management.base import BaseCommand
import pandas as pd
import datetime

from regs.models import Personnel, Member


def loader(file_path):
    df_main = pd.read_excel(file_path, sheet_name='Sheet1', header=0).fillna("")
    df_secondary = pd.read_excel(file_path, sheet_name='MainReport', header=1).fillna("")
    
    print('Создаем записи сотрудников ...')
    for item, value in df_main.iterrows():
        employee_id = value['Табельный']
        if employee_id:
            pers_data = df_secondary.loc[df_secondary['Табельный номер'] == employee_id]
        else:
            full_name = value['ФИО']
            pers_data = df_secondary.loc[df_secondary['ФИО'] == full_name]
        if not pers_data.empty:
            employee, created = Personnel.objects.update_or_create(
                employee_id = employee_id,
                birthday = datetime.datetime.strptime(pers_data['Дата рождения'].values[0], '%d.%m.%Y') if pers_data['Дата рождения'].values and pers_data['Дата рождения'].values[0] != "" else None,
                defaults={
                    'first_name': pers_data['ФИО'].values[0].split()[1],
                    'last_name': pers_data['ФИО'].values[0].split()[0],
                    'patronimic': pers_data['ФИО'].values[0].split()[2],
                    'birthplace': pers_data['Место рождения'].values[0],
                    'education_level': pers_data['Тип образования'].values[0],
                    'education_institution': pers_data['Наименование учебного заведения'].values[0],
                    'qualification': pers_data['Квалификация/Специальность'].values[0].split('/')[0].strip(),
                    'specialty': pers_data['Квалификация/Специальность'].values[0].split('/')[1].strip() if '/' in pers_data['Квалификация/Специальность'].values[0] else "",
                    'diploma_number': pers_data['Документ об образовании'].values[0],
                    'graduation_year': datetime.datetime.strptime(pers_data['Дата окончания'].values[0], '%d.%m.%Y') if pers_data['Дата окончания'].values[0] != '' else None,
                    'profession': pers_data['Квалификация/Специальность'].values[0].split('/')[0].strip(),
                    'marital_status': pers_data['Семейное положение'].values[0],
                    'passport_series': pers_data['Номер паспорта'].values[0].split()[0] if pers_data['Номер паспорта'].values[0] != '' else None,
                    'passport_no': pers_data['Номер паспорта'].values[0].split()[1] if pers_data['Номер паспорта'].values[0] != '' else None,
                    'passport_issue_date': datetime.datetime.strptime(pers_data['Дата выдачи паспорта'].values[0], '%d.%m.%Y') if pers_data['Дата выдачи паспорта'].values[0] != '' and pers_data['Дата выдачи паспорта'].values[0] != '00.00.0000' else None,
                    'passport_issue_authority': pers_data['Паспорт выдан'].values[0],
                    'registration_address': pers_data['Адрес регистрации'].values[0],
                    'actual_adress': pers_data['Фактический адрес'].values[0],
                    'military_category': value['Категория'],
                    'military_rank': value['Воинское звание'],
                    'military_profile': value['Состав'],
                    'military_code': value['Специальность'],
                    'fitness_category': value['Годность к военной службе'],
                    'commissariat': value['Военный комиссариат'],
                }
            )
            if created:
                print(f"   ... {employee}")
                family_members = []
                name = pers_data['Супруг(а)'].values[0]
                birthday = pers_data['Дата рождения Супруга (ги)'].values[0]
                family_members.append({"name": name, "birthday": birthday, "relation": "супруг(а)"})

                name = pers_data['Ребенок 1'].values[0]
                birthday = pers_data['Ребенок 1 Дата рождения'].values[0]
                family_members.append({"name": name, "birthday": birthday, "relation": "ребенок"})

                name = pers_data['Ребенок 2'].values[0]
                birthday = pers_data['Ребенок 2 Дата рождения'].values[0]
                family_members.append({"name": name, "birthday": birthday, "relation": "ребенок"})

                name = pers_data['Ребенок 3'].values[0]
                birthday = pers_data['Ребенок 3 Дата рождения'].values[0]
                family_members.append({"name": name, "birthday": birthday, "relation": "ребенок"})

                for family_member in family_members:
                    name = family_member['name'] if family_member['name'] else None
                    birthyear = family_member['birthday'] if family_member['birthday'] else None
                    relation = family_member['relation']
                    
                    if name and birthyear:
                        Member.objects.create(
                            name = name,
                            birthyear = birthyear,
                            relation = relation,
                            employee = employee)


class Command(BaseCommand):
    help = 'Загрузить данные из Excel'

    def add_arguments(self, parser):
        parser.add_argument('--file_path', type=str, default="Список военно обязанных_1178.xls")

    def handle(self, *args, **options):
        file_path = options['file_path']
        try:
            loader(file_path)
        except FileNotFoundError:
            print('Файл не найден: проверьте, что файл помещен в папку с кодом и правильно называется')
            return