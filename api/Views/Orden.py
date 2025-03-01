from django.views import View
from api.models import Orden
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class OrdenView(View):

    @csrf_exempt
    def get(self, request):
        orden = list(Orden.objects.values())
        if len(orden) > 0:
            datos = {'Ordenes': orden}
        else:
            datos = {'message': 'No se encontraron ordenes'}
        return JsonResponse(datos)
