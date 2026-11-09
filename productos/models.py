from django.db import models
from django.utils import timezone


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=50, unique=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(
        'categorias.Categoria',
        on_delete=models.PROTECT
    )
    activa = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            fecha = timezone.localdate().strftime('%Y%m%d')
            prefijo = f'INT-{fecha}-'

            codigos = Producto.objects.filter(
                codigo__startswith=prefijo
            ).values_list('codigo', flat=True)

            numeros = [
                int(codigo.split('-')[-1])
                for codigo in codigos
            ]

            siguiente = max(numeros, default=0) + 1
            self.codigo = f'{prefijo}{siguiente:03d}'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    