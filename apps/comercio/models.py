from django.db import models


class Departamento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)


class Localidad(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)


class Domicilio(models.Model):
    codigo = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    coordenadas = models.CharField(max_length=30)

    localidad = models.OneToOneField(Localidad)

    def __str__(self):
        return 'calle {} nro {}'.format(self.calle, self.numero)


class Comercio(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    rubro = models.CharField(max_length=20)
    horarios = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=150)
    disponibilidad = models.BooleanField()

    domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img_comercios')

    def __str__(self):
        return 'comercio: {}'.format(self.nombre)


class Telefono(models.Model):
    numero = models.CharField(primary_key=True, max_length=25)
    descripcion = models.TextField(max_length=30)
    disponibilidad = models.BooleanField()

    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.numero)


class Pago(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50)
    disponibilidad = models.BooleanField()

    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)
