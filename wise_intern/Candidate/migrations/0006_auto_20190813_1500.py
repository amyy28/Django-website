# Generated by Django 2.2.4 on 2019-08-13 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0005_candidate_current_designation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='company_applied',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='position_applied',
        ),
    ]
