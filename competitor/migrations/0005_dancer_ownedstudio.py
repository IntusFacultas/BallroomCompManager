# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitor', '0004_auto_20171130_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='dancer',
            name='ownedStudio',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='competitor.Studio'),
        ),
    ]