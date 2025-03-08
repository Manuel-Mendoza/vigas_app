from rest_framework import viewsets
from rest_framework import status
from .models import Orden
from .serializers import OrdenSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

def create(self, request, *args, **kwargs):
        fecha = request.data.get('produccion_fecha')
        if Orden.objects.filter(produccion_fecha=fecha).exists():
            return Response({'error': 'La fecha ya existe, por favor seleccione otra.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
