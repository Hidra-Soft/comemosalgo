# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0024_auto_20161110_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='latitud',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='longitud',
            field=models.CharField(max_length=10, null=True),
        ),
    ]