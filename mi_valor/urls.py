from django.urls import path 
from . import views 

urlpatterns = [
    path('listbook/', views.listar_libros, name='listar_libros'), 
]
