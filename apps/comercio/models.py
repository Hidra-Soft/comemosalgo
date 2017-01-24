from django.db import models
from geoposition.fields import GeopositionField

TELEFONO_CHOICE = (
	('Movil', 'Movil'),
	('Fijo', 'Fijo'),
)

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


class Comercio(models.Model):
    codigo = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=40)
    rubro = models.ManyToManyField(Rubro)
    descripcion = models.TextField(max_length=500)
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

class Horario(models.Model):
    comercio = models.ForeignKey(Comercio)
    descripcion = models.CharField(max_length=100)
    apertura = models.TimeField()
    cierre = models.TimeField()

    def __str__(self):
        return '{}'.format(self.descripcion, self.apertura, self.cierre)

class Telefono(models.Model):
    id = models.AutoField(primary_key=True)
    comercio = models.ForeignKey(Comercio, null=True)
    tipo = models.CharField(choices=TELEFONO_CHOICE,
                            max_length=10,
                            default=TELEFONO_CHOICE[0][0])
    numero = models.CharField(max_length=15)

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
    localidad = models.ForeignKey(Localidad)
    position = GeopositionField()

    def __str__(self):
        return 'calle {} nro {}'.format(self.calle, self.numero)