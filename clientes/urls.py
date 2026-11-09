
from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('nuevo/', views.crear_cliente, name='crear_cliente'),
    path('<int:id>/modificar/', views.modificar_cliente, name='modificar_cliente'),
]
