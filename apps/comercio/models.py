from django.db import models

class Comercio(models.Model):
    cod_comercio = models.AutoField(primary_key= True)
    nombre_cadena = models.CharField(max_length=40)
    nombre_comercio = models.CharField(max_length=40)
    rubro = models.CharField(max_length=20)
    horarios = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return '-CADENA: {} -COMERCIO: {}'.format(self.nombre_cadena, self.nombre_comercio)


class Domicilio(models.Model):
    cod_domicilio = models.AutoField(primary_key= True)
    calle = models.CharField(max_length=50)
    nro_calle = models.IntegerField()
    cod_localidad = models.IntegerField()
    coordenadas = models.CharField(max_length=30)
    comercio = models.OneToOneField(Comercio, on_delete=models.CASCADE)

    def __str__(self):
        return '{} -CALLE: {} -NRO CALLE: {}'.format(self.comercio,self.calle, self.nro_calle)

class Pago(models.Model):
    cod_pago = models.AutoField(primary_key=True)
    comercio = models.ForeignKey(Comercio,  on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)


class Telefono(models.Model):
    nro_tel = models.CharField(primary_key= True, max_length=25)
    descripcion = models.CharField(max_length=30)
    comercio = models.ForeignKey(Comercio,  on_delete=models.CASCADE)