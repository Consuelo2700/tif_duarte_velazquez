from django.contrib import admin
from django.urls import path, include
from .views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('categorias/', include('categorias.urls')),
    path('ventas/', include('ventas.urls')),
    path('clientes/', include('clientes.urls')),
    path('', inicio, name='inicio'),
]