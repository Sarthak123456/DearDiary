# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-19 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DearDiary', '0022_auto_20180419_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='post_image',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to=b''),
        ),
    ]
