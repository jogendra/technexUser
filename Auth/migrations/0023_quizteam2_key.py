# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-04 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0022_auto_20170203_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizteam2',
            name='key',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
