# Generated by Django 4.1 on 2022-08-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_alter_thing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='body',
            field=models.CharField(max_length=20),
        ),
    ]