# Generated by Django 2.2.4 on 2019-08-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0003_auto_20190809_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10),
        ),
    ]
