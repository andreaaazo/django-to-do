# Generated by Django 4.1 on 2022-08-28 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0006_thing_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='creation_date',
            field=models.DateField(default=datetime.time, verbose_name='Date'),
        ),
    ]
