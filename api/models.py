from django.db import models
from django.utils import timezone

class Orden(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Orden {self.numero} - {self.fecha}"

class Viga(models.Model):
    orden = models.ForeignKey(Orden, related_name="vigas", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    medidas = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} unidades"
