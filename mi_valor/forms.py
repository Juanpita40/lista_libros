# book/forms.py
from django import forms

class BuscarLibroForm(forms.Form): 
    query = forms.CharField(label='Buscar libro', max_length=100)
    
class IngresarLibroForm(forms.Form):
    titulo = forms.CharField(label='Titulo', max_length=150, required=True)
    autor = forms.CharField(label='Autor', max_length=150, required=True)
    valoracion = forms.IntegerField(label='Valoracion', min_value=0, max_value=10000, required=True)

