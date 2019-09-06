# Generated by Django 2.2.4 on 2019-08-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0003_auto_20190812_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='new_experience',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='skills',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='PAN_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]