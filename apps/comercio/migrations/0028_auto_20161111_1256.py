# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-11 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0027_auto_20161111_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='longitud',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
