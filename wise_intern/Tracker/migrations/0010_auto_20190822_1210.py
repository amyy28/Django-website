# Generated by Django 2.2.4 on 2019-08-22 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0009_auto_20190822_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
