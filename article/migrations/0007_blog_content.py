# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 09:31
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20160312_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(default='', verbose_name='\u5185\u5bb9'),
        ),
    ]