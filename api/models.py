from django.db import models



# Create your models here.
class Produccion(models.Model):
<<<<<<< HEAD
<<<<<<< Updated upstream
<<<<<<< Updated upstream

    fecha = models.DateField()
=======
    fecha = models.DateField(auto_now_add=True)
>>>>>>> parent of 2aaf604 (Ya sirve Poner fecha por Json y Automaticamente)
    def __str__(self):
        return f"Fecha: {self.fecha.strftime('%m-%d-%Y')}"
=======
=======
>>>>>>> Stashed changes
    id = models.CharField(max_length=20, primary_key=True, editable=False)
    fecha = models.DateField(unique=True)

    def save(self, *args, **kwargs):

        # Si es un objeto nuevo o no tiene ID asignado
        if not self.id or self._state.adding:

            # Convierte la fecha a formato YYYYMMDD para el ID
            from datetime import datetime
            fecha_formateada = self.fecha.strftime('%Y%m%d')
            if isinstance(self.fecha, datetime):
                fecha_formateada = self.fecha.strftime('%Y%m%d')
            self.id = fecha_formateada

        super(Produccion, self).save(*args, **kwargs)

        def __str__(self):
          return f"Producción del {self.fecha}"
          print("Producción del", self.fecha)

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

class Orden(models.Model):
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE, related_name="ordenes")
    numero_orden = models.CharField(max_length=50)  # Changed from NumberField to CharField

    def __str__(self):
        return f"Orden {self.numero_orden} - {self.produccion.fecha.strftime('%m-%d-%Y')}"

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
