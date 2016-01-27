# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 09:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='post_time',
        ),
        migrations.AddField(
            model_name='job',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 26, 9, 31, 55, 83039, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 26, 9, 32, 5, 3968, tzinfo=utc)),
            preserve_default=False,
        ),
    ]