from django.db import models
from apps.comercio.models import Comercio
import datetime


class Capacidad(models.Model):
    codigo = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion)


class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion)


class Categoria_Bebida(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion)


class Bebida(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    disponibilidad = models.BooleanField()
    imagen = models.ImageField(upload_to='img_bebidas', null=True)
    categoria = models.ManyToManyField(Categoria_Bebida)
    capacidad = models.ForeignKey(Capacidad, on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.nombre)


class Comida(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=150)
    precio = models.FloatField()
    descuento = models.FloatField(default=0.00)
    disponibilidad = models.BooleanField()
    imagen = models.ImageField(upload_to='img_comidas', null=True, blank=True)
    categoria = models.ManyToManyField(Categoria)
    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return '{}'.format(self.nombre)

class Promocion(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='img_promociones', null=True, blank=True)
    descripcion = models.TextField(max_length=200)
    precio = models.FloatField()
    fecha_caducidad = models.DateField(default=datetime.datetime.now)

    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE, null=True)