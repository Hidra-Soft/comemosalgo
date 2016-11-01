from django.conf.urls import url
from apps.comercio.views import index
from apps.comercio.views import ListaComercio, DetalleComercio

urlpatterns = [
    url(r'^$', index),
    url(r'^lista$', ListaComercio.as_view(), name='lista'),
    url(r'^detalle/(?P<pk>\d+)/$', DetalleComercio.as_view(), name='detalle')
]