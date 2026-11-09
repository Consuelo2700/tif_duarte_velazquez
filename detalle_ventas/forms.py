
from django import forms
from django.forms.models import BaseInlineFormSet

from .models import DetalleVenta
from productos.models import Producto


class DetalleVentaForm(forms.ModelForm):

    class Meta:
        model = DetalleVenta
        fields = [
            'producto',
            'cantidad',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['producto'].queryset = Producto.objects.filter(
            activa=True
        ).order_by('nombre')


class BaseDetalleVentaFormSet(BaseInlineFormSet):

    def clean(self):

        super().clean()

        if any(self.errors):
            return

        productos = set()
        hay_detalles = False

        for formulario in self.forms:

            datos = formulario.cleaned_data

            if not datos:
                continue

            producto = datos.get('producto')
            cantidad = datos.get('cantidad')

            if not producto:
                continue

            hay_detalles = True

            if producto.id in productos:
                raise forms.ValidationError(
                    'No podés agregar el mismo producto dos veces. '
                    'Modificá la cantidad del detalle existente.'
                )

            productos.add(producto.id)

            if cantidad is not None and cantidad <= 0:
                raise forms.ValidationError(
                    'La cantidad debe ser mayor que cero.'
                )

        if not hay_detalles:
            raise forms.ValidationError(
                'Debés agregar al menos un producto a la venta.'
            )
