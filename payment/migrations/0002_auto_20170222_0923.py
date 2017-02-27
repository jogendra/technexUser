# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-22 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currenthostel',
            name='hostel',
        ),
        migrations.RemoveField(
            model_name='deskteam',
            name='user',
        ),
        migrations.RemoveField(
            model_name='idcard',
            name='facility',
        ),
        migrations.RemoveField(
            model_name='idcard',
            name='techProfile',
        ),
        migrations.RemoveField(
            model_name='offlineprofile',
            name='hostel',
        ),
        migrations.RemoveField(
            model_name='offlineprofile',
            name='techProfile',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='creditor',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='facility',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='reciever',
        ),
        migrations.DeleteModel(
            name='CurrentHostel',
        ),
        migrations.DeleteModel(
            name='DeskTeam',
        ),
        migrations.DeleteModel(
            name='Facility',
        ),
        migrations.DeleteModel(
            name='Hostel',
        ),
        migrations.DeleteModel(
            name='IdCard',
        ),
        migrations.DeleteModel(
            name='OffLineProfile',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
