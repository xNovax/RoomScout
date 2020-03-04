# Generated by Django 3.0.3 on 2020-02-12 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0005_auto_20200212_1641'),
        ('main', '0005_remove_contactmessage_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='ip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='security.IP'),
        ),
    ]