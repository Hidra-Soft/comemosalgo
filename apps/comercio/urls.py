from django.conf.urls import url
from .views import index
from .views import ListaComercio, DetalleComercio, FormularioRegistroComercio, Perfil, MiNegocio, Productos

urlpatterns = [
    url(r'^$', index),
    url(r'^lista/$', ListaComercio.as_view(), name='lista'),
    url(r'^detalle/(?P<pk>\d+)/$', DetalleComercio.as_view(), name='detalle'),
    url(r'^perfil/(?P<pk>\d+)/$', Perfil.as_view(), name='perfil'),
    url(r'^minegocio/(?P<pk>\d+)/$', MiNegocio.as_view(), name='minegocio'),
    url(r'^minegocio/(?P<pk>\d+)/productos/$', Productos.as_view(), name='productos'),
    url(r'^registroComercio/$', FormularioRegistroComercio.as_view())
]