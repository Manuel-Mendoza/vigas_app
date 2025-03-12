from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Orden
from .serializers import OrdenSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=400
            )

    def retrieve(self, request, pk=None):
        # Intentar primero buscar por ID
        try:
            orden_id = int(pk)
            orden = self.queryset.filter(id=orden_id).first()
            if orden:
                serializer = self.get_serializer(orden)
                return Response(serializer.data)
        except ValueError:
            # Si no es un número entero, buscar por número de orden
            pass
        
        # Buscar por número de orden
        ordenes = self.queryset.filter(numero_orden=pk)
        if ordenes.exists():
            serializer = self.get_serializer(ordenes, many=True)
            return Response(serializer.data)
        
        return Response({'error': 'No se encontraron órdenes con ese número o ID'}, status=404)
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)