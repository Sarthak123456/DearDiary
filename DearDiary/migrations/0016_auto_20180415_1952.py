# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-15 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DearDiary', '0015_auto_20180415_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
