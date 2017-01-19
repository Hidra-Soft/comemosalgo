from django.conf.urls import url

from apps.usuario.views import RegistroUsuario, perfilusuario

urlpatterns = [
    url(r'^registrar/$', RegistroUsuario.as_view(), name='registrar'),
    url(r'^perfil/$', perfilusuario, name='perfil'),
]
