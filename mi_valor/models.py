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
    
    @property 
    def rating(self): 
        if self.valoracion < 1000: 
            return 'Baja' 
        elif 1000 <= self.valoracion <= 2500: 
            return 'Media' 
        else: 
            return 'Alta'
  
    class Meta: 
        permissions = [ 
        ("development", "Permiso como Desarrollador"), 
        ("scrum_master", "Permiso como Scrum Master"), 
        ("product_owner", "Permiso como Product Owner"), 
        ]
        verbose_name = "Libro" 
        verbose_name_plural = "Libros"

