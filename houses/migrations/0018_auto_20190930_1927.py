# Generated by Django 2.2.4 on 2019-09-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0017_auto_20190929_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='hide_address',
            field=models.BooleanField(default=False, help_text='Hides the specific address on all publicly available pages'),
        ),
    ]
