from django.db import models


class Linea(models.Model):
    descripcion = models.TextField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion)


class Capacidad(models.Model):
    descripcion = models.TextField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion)


class Bebida(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    disponibilidad = models.BooleanField()

    capacidad = models.ForeignKey(Capacidad, on_delete=models.CASCADE)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)


class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion)


class Comida(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=150)
    precio = models.FloatField()
    disponibilidad = models.BooleanField()

    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return '{}'.format(self.nombre)


class Imagen_Bebida(models.Model):
    imagen = models.ImageField(upload_to='img_bebidas')
    bebida = models.OneToOneField(Bebida)

    def __str__(self):
        return '{}'.format(self.bebida)


class Imagen_Comida(models.Model):
    imagen = models.ImageField(upload_to='img_comidas')
    comida = models.OneToOneField(Comida)

    def __str__(self):
        return '{}'.format(self.comida)
