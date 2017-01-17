from django.conf.urls import url

from apps.usuario.views import RegistroUsuario, PerfilUsuario

urlpatterns = [
    url(r'^registrar/$', RegistroUsuario.as_view(), name='registrar'),
    url(r'^perfil/$', PerfilUsuario, name='perfil'),
]