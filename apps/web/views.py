from django.shortcuts import render
from apps.comercio.models import Comercio, Domicilio, Telefono
from apps.producto.models import Promocion, Comida
from django_comments.models import Comment
from django.views.generic import TemplateView
from watson import search as watson
from django.db.models import Q

def index(request):
    comentarios = Comment.objects.order_by('submit_date')
    comercios = Comercio.objects.order_by('visitas')
    promociones = Promocion.objects.all()
    domicilios = Domicilio.objects.all()
    contexto = {'comentarios': comentarios, 'comercios': comercios, 'promociones': promociones, 'domicilios': domicilios}

    return render(request, 'web/index.html', contexto)


class SearchView(TemplateView):
    template_name = "web/search_result.html"

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        q_comida = request.GET.get("q1", "")
        q_comercio = request.GET.get("q2", "")
        q_domicilio = request.GET.get("q3", "")
        # q_ubicacion = request.GET.get("q4", "")

        results = []
        if q_comercio and q_domicilio:
            resultes = watson.filter(Domicilio, q_domicilio).filter(comercio__nombre=q_comercio)

            for re in resultes:
                results.append(re.comercio)
            context['search'] = "Comercio: " + q_comercio + " + Domicilio: " + q_domicilio
            context['search_results'] = results
            return self.render_to_response(context)

        elif q_comercio:
            context['search'] = "Comercio: " + q_comercio
            context['search_results'] = watson.filter(Comercio, q_comercio)
            return self.render_to_response(context)

        elif q_comida:
            resultes = watson.filter(Comida, q_comida)

            for re in resultes:
                results.append(re.comercio)
            context['search'] = "Comida: " + q_comida
            context['search_results'] = results
            return self.render_to_response(context)

        else:

            resultes = watson.filter(Domicilio, q_domicilio)

            for re in resultes:
                results.append(re.comercio)

            context['search'] = "Domicilio: " + q_domicilio
            context['search_results'] = results
            return self.render_to_response(context)


