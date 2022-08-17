from django.db import models

class Personnel(models.Model):
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
    dob = models.DateField(
        'Дата рождения',    
    )
