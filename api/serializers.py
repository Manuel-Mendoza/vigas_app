from rest_framework import serializers
from .models import Orden, Viga

class VigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viga
        fields = ["nombre", "cantidad", "medidas"]

class OrdenSerializer(serializers.ModelSerializer):
    vigas = VigaSerializer(many=True, read_only=True)

    class Meta:
        model = Orden
        fields = ["numero", "fecha", "vigas"]
