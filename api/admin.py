from django.contrib import admin
from .models import Orden, Viga

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ("id", "numero", "fecha")  # Usando los nombres correctos de los campos
    search_fields = ("numero",)  # Permite búsqueda por número de orden

@admin.register(Viga)
class VigaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "cantidad", "medidas", "orden")  # Ajusta según los campos de Viga
    search_fields = ("nombre", "orden__numero")  # Corregido para usar el nombre correcto del campo
