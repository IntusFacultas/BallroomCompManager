# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0020_auto_20171225_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='status',
            field=models.CharField(blank=True, max_length=1000000, null=True, verbose_name='Heat List'),
        ),
    ]