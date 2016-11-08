from django.db import models
import datetime



#class Departamento(models.Model):
#    codigo = models.IntegerField(primary_key=True)
#    nombre = models.CharField(max_length=50)
#
#
#    def __str__(self):
#        return '{}'.format(self.nombre)


class Localidad(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre =models.CharField(max_length=50)

    #departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)


class Domicilio(models.Model):
    codigo = models.AutoField(primary_key= True)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    localidad = models.ForeignKey(Localidad)

    def __str__(self):
        return 'calle {} nro {}'.format(self.calle, self.numero)


class Pago(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50)
    #disponibilidad = models.BooleanField()


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


class Telefono(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=15)


    def __str__(self):
        return '{}'.format(self.tipo, self.descripcion)


class Comercio(models.Model):
    codigo = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=40)
    rubro = models.ManyToManyField(Rubro)
    horarios = models.CharField(max_length=50)
    #telefono = models.CharField(max_length=50, null=True)
    telefono = models.ForeignKey(Telefono, null=True)
    descripcion = models.TextField(max_length=150)
    forma_pago = models.ManyToManyField(Pago)
    disponibilidad = models.BooleanField()
    #domicilio = models.CharField(max_length=150)
    domicilio = models.ForeignKey(Domicilio, null=True)
    latitud = models.CharField(max_length=10, null=True)
    longitud = models.CharField(max_length=10, null=True)
    localidad = models.ForeignKey(Localidad, null=True)
    imagen = models.ImageField(upload_to='img_comercios')
    delivery = models.OneToOneField(Delivery, null=True, blank=True)
    visitas = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.nombre)


