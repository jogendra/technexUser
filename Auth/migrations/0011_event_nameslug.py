# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-29 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0010_workshopteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='nameSlug',
            field=models.SlugField(null=True),
        ),
    ]
