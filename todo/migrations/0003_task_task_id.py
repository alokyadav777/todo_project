# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20181013_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_id',
            field=models.IntegerField(default=0),
        ),
    ]
