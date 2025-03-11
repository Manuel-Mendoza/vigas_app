from rest_framework import serializers
from .models import Orden, Viga


class VigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viga
        fields = ["nombre", "cantidad", "medidas", "cada_una", "tipo"]


class OrdenSerializer(serializers.ModelSerializer):
    vigas = VigaSerializer(many=True)

    class Meta:
        model = Orden
        fields = ["numero_orden", "fecha", "vigas"]

    def create(self, validated_data):
        vigas_data = validated_data.pop('vigas')
        orden = Orden.objects.create(**validated_data)

        for viga_data in vigas_data:
            Viga.objects.create(orden=orden, **viga_data)

        return orden