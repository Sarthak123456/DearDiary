# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-24 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DearDiary', '0008_auto_20180223_0822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='photos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to=b''),
        ),
    ]
