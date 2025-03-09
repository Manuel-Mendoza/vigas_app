from rest_framework import serializers
from .models import Orden, Viga

class VigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viga
        fields = ["nombre", "cantidad", "medidas",'cada_una','tipo']

class OrdenSerializer(serializers.ModelSerializer):
    vigas = VigaSerializer(many=True, read_only=True)

    class Meta:
        model = Orden
        fields = ["numero_orden", "fecha", "vigas"]

    # Eliminamos la validación que impide tener múltiples órdenes con el mismo número
    # def validate(self, data):
    #       # Verificar si la combinación de número de orden y fecha ya existe
    #       if Orden.objects.filter(numero_orden=data['numero_orden'], fecha=data['produccion_fecha']).exists():
    #           raise serializers.ValidationError("Esta orden ya tiene esta fecha registrada.")
    #       return data
