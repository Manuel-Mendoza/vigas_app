from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from .models import Orden
from .serializers import OrdenSerializer, LoginSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_api(request):
    serializer = LoginSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            # Devolver un mensaje de error más detallado
            error_message = str(e)
            if hasattr(e, 'detail'):
                error_message = str(e.detail)
            return Response(
                {'error': error_message},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            # Devolver un mensaje de error más detallado
            error_message = str(e)
            if hasattr(e, 'detail'):
                error_message = str(e.detail)
            return Response(
                {'error': error_message},
                status=status.HTTP_400_BAD_REQUEST
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