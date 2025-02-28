from django.views import View
from api.models import Orden
from django.http import JsonResponse


class OrdenView(View):
    def get(self, request):
        orden = list(Orden.objects.values())
        if len(orden) > 0:
            datos = {'message': 'Ordenes encontradas', 'vigas': orden}
        else:
            datos = {'message': 'No se encontraron vigas'}
        return JsonResponse(datos)
