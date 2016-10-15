from django.contrib import admin
from apps.comercio.models import Comercio, Domicilio, Pago, Telefono, Departamento, Localidad

admin.site.register(Comercio)
admin.site.register(Domicilio)
admin.site.register(Pago)
admin.site.register(Telefono)
admin.site.register(Departamento)
admin.site.register(Localidad)
