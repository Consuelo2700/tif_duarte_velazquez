from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm


def listar_categorias(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        'categorias/listar.html',
        {'categorias': categorias}
    )


def crear_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('categorias:listar_categorias')
    else:
        formulario = CategoriaForm()

    return render(
        request,
        'categorias/crear.html',
        {'formulario': formulario}
    )


def modificar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        formulario = CategoriaForm(request.POST, instance=categoria)

        if formulario.is_valid():
            formulario.save()
            return redirect('categorias:listar_categorias')
    else:
        formulario = CategoriaForm(instance=categoria)

    return render(
        request,
        'categorias/modificar.html',
        {'formulario': formulario}
    )


def cambiar_estado_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.activa = not categoria.activa
        categoria.save()

    return redirect('categorias:listar_categorias')

# Create your views here.
