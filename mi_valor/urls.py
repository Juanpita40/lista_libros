from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.inicio, name='index'),
    path('listbook/', views.listar_libros, name='listar_libros'),
    path('inputbook/', views.input_book, name='input_book'),
    path('register/', views.registro, name='registro'),
]


