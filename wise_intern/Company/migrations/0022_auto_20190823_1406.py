# Generated by Django 2.2.4 on 2019-08-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0021_auto_20190823_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='CTC_type',
            field=models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('Gross', 'Gross')], help_text="Only required if 'Percentage' attributes are selected.", max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='commercials',
            field=models.CharField(choices=[('Fixed', (('Fixed-Inclusive of all Taxes', 'Fixed-Inclusive of all Taxes'), ('Fixed-Exclusive of all Taxes', 'Fixed-Exclusive of all Taxes'))), ('Percentage', (('Percent-Inclusive of all Taxes', 'Percent-Inclusive of all Taxes'), ('Percent-Exclusive of all Taxes', 'Percent-Exclusive of all Taxes')))], default='Fixed', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='value',
            field=models.CharField(help_text='Enter ₹ for Fixed, % for Percentage', max_length=100),
        ),
    ]
