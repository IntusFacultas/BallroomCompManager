# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 14:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitor', '0003_auto_20171129_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancer',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dancer', to=settings.AUTH_USER_MODEL),
        ),
    ]