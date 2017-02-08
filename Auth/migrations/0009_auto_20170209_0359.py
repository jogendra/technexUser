# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-08 22:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0008_auto_20170209_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentevent',
            name='assosponimage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parentevent',
            name='assosponlink',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]