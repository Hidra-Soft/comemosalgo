from django.contrib import admin
from apps.comercio.models import Comercio, Domicilio, Pago, Telefono, Departamento, Localidad


class ComercioAdmin(admin.ModelAdmin):
    list_display = ('cod_comercio','nombre_cadena','nombre_comercio','rubro','descripcion','disponibilidad','domicilio')


class DomicilioAdmin():
    list_display = ()

class PagoAdmin():
    list_display = ()

class TelefonoAdmin():
    list_display = ()

class DepartamentoAdmin():
    list_display = ()


admin.site.register(Comercio, ComercioAdmin)
admin.site.register(Domicilio, DomicilioAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Telefono, TelefonoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Localidad, LocalidadAdmin)

