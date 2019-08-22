# Generated by Django 2.2.4 on 2019-08-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_person',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_phone',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='state',
            field=models.TextField(max_length=100),
        ),
    ]
