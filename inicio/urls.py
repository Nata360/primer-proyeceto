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
    # Vistas comunes
    
    # V1 Crear perro
    # path('crear-perro/<str:nombre>/<str:edad>', views.crear_perro, name='crear_perro'),
    # V2 Crear perro
    # path('perro/', views.listar_perros, name='listar_perros'),
    # path('perro/crear/', views.crear_perro, name='crear_perro'),
    # path('perro/eliminar/<int:perro_id>/', views.eliminar_perro, name='eliminar_perro'), #la info que se otorga en url, la vista lo recibe como parámetro
    # path('perro/modificar/<int:perro_id>/', views.modificar_perro, name='modificar_perro'),
     
    # CBV
    path('perro/', views.ListarPerros.as_view(), name='listar_perros'),
    path('perro/crear/', views.CrearPerro.as_view(), name='crear_perro'),
    path('perro/eliminar/<int:pk>/', views.EliminarPerro.as_view(), name='eliminar_perro'),
    path('perro/modificar/<int:pk>/', views.ModificarPerro.as_view(), name='modificar_perro'),
    path('perro/<int:pk>/', views.MostrarPerro.as_view(), name='mostrar_perro'),
]
