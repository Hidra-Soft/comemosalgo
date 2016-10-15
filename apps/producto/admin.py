from django.contrib import admin
from apps.producto.models import Categoria, Capacidad, Comida, Bebida, Linea

admin.site.register(Comida)
admin.site.register(Bebida)
admin.site.register(Capacidad)
admin.site.register(Linea)
admin.site.register(Categoria)