from django.contrib import admin
from apps.comercio.models import Comercio, Pago, Localidad, Rubro, Delivery, Telefono, Domicilio, Horario


class ComercioAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','disponibilidad', 'imagen')


#class DomicilioAdmin(admin.ModelAdmin):
 #   list_display = ('codigo','calle','numero','coordenadas','localidad')


class PagoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','descripcion')


#class TelefonoAdmin(admin.ModelAdmin):
#    list_display = ('numero','descripcion','comercio')


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre')


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre')


class RubroAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')


class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'descripcion')


class DomicilioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'calle', 'numero', 'latitud', 'longitud', 'localidad')


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'apertura', 'cierre')



admin.site.register(Comercio, ComercioAdmin)
admin.site.register(Pago, PagoAdmin)
#admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Rubro, RubroAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Telefono, TelefonoAdmin)
admin.site.register(Domicilio, DomicilioAdmin)
admin.site.register(Horario, HorarioAdmin)