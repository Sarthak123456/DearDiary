# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DearDiary', '0004_auto_20180106_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
