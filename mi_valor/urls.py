from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.inicio, name='index'),
    path('listbook/', views.listar_libros, name='listar_libros'), 
]


