from rest_framework import viewsets
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
        ordenes = self.queryset.filter(numero_orden=pk)
        if ordenes.exists():
            serializer = self.get_serializer(ordenes, many=True)
            return Response(serializer.data)
        return Response({'error': 'No se encontraron órdenes con ese número'}, status=404)