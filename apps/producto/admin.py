from django.contrib import admin
from apps.producto.models import Categoria, CategoriaBebida, Capacidad, Comida, Bebida, Promocion


class ComidaAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','descripcion','precio','descuento', 'disponibilidad', 'imagen')


class BebidaAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio', 'disponibilidad','capacidad', 'imagen')


class CapacidadAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion')


class CategoriaBebidaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion')


class Imagen_ComidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen','comida')


class Imagen_BebidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen', 'bebida')

class PromocionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'descripcion', 'precio', 'fecha_caducidad', 'comercio')



admin.site.register(Comida, ComidaAdmin)
admin.site.register(Bebida, BebidaAdmin)
admin.site.register(Capacidad, CapacidadAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(CategoriaBebida, CategoriaBebidaAdmin)
admin.site.register(Promocion, PromocionAdmin)
