from django.apps import AppConfig
from watson import search as watson

class ProductoConfig(AppConfig):
    name = 'apps.producto'

    def ready(self):
        Comida = self.get_model("Comida")
        Bebida = self.get_model("Bebida")
        watson.register(Comida.objects.filter(disponibilidad=True),
                        fields=["nombre",
                                "categoria",
                                ],
                        )
        watson.register(Bebida.objects.filter(disponibilidad=True),
                        field=["nombre",
                               "categoria",
                               ],
                        )
