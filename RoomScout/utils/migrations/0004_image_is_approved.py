# Generated by Django 2.2.3 on 2019-07-25 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_auto_20190725_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
