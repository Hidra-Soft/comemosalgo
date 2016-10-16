from django.contrib import admin
from apps.producto.models import Categoria, Capacidad, Comida, Bebida, Linea, Imagen_Bebida, Imagen_Comida


class ComidaAdmin(admin.ModelAdmin):
    list_display = ('cod_comida','nombre_comida','descripcion_comida','precio_comida','disponibilidad_comida',)


class BebidaAdmin(admin.ModelAdmin):
    list_display = ('cod_bebida', 'nombre_bebida','precio_bebida', 'disponibilidad_bebida','capacidad','linea')


class CapacidadAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion_capacidad')


class LineaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion_linea')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('cod_categoria','descripcion_categoria')


class Imagen_ComidaAdmin(admin.ModelAdmin):
    list_display = ('id','img_comida','comida')


class Imagen_BebidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_bebida', 'bebida')



admin.site.register(Comida, ComidaAdmin)
admin.site.register(Bebida, BebidaAdmin)
admin.site.register(Capacidad, CapacidadAdmin)
admin.site.register(Linea, LineaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Imagen_Comida, Imagen_ComidaAdmin)
admin.site.register(Imagen_Bebida, Imagen_BebidaAdmin)