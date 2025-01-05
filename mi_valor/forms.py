# book/forms.py
from django import forms
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