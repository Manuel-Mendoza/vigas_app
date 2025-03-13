from rest_framework import serializers
from .models import Orden, Viga


class VigaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viga
        fields = ['id', 'nombre', 'cantidad', 'medidas', 'cada_una', 'tipo', 'orden']
        read_only_fields = ['orden']  # Marca el campo orden como solo lectura


class OrdenSerializer(serializers.ModelSerializer):
    vigas = VigaSerializer(many=True)
    id = serializers.IntegerField(read_only=True)  # Aseguramos que el ID se incluya explícitamente

    class Meta:
        model = Orden
        fields = ['id', 'numero_orden', 'fecha', 'vigas']  # Incluimos el ID explícitamente

    def create(self, validated_data):
        vigas_data = validated_data.pop('vigas')
        orden = Orden.objects.create(**validated_data)

        for viga_data in vigas_data:
            # Creamos la viga y asignamos la orden automáticamente
            Viga.objects.create(orden=orden, **viga_data)

        return orden
        
    def validate_vigas(self, value):
        # Validamos que haya al menos una viga
        if len(value) == 0:
            raise serializers.ValidationError("Debe incluir al menos una viga")
        return value