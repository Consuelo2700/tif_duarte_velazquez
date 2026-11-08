from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm


def listar_clientes(request):
    clientes = Cliente.objects.all()

    return render(
        request,
        'clientes/listar.html',
        {'clientes': clientes}
    )


def crear_cliente(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('clientes:listar_clientes')
    else:
        formulario = ClienteForm()

    return render(
        request,
        'clientes/crear.html',
        {'formulario': formulario}
    )


def modificar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        formulario = ClienteForm(request.POST, instance=cliente)

        if formulario.is_valid():
            formulario.save()
            return redirect('clientes:listar_clientes')
    else:
        formulario = ClienteForm(instance=cliente)

    return render(
        request,
        'clientes/modificar.html',
        {'formulario': formulario}
    )

# Create your views here.
