from django.shortcuts import render
from .models import Producto


def listar_productos(request):
    productos = Producto.objects.all()

    return render(
        request,
        'productos/listar.html',
        {'productos': productos}
    )

# Create your views here.
