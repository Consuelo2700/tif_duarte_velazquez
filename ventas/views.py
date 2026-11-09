
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.forms import formset_factory
from django.contrib import messages

from .models import Venta
from .forms import VentaForm, DetalleVentaForm
from detalle_ventas.models import DetalleVenta


def listar_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha_venta')

    return render(
        request,
        'ventas/listar.html',
        {'ventas': ventas}
    )


def crear_venta(request):
    DetalleFormSet = formset_factory(
        DetalleVentaForm,
        extra=1,
        min_num=1,
        validate_min=True
    )

    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        detalle_formset = DetalleFormSet(request.POST)

        if formulario.is_valid() and detalle_formset.is_valid():

            detalles_validos = [
                detalle for detalle in detalle_formset.cleaned_data
                if detalle.get('producto') and detalle.get('cantidad') is not None
            ]

            # Sumar las cantidades de cada producto
            cantidades_por_producto = {}

            for detalle in detalles_validos:
                producto = detalle['producto']
                cantidad = detalle['cantidad']

                if cantidad <= 0:
                    formulario.add_error(
                        None,
                        f'La cantidad de {producto.nombre} debe ser mayor que cero.'
                    )
                    return render(
                        request,
                        'ventas/crear.html',
                        {
                            'formulario': formulario,
                            'detalle_formset': detalle_formset
                        }
                    )

                cantidades_por_producto[producto.id] = (
                    cantidades_por_producto.get(producto.id, 0) + cantidad
                )

            with transaction.atomic():

                # Comprobar el stock total de cada producto
                for producto_id, cantidad_total in cantidades_por_producto.items():
                    producto = next(
                        detalle['producto']
                        for detalle in detalles_validos
                        if detalle['producto'].id == producto_id
                    )

                    if cantidad_total > producto.stock:
                        formulario.add_error(
                            None,
                            f'Stock insuficiente para {producto.nombre}. '
                            f'Stock disponible: {producto.stock}. '
                            f'Cantidad solicitada: {cantidad_total}.'
                        )
                        return render(
                            request,
                            'ventas/crear.html',
                            {
                                'formulario': formulario,
                                'detalle_formset': detalle_formset
                            }
                        )

                # Registrar la venta
                venta = formulario.save(commit=False)
                venta.total = 0
                venta.save()

                total = 0

                # Registrar los detalles de la venta
                for detalle in detalles_validos:
                    producto = detalle['producto']
                    cantidad = detalle['cantidad']
                    precio = producto.precio

                    DetalleVenta.objects.create(
                        venta=venta,
                        producto=producto,
                        cantidad=cantidad,
                        precio_unitario=precio
                    )

                    total += precio * cantidad

                # Descontar el stock una sola vez por producto
                productos_procesados = set()

                for detalle in detalles_validos:
                    producto = detalle['producto']

                    if producto.id not in productos_procesados:
                        cantidad_total = cantidades_por_producto[producto.id]
                        producto.stock -= cantidad_total
                        producto.save()

                        productos_procesados.add(producto.id)

                # Actualizar el total de la venta
                venta.total = total
                venta.save()

            messages.success(request, 'Venta registrada correctamente.')
            return redirect('ventas:listar_ventas')

    else:
        formulario = VentaForm()
        detalle_formset = DetalleFormSet()

    return render(
        request,
        'ventas/crear.html',
        {
            'formulario': formulario,
            'detalle_formset': detalle_formset
        }
    )


def ver_detalle_venta(request, id):
    venta = get_object_or_404(Venta, id=id)

    detalles = DetalleVenta.objects.filter(
        venta=venta
    ).select_related('producto')

    for detalle in detalles:
        detalle.subtotal = detalle.cantidad * detalle.precio_unitario

    return render(
        request,
        'ventas/detalle.html',
        {
            'venta': venta,
            'detalles': detalles
        }
    )

