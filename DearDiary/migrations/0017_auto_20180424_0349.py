# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-24 03:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DearDiary', '0016_auto_20180422_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post_image',
            name='created_by_user',
        ),
        migrations.AddField(
            model_name='post_image',
            name='post',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='DearDiary.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
