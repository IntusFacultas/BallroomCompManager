# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-29 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0024_auto_20180129_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='dance',
            name='competition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dances', to='competition.Competition'),
            preserve_default=False,
        ),
    ]