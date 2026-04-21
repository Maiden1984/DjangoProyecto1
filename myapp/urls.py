from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.saludo),
    path('prueba/', views.index, name='index'),
]