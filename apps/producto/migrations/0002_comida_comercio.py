# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-03 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0002_remove_pago_comercio'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comida',
            name='comercio',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='comercio.Comercio'),
        ),
    ]