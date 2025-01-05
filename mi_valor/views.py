# mi_valor/views.py
from django.shortcuts import render
from .models import Libro
from .forms import BuscarLibroForm

def inicio(request):
    return render(request, 'index.html')

def listar_libros(request):
    form = BuscarLibroForm(request.GET or None)
    query = request.GET.get('query')
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)
    else:
        libros = Libro.objects.all()
    libros_valoracion_alta = libros.filter(valoracion__gt=1500)
    context = {
        'libros_valoracion_alta': libros_valoracion_alta,
        'libros': libros,
        'form': form,
    }
    return render(request, 'listbook.html', context)
