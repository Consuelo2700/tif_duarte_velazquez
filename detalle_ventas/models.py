from django.db import models

class DetalleVenta(models.Model):
    venta = models.ForeignKey('ventas.Venta', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2) #precio del producto al momento de la venta

    def __str__(self):
        return f"Detalle de Venta {self.id} - Producto: {self.producto.nombre}"
