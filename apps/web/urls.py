from django.conf.urls import url, include
#from apps.comercio.views import index
from .views import index, SearchView

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^search/', include("watson.urls", namespace="watson"))
    url(r'^search/', SearchView.as_view(), name="watson"),

]