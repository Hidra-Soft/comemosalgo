from .forms import ComercioRegistroForm
from apps.comercio.models import Comercio, Domicilio, Telefono
from apps.producto.models import Promocion, Comida
from django_comments.models import Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.shortcuts import render
import datetime
#from django.core.urlresolvers import reverse_lazy

def index(request):
    comentarios = Comment.objects.order_by('submit_date')
    comercios = Comercio.objects.order_by('visitas')
    promociones = Promocion.objects.all()
    contexto = {'comentarios':comentarios, 'comercios':comercios, 'promociones':promociones}
    return render(request,'index.html', contexto)


class ListaComercio(ListView):
    model = Comercio
    #ACA EN EL QUERYSET HAY QUE HACER QUE FILTRE LAS PROMOCIONES QUE NO ESTAN VENCIDAS
    #hoy = datetime.datetime.now()
    #vencimiento = Promocion.fecha_caducidad
    #queryset = Promocion.objects.filter(date__range=[hoy, vencimiento])
    template_name = "comercio/lista.html"

class DetalleComercio(DetailView):
    model = Comercio
    #comidas = Comida.objects.filter(comercio = 3, disponibilidad=True)
    comidas = Comida.objects.all()
    queryset = Comercio.objects.filter(disponibilidad=True)
    template_name = "comercio/detail_comercio.html"

    def get_context_data(self, **kwargs):
        self.object.incrementar_visita()
        context = super().get_context_data(**kwargs)

        context['domicilios'] = Domicilio.objects.filter(comercio = self.object.pk)
        context['telefonos'] = Telefono.objects.filter(comercio = self.object.pk)
        return context

class Perfil(DetailView):
    model = Comercio
    #comidas = Comida.objects.filter(comercio = 3, disponibilidad=True)
    comidas = Comida.objects.all()
    queryset = Comercio.objects.filter(disponibilidad=True)
    template_name = "comercio/perfil.html"

    def get_context_data(self, **kwargs):
        self.object.incrementar_visita()
        context = super().get_context_data(**kwargs)

        context['domicilios'] = Domicilio.objects.filter(comercio = self.object.pk)
        context['telefonos'] = Telefono.objects.filter(comercio = self.object.pk)
        return context

class MiNegocio(DetailView):
    model = Comercio
    #comidas = Comida.objects.filter(comercio = 3, disponibilidad=True)
    comidas = Comida.objects.all()
    queryset = Comercio.objects.filter(disponibilidad=True)
    template_name = "comercio/minegocio.html"

    def get_context_data(self, **kwargs):
        self.object.incrementar_visita()
        context = super().get_context_data(**kwargs)

        context['domicilios'] = Domicilio.objects.filter(comercio = self.object.pk)
        context['telefonos'] = Telefono.objects.filter(comercio = self.object.pk)
        return context

class Productos(ListView):
    model = Comida
    template_name = "comercio/productos.html"

class FormularioRegistroComercio(FormView):
    form_class = ComercioRegistroForm
    template_name = 'comercio/formulario_registro_comercio.html'


