# Generated by Django 2.2.4 on 2019-09-09 01:34

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('houses', '0013_auto_20190908_2133'),
	]

	operations = [
		migrations.RemoveField(
			model_name='house',
			name='cats_allowed',
		),
		migrations.RemoveField(
			model_name='house',
			name='dogs_allowed',
		),
		migrations.AddField(
			model_name='house',
			name='has_air_conditioning',
			field=models.BooleanField(default=False),
		),
	]