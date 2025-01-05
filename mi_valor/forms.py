# book/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Libro


class BuscarLibroForm(forms.Form): 
    query = forms.CharField(label='Buscar libro', max_length=100)

class LibroForm(forms.ModelForm): 
    class Meta: 
        model = Libro 
        fields = ['titulo', 'autor', 'valoracion']
        widgets = { 
            'valoracion': forms.NumberInput(attrs={'min': 0, 'max': 10000}), 
        }
        help_texts = { 'valoracion': 'Valor entre 0 y 10000', 
        }

class RegistroUsuarioForm(UserCreationForm): 
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'})) 
    
    class Meta: 
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] 
        widgets = { 
            'username': forms.TextInput(attrs={'class': 'form-control'}), 
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}), 
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}), 
        }