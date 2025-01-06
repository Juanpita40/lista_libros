# mi_valor/admin.py
from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'valoracion')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion') # Campos de solo lectura 
    search_fields = ('titulo', 'autor') 
    list_filter = ('valoracion', 'fecha_modificacion') # Filtro por valoración y fecha de modificación
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by('-fecha_creacion')
        return queryset
