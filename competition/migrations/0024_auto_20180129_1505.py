# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-29 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0023_auto_20171228_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dances', to='competition.Event')),
                ('round_of_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dances', to='competition.Round')),
            ],
        ),
        migrations.RenameField(
            model_name='performance',
            old_name='round',
            new_name='round_of_performance',
        ),
        migrations.AddField(
            model_name='performance',
            name='dance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='competition.Dance'),
            preserve_default=False,
        ),
    ]