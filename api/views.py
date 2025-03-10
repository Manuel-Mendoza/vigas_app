from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Orden
from .serializers import OrdenSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def create(self, request, *args, **kwargs):
        produccion_fecha = request.data.get('fecha')
        if Orden.objects.filter(fecha=produccion_fecha).exists():
            return Response({'error': 'La fecha ya existe, por favor seleccione otra.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
  