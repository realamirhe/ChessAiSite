# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-02-11 21:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChessAiSite_app', '0009_auto_20170211_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activationcode',
            field=models.CharField(default='nothing', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 11, 21, 10, 21, 800974), max_length='50'),
        ),
    ]
