from django.conf.urls import url, include
from .views import index, SearchView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^search/', SearchView.as_view(), name="search"),

]