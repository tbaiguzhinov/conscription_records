# Generated by Django 3.2.15 on 2022-08-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='birthday',
        ),
        migrations.AddField(
            model_name='member',
            name='birthyear',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год рождения'),
        ),
    ]