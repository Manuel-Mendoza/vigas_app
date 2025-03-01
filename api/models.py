from django.db import models



# Create your models here.
# --------------Data Fecha-------------------
class Produccion(models.Model):
    fecha = models.DateField(unique=True)
    def __str__(self):
        return f"Fecha: {self.fecha.strftime('%m-%d-%Y')}"


# --------------Data orden-------------------
class Orden(models.Model):
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE, related_name="ordenes")
    numero_orden = models.CharField(max_length=50)

    def __str__(self):
        return f"Orden {self.numero_orden} - {self.produccion.fecha.strftime('%m-%d-%Y')}"


# --------------Data Viga-------------------
class Viga(models.Model):
    opciones = [
        ('DF', 'DF'), ('YC', 'YC')
    ]
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name="vigas")
    nombre_viga = models.CharField(max_length=20)
    cantidad = models.PositiveIntegerField()
    medidas = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=2,
        choices=opciones,
        default='DF'
    )

    def __str__(self):
        return f"{self.orden} {self.nombre_viga} ({self.cantidad} unidades) {self.medidas} {self.tipo}"
