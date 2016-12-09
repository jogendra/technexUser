# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-09 12:17
from __future__ import unicode_literals

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0028_team_technexteamid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notificationId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', ckeditor.fields.RichTextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('photo', models.TextField(blank=True, validators=[django.core.validators.URLValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='ReaderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.Notification')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.TechProfile')),
            ],
        ),
    ]