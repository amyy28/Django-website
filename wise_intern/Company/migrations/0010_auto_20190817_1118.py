# Generated by Django 2.2.4 on 2019-08-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0009_auto_20190817_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='tax_choice',
        ),
        migrations.AlterField(
            model_name='company',
            name='choice',
            field=models.CharField(choices=[('Fixed', (('Inclusive', 'Inclusive'), ('Exclusive', 'Exclusive'))), ('Percentage', (('Inclusive', 'Inclusive'), ('Exclusive', 'Exclusive')))], default='Fixed', max_length=20),
        ),
    ]
