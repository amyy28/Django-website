# Generated by Django 2.2.4 on 2019-08-16 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Job_openings', '0008_auto_20190816_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobb',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Company'),
        ),
    ]