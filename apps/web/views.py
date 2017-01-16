from django.shortcuts import render
from apps.comercio.models import Comercio, Domicilio, Telefono
from apps.producto.models import Promocion, Comida
from django_comments.models import Comment
from django.views.generic import TemplateView
from watson import search as watson

def index(request):
    comentarios = Comment.objects.order_by('submit_date')
    comercios = Comercio.objects.order_by('visitas')
    promociones = Promocion.objects.all()
    contexto = {'comentarios': comentarios, 'comercios': comercios, 'promociones': promociones}

    return render(request, 'web/index.html', contexto)

class SearchView(TemplateView):
    template_name = "web/search_result.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView,self).get_context_data(**kwargs)
        query = self.request.GET.get("q1", "")
        query2 = self.request.GET.get("q2", "")
        result = watson.search(query)

        for i in result:
            print(i.object)

        return context


