from django.apps import AppConfig
from watson import search as watson


class ProductoConfig(AppConfig):
    name = 'apps.producto'

    def ready(self):
        comida = self.get_model("Comida")
        bebida = self.get_model("Bebida")
        watson.register(comida.objects.filter(disponibilidad=True),
                        fields=["nombre",
                                "categoria",
                                ],
                        )
        watson.register(bebida.objects.filter(disponibilidad=True),
                        field=["nombre",
                               "categoria",
                               ],
                        )
