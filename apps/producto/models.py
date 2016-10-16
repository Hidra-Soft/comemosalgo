from django.db import models




class Linea(models.Model):
    descripcion_linea = models.TextField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion_linea)


class Capacidad(models.Model):
    descripcion_capacidad = models.TextField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion_capacidad)


class Bebida(models.Model):
    cod_bebida = models.IntegerField(primary_key=True)
    nombre_bebida = models.CharField(max_length=30)
    precio_bebida = models.FloatField()
    disponibilidad_bebida = models.BooleanField()

    capacidad = models.ForeignKey(Capacidad, on_delete=models.CASCADE)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_bebida)


class Categoria(models.Model):
    cod_categoria = models.AutoField(primary_key=True)
    descripcion_categoria = models.TextField(max_length=30)

    def __str__(self):
        return '{}'.format(self.descripcion_categoria)


class Comida(models.Model):
    cod_comida = models.AutoField(primary_key=True)
    nombre_comida = models.CharField(max_length=20)
    descripcion_comida = models.TextField(max_length=150)
    precio_comida = models.FloatField()
    disponibilidad_comida = models.BooleanField()

    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return '{}'.format(self.nombre_comida)

class Imagen_Bebida(models.Model):
    img_bebida = models.ImageField(upload_to='img_bebidas')
    bebida = models.OneToOneField(Bebida)

    def __str__(self):
        return '{}'.format(self.bebida)

class Imagen_Comida(models.Model):
    img_comida = models.ImageField(upload_to='img_comidas')
    comida = models.OneToOneField(Comida)

    def __str__(self):
        return '{}'.format(self.comida)