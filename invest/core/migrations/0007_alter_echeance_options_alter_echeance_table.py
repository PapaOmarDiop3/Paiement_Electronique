# Generated by Django 4.0 on 2022-12-18 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_echeance_investissement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='echeance',
            options={'verbose_name': 'Echeance', 'verbose_name_plural': 'Echeances'},
        ),
        migrations.AlterModelTable(
            name='echeance',
            table='echeance',
        ),
    ]
