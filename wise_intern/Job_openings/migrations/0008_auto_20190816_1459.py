# Generated by Django 2.2.4 on 2019-08-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_openings', '0007_auto_20190816_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobb',
            name='company',
            field=models.CharField(max_length=100),
        ),
    ]