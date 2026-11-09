from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.listar_categorias, name='listar_categorias'),
    path('nueva/', views.crear_categoria, name='crear_categoria'),
    path('<int:id>/modificar/', views.modificar_categoria, name='modificar_categoria'),
    path('<int:id>/cambiar-estado/', views.cambiar_estado_categoria, name='cambiar_estado_categoria'),
]