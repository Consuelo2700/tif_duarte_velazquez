from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('categorias/', include('categorias.urls')),
    path('clientes/', include('clientes.urls')),
    path('ventas/', include('ventas.urls')),
    path('', inicio, name='inicio'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.BASE_DIR / 'productos' / 'static'
    )
