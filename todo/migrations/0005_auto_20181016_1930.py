# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-16 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subtask_of',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='duedate',
            field=models.DateField(default=b'2018-10-16'),
        ),
    ]