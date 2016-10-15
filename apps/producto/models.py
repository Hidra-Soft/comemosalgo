from django.db import models


class Imagen_Bebida(models.Model):
    bebida = models.ForeignKey(Bebida)

class Imagen_Comida(models.Model):
    pass

class Linea(models.Model):
    descripcion_linea = models.CharField(max_length=15)


class Capacidad(models.Model):
    descripcion_capacidad = models.CharField(max_length=6)


class Bebida(models.Model):
    cod_bebida = models.IntegerField(primary_key=True, max_length=15)
    nombre_bebida = models.CharField(max_length=30)
    precio_bebida = models.FloatField()
    disponibilidad_bebida = models.BooleanField()

    capacidad = models.ForeignKey(Capacidad, on_delete=models.CASCADE)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)


class Categoria(models.Model):
    cod_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=15)


class Comida(models.Model):
    cod_comida = models.AutoField(primary_key=True)
    nombre_comida = models.CharField(max_length=20)
    descripcion_comida = models.CharField(max_length=50)
    precio_comida = models.FloatField()
    disponibilidad_comida = models.BooleanField()

    categoria = models.ManyToManyField(Categoria)
