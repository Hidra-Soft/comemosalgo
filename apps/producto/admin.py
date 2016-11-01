from django.contrib import admin
from apps.producto.models import Categoria, Capacidad, Comida, Bebida, Linea, Imagen_Bebida, Imagen_Comida


class ComidaAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','descripcion','precio','disponibilidad',)


class BebidaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre','precio', 'disponibilidad','capacidad','linea')


class CapacidadAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')


class LineaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('codigo','descripcion')


class Imagen_ComidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen','comida')


class Imagen_BebidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagen', 'bebida')



admin.site.register(Comida, ComidaAdmin)
admin.site.register(Bebida, BebidaAdmin)
admin.site.register(Capacidad, CapacidadAdmin)
admin.site.register(Linea, LineaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Imagen_Comida, Imagen_ComidaAdmin)
admin.site.register(Imagen_Bebida, Imagen_BebidaAdmin)