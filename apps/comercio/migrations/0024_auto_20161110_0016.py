# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0023_auto_20161109_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='latitud',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='longitud',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]