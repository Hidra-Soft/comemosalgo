from apps.comercio.models import Comercio
from apps.producto.models import Promocion
from django_comments.models import Comment
from django.views.generic import ListView, DetailView
from django.shortcuts import render
#from django.core.urlresolvers import reverse_lazy

def index(request):
    comentarios = Comment.objects.order_by('submit_date')
    comercios = Comercio.objects.order_by('visitas')
    promociones = Promocion.objects.all()
    contexto = {'comentarios':comentarios, 'comercios':comercios, 'promociones':promociones}
    return render(request,'index.html', contexto)


class ListaComercio(ListView):
    model = Comercio
    template_name = "Lista.html"


class DetalleComercio(DetailView):
    model = Comercio
    queryset = Comercio.objects.filter(disponibilidad=True)
    template_name = "detail_comercio.html"

    def get_context_data(self, **kwargs):
        self.object.incrementar_visita()
        return super().get_context_data(**kwargs)

