from django.urls import path
from inicio import views

app_name = 'Inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prueba', views.prueba,  name='prueba'),
    path('segunda-vista/', views.segunda_vista, name='segunda_vista'),
    path('fecha-actual/', views.fecha_actual, name='fecha_actual'),
    path('saludar/', views.saludar, name='saludar'),
    path('bienvenudo/<str:nombre>/<str:apellido>', views.bienvenudo, name='bienvenudo'),
    # V1 Crear perro
    # path('crear-perro/<str:nombre>/<str:edad>', views.crear_perro, name='crear_perro'),
    # V2 Crear perro
    path('perro/', views.listar_perros, name='listar_perros'),
    path('perro/crear/', views.crear_perro, name='crear_perro'),
]
