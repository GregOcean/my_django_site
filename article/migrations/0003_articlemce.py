# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_blog_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleMCE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
