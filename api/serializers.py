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
        
    def update(self, instance, validated_data):
        # Actualizamos los campos de la orden
        instance.numero_orden = validated_data.get('numero_orden', instance.numero_orden)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.save()
        
        # Manejamos las vigas
        if 'vigas' in validated_data:
            # Eliminamos todas las vigas existentes
            instance.vigas.all().delete()
            
            # Creamos las nuevas vigas
            for viga_data in validated_data.get('vigas', []):
                Viga.objects.create(orden=instance, **viga_data)
                
        return instance
        
    def validate_vigas(self, value):
        # Validamos que haya al menos una viga
        if len(value) == 0:
            raise serializers.ValidationError("Debe incluir al menos una viga")
        return value