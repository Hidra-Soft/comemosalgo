from django.conf.urls import url
#from apps.comercio.views import index
from .views import index

urlpatterns = [
    url(r'^$', index),
]