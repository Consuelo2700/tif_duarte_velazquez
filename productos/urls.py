from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('nuevo/', views.crear_producto, name='crear_producto'),
    path('<int:id>/modificar/', views.modificar_producto, name='modificar_producto'),
    path('<int:id>/cambiar-estado/', views.cambiar_estado_producto, name='cambiar_estado_producto'),
]