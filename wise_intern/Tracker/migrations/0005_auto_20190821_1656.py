# Generated by Django 2.2.4 on 2019-08-21 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0004_tracker_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Candidate.Candidate'),
        ),
    ]
