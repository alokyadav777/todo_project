# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20181017_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='softdeletedtask',
            old_name='soft_title',
            new_name='soft_task_title',
        ),
    ]