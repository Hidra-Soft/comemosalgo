from django.contrib import admin
from apps.comercio.models import Comercio, Pago, Telefono, Departamento, Localidad


class ComercioAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','rubro','disponibilidad', 'imagen')


#class DomicilioAdmin(admin.ModelAdmin):
 #   list_display = ('codigo','calle','numero','coordenadas','localidad')


class PagoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','descripcion','disponibilidad')


class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('numero','descripcion','comercio')


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre')


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre', 'departamento')


admin.site.register(Comercio, ComercioAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Localidad, LocalidadAdmin)

