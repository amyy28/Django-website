# Generated by Django 2.2.4 on 2019-08-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0004_auto_20190812_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='current_designation',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]