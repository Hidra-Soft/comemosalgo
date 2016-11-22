from django.conf.urls import url
#from apps.comercio.views import index
from .views import index
from .views import ListaComercio, DetalleComercio, FormularioRegistroComercio

urlpatterns = [
    url(r'^$', index),
    url(r'^lista/$', ListaComercio.as_view(), name='lista'),
    url(r'^detalle/(?P<pk>\d+)/$', DetalleComercio.as_view(), name='detalle'),
    url(r'^registroComercio/$', FormularioRegistroComercio.as_view())
]