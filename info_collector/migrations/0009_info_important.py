# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_collector', '0008_auto_20170314_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
