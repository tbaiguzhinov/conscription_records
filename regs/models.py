from django.db import models


class Personnel(models.Model):
    employee_id = models.IntegerField(
        'Табельный номер',
    )    
    first_name = models.CharField(
        'Имя',
        max_length=50
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50
    )
    patronimic = models.CharField(
        'Отчество',
        max_length=50,
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        'Дата рождения',
        null=True,
        blank=True,
    )
    birthplace = models.CharField(
        'Место рождения',
        max_length=200,
        null=True,
        blank=True,
    )
    education_level = models.CharField(
        'Уровень образования',
        max_length=200,
        null=True,
        blank=True,
    )
    education_institution = models.TextField(
        'Наименование образовательной организации',
        null=True,
        blank=True,
    )
    qualification = models.CharField(
        'Квалификация',
        max_length=50,
        null=True,
        blank=True,
    )
    specialty = models.CharField(
        'Специальность',
        max_length=50,
        null=True,
        blank=True,
    )
    diploma_number = models.CharField(
        'Серия и номер диплома',
        max_length=50,
        null=True,
        blank=True,
    )
    graduation_year = models.DateField(
        'Год окончания',
        null=True,
        blank=True,
    )
    profession = models.CharField(
        'Профессия',
        max_length=50,
        null=True,
        blank=True,
    )
    marital_status = models.CharField(
        'Семейное положение',
        max_length=50,
        null=True,
        blank=True,
    )
    passport_series = models.IntegerField(
        'Серия паспорта',
        null=True,
        blank=True,

    )
    passport_no = models.IntegerField(
        'Номер паспорта',
        null=True,
        blank=True,
    )
    passport_issue_date = models.DateField(
        'Дата выдачи',
        null=True,
        blank=True,
    )
    passport_issue_authority = models.TextField(
        'Кем выдано',
        null=True,
        blank=True,
    )
    registration_address = models.TextField(
        'Адрес регистрации',
        null=True,
        blank=True,
    )
    actual_adress = models.TextField(
        'Фактический адрес',
        null=True,
        blank=True,
    )
    military_category = models.CharField(
        'Категория запаса',
        max_length=100,
        null=True,
        blank=True,
    )
    military_rank = models.CharField(
        'Воинское звание',
        max_length=100,
        null=True,
        blank=True,
    )
    military_profile = models.CharField(
        'Состав (профиль)',
        max_length=100,
        null=True,
        blank=True,
    )
    military_code = models.CharField(
        'Полное кодовое обознчание ВУС',
        max_length=100,
        null=True,
        blank=True,
    )
    fitness_category = models.CharField(
        'Категория годности к военной службе',
        max_length=100,
        null=True,
        blank=True,
    )
    commissariat = models.TextField(
        'Наименование военного комиссариата по месту воинского учета',
        null=True,
        blank=True,
    )
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        if self.patronimic:
            return f'{self.last_name} {self.first_name} {self.patronimic}'
        else:
            return f'{self.last_name} {self.first_name}'


class Member(models.Model):
    name = models.CharField(
        'Фамилия, имя, отчество',
        max_length=100,
    )
    birthyear = models.CharField(
        'Год рождения',
        max_length=50,
        blank=True,
        null=True,
    )
    relation = models.CharField(
        'Степень родства',
        max_length=100,
    )
    employee = models.ForeignKey(
        Personnel,
        related_name='family_members',
        verbose_name='Сотрудник',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Член семьи"
        verbose_name_plural = "Члены семьи"
    
    def __str__(self):
        return f"{self.name} - {self.employee} "