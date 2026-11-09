
from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.listar_ventas, name='listar_ventas'),
    path('nueva/', views.crear_venta, name='crear_venta'),
    path('<int:id>/detalle/', views.ver_detalle_venta, name='ver_detalle_venta'),
]
