# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-14 06:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logging',
            name='deployment_pack',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='logging',
            name='operation',
            field=models.CharField(default=datetime.datetime(2016, 9, 14, 6, 54, 46, 484950, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
