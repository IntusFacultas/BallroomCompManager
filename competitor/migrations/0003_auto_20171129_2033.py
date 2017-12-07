# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitor', '0002_dancer_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='dancer',
            name='email',
            field=models.CharField(max_length=256, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='request',
            name='dancer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitor.Dancer'),
        ),
        migrations.AddField(
            model_name='request',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitor.Studio'),
        ),
    ]