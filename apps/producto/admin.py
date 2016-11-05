from django.contrib import admin
from apps.producto.models import Categoria, Categoria_Bebida, Capacidad, Comida, Bebida


class ComidaAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','descripcion','precio','disponibilidad', 'imagen')


class BebidaAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio', 'disponibilidad','capacidad', 'imagen')


class CapacidadAdmin(admin.ModelAdmin):
    list_display = ('codigo','descripcion')


#class LineaAdmin(admin.ModelAdmin):
#    list_display = ('id','descripcion')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion')


class Categoria_BebidaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion')


class Imagen_ComidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen','comida')


class Imagen_BebidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen', 'bebida')



admin.site.register(Comida, ComidaAdmin)
admin.site.register(Bebida, BebidaAdmin)
admin.site.register(Capacidad, CapacidadAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Categoria_Bebida, Categoria_BebidaAdmin)
