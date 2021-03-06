# Generated by Django 2.2.4 on 2019-09-21 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('houses', '0014_auto_20190908_2134'),
        ('utils', '0006_phonenumberverification'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('publicimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.PublicImage')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.House')),
            ],
            bases=('utils.publicimage',),
        ),
    ]
