from django.shortcuts import render
from django.http import HttpResponse
from .forms import Formulariolibro
from .models import  libros

# Create your views here.

def Index(request):
    tb=libros.objects.all()
    return render(request, "Index.html", {'tb':tb})

def Crear(request):

    obj = Formulariolibro(request.POST or None)

    #validar si viene informacion al formulario o viene vacio
    if obj.is_valid():
        obj.save()
        return HttpResponse('Guardado')

    return render(request, "Crear.html", {'formulario':obj} )

def Modificar(request):
    return HttpResponse('Modificar')


def Eliminar(request):
    return HttpResponse('Eliminar')

