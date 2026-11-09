
from decimal import Decimal

from django.shortcuts import render, redirect
from django.db import transaction
from django.forms import inlineformset_factory

from .models import Venta
from .forms import (
    VentaForm,
    DetalleVentaForm,
    BaseDetalleVentaFormSet
)

from detalle_ventas.models import DetalleVenta
from productos.models import Producto


# Formset para cargar los detalles de una venta

DetalleVentaFormSet = inlineformset_factory(
    Venta,
    DetalleVenta,
    form=DetalleVentaForm,
    formset=BaseDetalleVentaFormSet,
    fields=['producto', 'cantidad'],
    extra=5,
    min_num=1,
    validate_min=True,
    can_delete=False
)


# LISTAR VENTAS

def listar_ventas(request):

    ventas = Venta.objects.select_related(
        'cliente'
    ).prefetch_related(
        'detalleventa_set__producto'
    ).order_by('-fecha_venta')

    return render(
        request,
        'ventas/listar.html',
        {'ventas': ventas}
    )


# CREAR VENTA

def crear_venta(request):

    venta = Venta()

    if request.method == 'POST':

        formulario = VentaForm(request.POST)

        formulario_detalles = DetalleVentaFormSet(
            request.POST,
            instance=venta
        )

        if formulario.is_valid() and formulario_detalles.is_valid():

            with transaction.atomic():

                # Obtener los productos seleccionados

                ids_productos = [
                    form.cleaned_data['producto'].id
                    for form in formulario_detalles.forms
                    if form.cleaned_data.get('producto')
                ]

                # Bloquear los productos mientras se realiza
                # la comprobación y actualización del stock

                productos = Producto.objects.select_for_update().filter(
                    id__in=ids_productos
                )

                productos_dict = {
                    producto.id: producto
                    for producto in productos
                }

                # Comprobar que haya stock suficiente

                stock_valido = True

                for form in formulario_detalles.forms:

                    datos = form.cleaned_data

                    if not datos or not datos.get('producto'):
                        continue

                    producto = productos_dict.get(
                        datos['producto'].id
                    )

                    cantidad = datos['cantidad']

                    if producto is None:

                        form.add_error(
                            'producto',
                            'El producto ya no está disponible.'
                        )

                        stock_valido = False

                    elif cantidad > producto.stock:

                        form.add_error(
                            'cantidad',
                            f'Stock insuficiente. '
                            f'Disponibles: {producto.stock}.'
                        )

                        stock_valido = False

                if not stock_valido:

                    return render(
                        request,
                        'ventas/crear.html',
                        {
                            'formulario': formulario,
                            'formulario_detalles': formulario_detalles
                        }
                    )

                # Guardar la venta

                venta = formulario.save(commit=False)

                venta.total = Decimal('0.00')

                venta.save()

                total_venta = Decimal('0.00')

                # Guardar cada detalle y descontar el stock

                for form in formulario_detalles.forms:

                    datos = form.cleaned_data

                    if not datos or not datos.get('producto'):
                        continue

                    producto = productos_dict[
                        datos['producto'].id
                    ]

                    detalle = DetalleVenta(
                        venta=venta,
                        producto=producto,
                        cantidad=datos['cantidad'],
                        precio_unitario=producto.precio
                    )

                    detalle.save()

                    subtotal = (
                        detalle.precio_unitario * detalle.cantidad
                    )

                    total_venta += subtotal

                    producto.stock -= detalle.cantidad

                    producto.save(update_fields=['stock'])

                # Actualizar el total definitivo

                venta.total = total_venta

                venta.save(update_fields=['total'])

            return redirect('ventas:listar_ventas')

    else:

        formulario = VentaForm()

        formulario_detalles = DetalleVentaFormSet(
            instance=venta
        )

    return render(
        request,
        'ventas/crear.html',
        {
            'formulario': formulario,
            'formulario_detalles': formulario_detalles
        }
    )
