from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


def listar_productos(request):
    productos = Producto.objects.all()
    return render(
        request,
        'productos/listar.html',
        {'productos': productos}
    )


def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('productos:listar_productos')
    else:
        formulario = ProductoForm()

    return render(
        request,
        'productos/crear.html',
        {'formulario': formulario}
    )
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)

        if formulario.is_valid():
            formulario.save()
            return redirect('productos:listar_productos')
    else:
        formulario = ProductoForm(instance=producto)

    return render(
        request,
        'productos/modificar.html',
        {'formulario': formulario}
    )
def cambiar_estado_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.activa = not producto.activa
        producto.save()

    return redirect('productos:listar_productos')
# Create your views here.
