
import json
from django.views import View
from api.models import Produccion
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime

class FechaView(View):
    def get(self, request):
        fecha = list(Produccion.objects.values())
        if len(fecha) > 0:
            datos = {'message': 'Fecha encontradas', 'vigas': fecha}
        else:
            datos = {'message': 'No se encontraron vigas'}
        return JsonResponse(datos)


#-------------------Dispatch-----------------
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

        #Eliminar para se vaya a subir a la web
#-------------------------------------------------


    def post(self, request):
        # Se revisa si hay body, si no, simplemente continuamos
        if request.body:
            jsondata = json.loads(request.body)
            # Variable jsondata ahora está disponible para uso futuro si es necesario

        # Usar datetime.now() correctamente
        fecha_actual = datetime.now().strftime('%m-%d-%Y')
        Produccion.objects.create(fecha=fecha_actual)
        response_data = {'message': 'POST request received', 'fecha': fecha_actual}
        return JsonResponse(response_data)
