from django.shortcuts import render
from apps.comercio.models import Comercio, Domicilio, Telefono
from apps.producto.models import Promocion, Comida
from django_comments.models import Comment

def index(request):
    comentarios = Comment.objects.order_by('submit_date')
    comercios = Comercio.objects.order_by('visitas')
    promociones = Promocion.objects.all()
    contexto = {'comentarios':comentarios, 'comercios':comercios, 'promociones':promociones}
    return render(request,'web/index.html', contexto)

