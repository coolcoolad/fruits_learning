# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20170321_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boughtsoldtransaction',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bs_transactions', to='stocks.Account'),
        ),
        migrations.AlterField(
            model_name='boughtsoldtransaction',
            name='bought_stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bs_transactions', to='stocks.Stock', verbose_name='\u4e70\u5165\u80a1\u7968'),
        ),
    ]