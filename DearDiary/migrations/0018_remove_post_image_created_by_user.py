# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-19 04:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DearDiary', '0017_auto_20180419_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_image',
            name='created_by_user',
        ),
    ]
