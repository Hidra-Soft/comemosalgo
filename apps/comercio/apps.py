from django.apps import AppConfig
from watson import search as watson

class ComercioConfig(AppConfig):
    name = 'apps.comercio'

    def ready(self):
        Comercio = self.get_model("Comercio")
        Domicilio = self.get_model("Domicilio")
        watson.register(Comercio.objects.filter(disponibilidad=True),
                        fields=["nombre",
                                "rubro",
                                ],
                        )
        watson.register(Domicilio)
