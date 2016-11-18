# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-18 15:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comercio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('disponibilidad', models.BooleanField()),
                ('imagen', models.ImageField(null=True, upload_to='img_bebidas')),
            ],
        ),
        migrations.CreateModel(
            name='Capacidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria_Bebida',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=150)),
                ('precio', models.FloatField()),
                ('descuento', models.FloatField(default=0.0)),
                ('disponibilidad', models.BooleanField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img_comidas')),
                ('categoria', models.ManyToManyField(to='producto.Categoria')),
                ('comercio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comercio.Comercio')),
            ],
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img_promociones')),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.FloatField()),
                ('fecha_caducidad', models.DateField(default=datetime.datetime.now)),
                ('comercio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comercio.Comercio')),
            ],
        ),
        migrations.AddField(
            model_name='bebida',
            name='capacidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Capacidad'),
        ),
        migrations.AddField(
            model_name='bebida',
            name='categoria',
            field=models.ManyToManyField(to='producto.Categoria_Bebida'),
        ),
    ]
