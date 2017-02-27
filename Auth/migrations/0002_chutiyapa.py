# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-04 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chutiyapa',
            fields=[
                ('responseId', models.AutoField(primary_key=True, serialize=False)),
                ('fieldChutiyap', models.CharField(blank=True, max_length=2, null=True)),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.questions')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.quizResponses')),
            ],
        ),
    ]
