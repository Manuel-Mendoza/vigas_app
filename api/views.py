from django.views import View
from django.http import JsonResponse
from .models import Viga,Produccion,Orden


# Create your views here.

class OrdenView(View):
    def get(self, request):
        orden = list(Orden.objects.values())
        if len(orden) > 0:
            datos = {'message': 'Ordenes encontradas', 'vigas': orden}
        else:
            datos = {'message': 'No se encontraron vigas'}
        return JsonResponse(datos)

class FechaView(View):
    def get(self, request):
        vigas = list(Produccion.objects.values())
        if len(vigas) > 0:
            datos = {'message': 'Fecha encontradas', 'vigas': vigas}
        else:
            datos = {'message': 'No se encontraron vigas'}
        return JsonResponse(datos)

class VigasView(View):
    def get(self, request):
        vigas = list(Viga.objects.values())
        if len(vigas) > 0:
            datos = {'message': 'Vigas encontradas', 'vigas': vigas}
        else:
            datos = {'message': 'No se encontraron vigas'}
        return JsonResponse(datos)
#_____________________________GET_________________________

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
