from django.contrib import admin
from apps.comercio.models import Comercio, Pago, Departamento, Localidad, Rubro


class ComercioAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','disponibilidad', 'imagen')


#class DomicilioAdmin(admin.ModelAdmin):
 #   list_display = ('codigo','calle','numero','coordenadas','localidad')


class PagoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','descripcion','disponibilidad')


#class TelefonoAdmin(admin.ModelAdmin):
#    list_display = ('numero','descripcion','comercio')


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre')


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre', 'departamento')

class RubroAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')


admin.site.register(Comercio, ComercioAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Rubro, RubroAdmin)

