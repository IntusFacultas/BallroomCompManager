# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitor', '0011_auto_20171207_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='dancer',
            name='judging_pin',
            field=models.IntegerField(default=1, verbose_name='Judging PIN'),
            preserve_default=False,
        ),
    ]
