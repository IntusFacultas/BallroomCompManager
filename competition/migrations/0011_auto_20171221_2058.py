# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0010_competition_heat_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='heat_list',
            field=models.CharField(blank=True, max_length=1000000, null=True, verbose_name='Heat List'),
        ),
    ]