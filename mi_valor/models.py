from django.db import models 

class Libro(models.Model): 
    titulo = models.CharField(max_length=150) 
    autor = models.CharField(max_length=150) 
    valoracion = models.IntegerField() 
    
    def __str__(self): 
        return self.titulo
    
    