# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-13 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0009_realtransactionsource_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtransaction',
            name='purpose',
            field=models.CharField(max_length=1000),
        ),
    ]
