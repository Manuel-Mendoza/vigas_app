from django.db import models

# Create your models here.
from django.db import models

class Produccion(models.Model):
    fecha = models.DateField()

    def __str__(self):
        return self.fecha.strftime("%Y-%m-%d")

class Orden(models.Model):
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE, related_name="ordenes")
    numero_orden = models.CharField(max_length=50)

    def __str__(self):
        return f"Orden {self.numero_orden} - {self.produccion.fecha.strftime('%Y-%m-%d')}"

class Viga(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name="vigas")
    nombre_viga = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    medidas = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_viga} ({self.cantidad} unidades)"
