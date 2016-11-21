from django.db import models
import datetime



class Pago(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50)


    def __str__(self):
        return '{}'.format(self.nombre, self.descripcion)


class Rubro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=50)


    def __str__(self):
        return '{}'.format(self.nombre)


class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return '{}'.format(self.descripcion)


class Horario(models.Model):
    descripcion = models.CharField(max_length=100)
    apertura = models.TimeField()
    cierre = models.TimeField()

    def __str__(self):
        return '{}'.format(self.descripcion, self.apertura, self.cierre)


class Comercio(models.Model):
    codigo = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=40)
    rubro = models.ManyToManyField(Rubro)
    horarios = models.ForeignKey(Horario)
    descripcion = models.TextField(max_length=150)
    forma_pago = models.ManyToManyField(Pago)
    disponibilidad = models.BooleanField()
    imagen = models.ImageField(upload_to='img_comercios', blank=True)
    delivery = models.ForeignKey(Delivery, null=True, blank=True)
    visitas = models.IntegerField(default=0)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}'.format(self.nombre)

    def incrementar_visita(self):
        self.visitas += 1
        self.save()

class Telefono(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30)
    numero = models.CharField(max_length=15)
    comercio = models.ForeignKey(Comercio, null=True)

    def __str__(self):
        return '{}'.format(self.tipo, self.numero)

class Localidad(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre =models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)


class Domicilio(models.Model):
    codigo = models.AutoField(primary_key= True)
    comercio = models.ForeignKey(Comercio, null=True)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    latitud = models.CharField(max_length=11)
    longitud = models.CharField(max_length=11)
    localidad = models.ForeignKey(Localidad)

    def __str__(self):
        return 'calle {} nro {}'.format(self.calle, self.numero)