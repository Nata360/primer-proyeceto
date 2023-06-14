from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio),
    path('segunda-vista/', views.segunda_vista),
    path('fecha-actual/', views.fecha_actual),
    path('saludar/', views.saludar),
    path('bienvenudo/<str:nombre>/<str:apellido>', views.bienvenudo),
    path('crear-perro/<str:nombre>/<str:edad>', views.crear_perro),
]
