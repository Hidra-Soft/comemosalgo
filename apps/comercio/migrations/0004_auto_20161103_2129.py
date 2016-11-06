# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-03 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0003_comercio_comida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='domicilio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Domicilio'),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Localidad'),
        ),
    ]