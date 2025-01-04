from django.shortcuts import render 
from .models import Libro 

def listar_libros(request): 
    libros = Libro.objects.all() 
    libros_valoracion_alta = libros.filter(valoracion__gt=1500) 
    context = {
        'libros_valoracion_alta': libros_valoracion_alta, 
        'libros': libros
        } 
    return render(request, 'listbook.html', context)
