
from django import forms
from .models import Venta
from detalle_ventas.models import DetalleVenta
from productos.models import Producto


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente']


class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.filter(
            activa=True,
            categoria__activa=True
        )
