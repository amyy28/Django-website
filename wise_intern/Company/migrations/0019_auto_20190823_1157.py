# Generated by Django 2.2.4 on 2019-08-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0018_auto_20190823_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='commercials',
            field=models.CharField(choices=[('Fixed', (('Fixed-Inclusive of all Taxes', 'Fixed-Inclusive of all Taxes'), ('Fixed-Exclusive of all Taxes', 'Fixed-Exclusive of all Taxes'))), ('Percentage', (('Percent-Inclusive of all Taxes', 'Percent-Inclusive of all Taxes'), ('Percent-Exclusive of all Taxes', 'Percent-Exclusive of all Taxes')))], default='Fixed', max_length=20),
        ),
    ]
