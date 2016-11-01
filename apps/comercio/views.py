from apps.comercio.models import Comercio
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

def index(request):
    return render(request,'index.html')

class ListaComercio(ListView):
    model = Comercio
    template_name = "Lista.html"

class DetalleComercio(DetailView):
    model = Comercio
    template_name = "detail_comercio.html"


