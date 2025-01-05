# mi_valor/views.py
from django.shortcuts import render, redirect
from .models import Libro
from .forms import IngresarLibroForm, BuscarLibroForm

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
        'form': form, } 
    return render(request, 'listbook.html', context)

def input_book(request): 
    if request.method == 'POST': 
        form = IngresarLibroForm(request.POST) 
        if form.is_valid(): 
            # Aquí puedes manejar los datos del formulario, como guardarlos en la base de datos 
            return redirect('index') # Redirigir a la página de inicio o a otra página después de enviar el formulario 
    else: 
        form = IngresarLibroForm() 
        
    return render(request, 'inputbook.html', {'form': form})