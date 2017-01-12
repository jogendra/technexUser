# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-12 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0070_auto_20170112_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentstatus',
            name='status',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='startupmails',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.StartUpFair'),
        ),
    ]
