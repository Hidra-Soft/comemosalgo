from apps.comercio.models import Comercio
from django_comments.models import Comment
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

def index(request):
    comentarios = Comment.objects.all()
    contexto = {'comentarios':comentarios}
    return render(request,'index.html', contexto)


class ListaComercio(ListView):
    model = Comercio
    template_name = "Lista.html"

class DetalleComercio(DetailView):
    model = Comercio
    template_name = "detail_comercio.html"


