# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(default='', max_length=256, verbose_name='\u6982\u8ff0'),
        ),
    ]
