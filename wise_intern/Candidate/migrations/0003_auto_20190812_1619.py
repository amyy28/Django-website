# Generated by Django 2.2.4 on 2019-08-12 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0002_candidate_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='current_CTC',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='expected_CTC',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='notice_period',
        ),
    ]
