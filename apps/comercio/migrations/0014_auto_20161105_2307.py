# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-05 23:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0013_auto_20161105_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comercio',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='comercio',
            name='localidad',
        ),
        migrations.RemoveField(
            model_name='comercio',
            name='longitud',
        ),
        migrations.RemoveField(
            model_name='localidad',
            name='departamento',
        ),
        migrations.AlterField(
            model_name='comercio',
            name='domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comercio.Domicilio'),
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.AddField(
            model_name='domicilio',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Localidad'),
        ),
    ]