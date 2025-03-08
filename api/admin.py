from django.contrib import admin
from .models import Orden, Viga

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ("id", "numero_orden", "fecha")  # Usando los nombres correctos de los campos
    search_fields = ("numero_orden",)  # Permite búsqueda por número de orden

@admin.register(Viga)
class VigaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "cantidad", "medidas", "orden",'cada_una','tipo')
    search_fields = ("nombre", "orden__numero_orden")
