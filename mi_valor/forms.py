# mi_valor/forms.py
from django import forms

class BuscarLibroForm(forms.Form):
    query = forms.CharField(label='Buscar libro', max_length=100)
