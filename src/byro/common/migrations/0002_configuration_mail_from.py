# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("common", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="configuration",
            name="mail_from",
            field=models.EmailField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="e-mail sender address",
            ),
        )
    ]
