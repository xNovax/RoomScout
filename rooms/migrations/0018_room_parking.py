# Generated by Django 2.2.4 on 2019-10-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rooms', '0017_auto_20191001_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='parking',
            field=models.BooleanField(default=False, help_text='Parking spot is included or available'),
        ),
    ]
