from django.db import models

class Orden(models.Model):
      numero_orden = models.CharField(max_length=10)
      fecha = models.DateField()

      class Meta:
        unique_together = ('numero_orden', 'fecha')  # Restricción única

      def __str__(self):
        return f"Orden {self.numero_orden} - Fecha {self.fecha}"

class Viga(models.Model):
      orden = models.ForeignKey(Orden, related_name="vigas", on_delete=models.CASCADE)
      nombre = models.CharField(max_length=50)
      cantidad = models.IntegerField()
      medidas = models.CharField(max_length=20)
      cada_una = models.CharField(max_length=10)
      tipo = models.CharField(max_length=5)

      def __str__(self):
          return f"{self.nombre} - {self.cantidad} unidades"
