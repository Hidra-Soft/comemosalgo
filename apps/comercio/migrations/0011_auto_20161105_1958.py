# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-05 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0010_auto_20161105_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='comercio',
            name='delivery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comercio.Delivery'),
        ),
    ]
