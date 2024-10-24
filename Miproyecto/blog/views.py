from django.shortcuts import render
from .models import Articulo

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')#Renderiza la plantilla index.html

def articulos_list(request):
    articulos = Articulo.objects.all()     #Llama al metodo objects.all de Articulo, para retornar todos los articulos
    return render(request, 'blog/articulo_list.html', {'articulos': articulos}) #renderiza