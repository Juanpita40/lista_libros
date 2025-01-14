# mi_valor/views.py
from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm, BuscarLibroForm
from django.contrib.auth.models import Permission
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login as auth_login, logout as auth_logout


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
    
    # Crear una lista de diccionarios con los datos y el rating 
    libros_con_rating = [] 
    for libro in libros: 
        rating = libro.rating # Obtener el rating dinámico 
        libros_con_rating.append({ 
            'titulo': libro.titulo, 
            'autor': libro.autor, 
            'valoracion': libro.valoracion, 
            'rating': rating,
        })

    context = { 
        'libros_valoracion_alta': libros_valoracion_alta, 
        'libros': libros, 
        'form': form, } 
    return render(request, 'listbook.html', context)

def input_book(request): 
        if request.method == 'POST': 
            form = LibroForm(request.POST) 
            if form.is_valid(): 
                form.save() # Guardar los datos del formulario en la base de datos 
                return redirect('listar_libros') # Redirigir a la página de inicio o a otra página después de enviar el formulario 
        else: 
            form = LibroForm() # Crear un formulario vacío para solicitudes GET 
        return render(request, 'inputbook.html', {'form': form})

def registro(request): 
    if request.method == 'POST': 
        form = RegistroUsuarioForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            permiso_desarrollador = Permission.objects.get(codename='development') 
            user.user_permissions.add(permiso_desarrollador) 
            user.save()
            return redirect('index') # Redirigir a la página de inicio después de registrar al usuario 
    else: 
        form = RegistroUsuarioForm() 
    return render(request, 'register.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('input_book')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('index')
    return render(request, 'logout.html')

