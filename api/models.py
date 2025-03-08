from django.utils import timezone
from django.db import models

class Orden(models.Model):
      numero_orden = models.CharField(max_length=10, unique=True)
      fecha = models.DateField(default=timezone.now)

      def __str__(self):
          return f"Orden {self.numero_orden} - {self.fecha}"

class Viga(models.Model):
      orden = models.ForeignKey(Orden, related_name="vigas", on_delete=models.CASCADE)
      nombre = models.CharField(max_length=50)
      cantidad = models.IntegerField()
      medidas = models.CharField(max_length=20)
      cada_una = models.CharField(max_length=10)
      tipo = models.CharField(max_length=5)

      def __str__(self):
          return f"{self.nombre} - {self.cantidad} unidades"
