from django.db import models 
from django.utils import timezone

class Libro(models.Model): 
    titulo = models.CharField(max_length=150) 
    autor = models.CharField(max_length=150) 
    valoracion = models.IntegerField() 
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.titulo
    
    class Meta: 
        permissions = [ 
        ("development", "Permiso como Desarrollador"), 
        ("scrum_master", "Permiso como Scrum Master"), 
        ("product_owner", "Permiso como Product Owner"), 
        ]
        verbose_name = "Libro" 
        verbose_name_plural = "Libros"

