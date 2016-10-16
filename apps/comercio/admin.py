from django.contrib import admin
from apps.comercio.models import Comercio, Domicilio, Pago, Telefono, Departamento, Localidad


class ComercioAdmin(admin.ModelAdmin):
    list_display = ('cod_comercio','nombre_cadena','nombre_comercio','rubro','descripcion','disponibilidad','domicilio')


class DomicilioAdmin(admin.ModelAdmin):
    list_display = ('cod_domicilio','calle','nro_calle','coordenadas','localidad')


class PagoAdmin(admin.ModelAdmin):
    list_display = ('cod_pago','nombre_pago','descripcion','disponibilidad_pago')


class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('nro_tel','descripcion','disponibilidad_tel','comercio')


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('cod_depto','nom_depto')


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('cod_localidad','nom_localidad')


admin.site.register(Comercio, ComercioAdmin)
admin.site.register(Domicilio, DomicilioAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Telefono, TelefonoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Localidad, LocalidadAdmin)

