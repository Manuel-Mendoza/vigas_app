
from django.views import View
from api.models import Produccion
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class FechaView(View):
    def get(self, request):
        fecha = list(Produccion.objects.values())
        if len(fecha) > 0:
            datos = {'message': 'Fecha encontradas', 'vigas': fecha}
        else:
            datos = {'message': 'No se encontraron vigas'}
        return JsonResponse(datos)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        # Placeholder for handling POST requests
        # You can add the logic to handle POST data here
        response_data = {'message': 'POST request received'}
        return JsonResponse(response_data)
