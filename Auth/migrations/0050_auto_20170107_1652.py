# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-07 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0049_auto_20170106_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentevent',
            name='sponimage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startupmails',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.StartUpFair'),
        ),
    ]