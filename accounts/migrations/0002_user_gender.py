# Generated by Django 2.2.4 on 2019-08-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='', max_length=2),
        ),
    ]