# Generated by Django 3.0.3 on 2020-03-15 01:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('payments', '0002_auto_20191229_1937'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
