# Generated by Django 2.2.4 on 2019-08-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_status',
            field=models.CharField(choices=[('1', 'active'), ('2', 'inactive')], default=1, max_length=10),
        ),
    ]
