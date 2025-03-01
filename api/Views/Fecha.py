import json
from django.views import View
from api.models import Produccion
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime

@method_decorator(csrf_exempt, name='dispatch')
class FechaView(View):

#-----------------GET-------------------
    def get(self, request):
        fecha = list(Produccion.objects.values())
        if len(fecha) > 0:
            datos = {'Fecha': fecha}
        else:
            datos = {'message': 'No se encontraron Fechas'}
        return JsonResponse(datos)


#-------------------Dispatch-----------------
    #Eliminar para se vaya a subir a la web
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
#-------------------------------------------------


#-------------------POST-----------------
    def post(self, request):
            fecha = None

            # Si hay datos en el body, extraemos la fecha
            if request.body:
                jsondata = json.loads(request.body)
                if jsondata['fecha']:
                    fecha = jsondata['fecha']

            # Si no se proporcionó fecha, usamos la actual
            if fecha is None:
                fecha = datetime.now().strftime('%Y-%m-%d')

            #Validando que la fecha no exista en la base de datos
            if Produccion.objects.filter(fecha=fecha).exists():
                return JsonResponse({'message': 'Fecha ya existe'}, status=400)

            # Crear el registro con la fecha
            produccion = Produccion.objects.create(fecha=fecha)

            # Devolver la información del registro creado
            response_data = {'id': produccion.id, 'fecha': produccion.fecha}
            return JsonResponse(response_data, status=201)


#--------------------Delete-----------------
    @csrf_exempt
    def delete(self, request, id):
        fecha = list(Produccion.objects.filter(id=id).values())
        #print(fecha)
        if len(fecha) > 0:
            Produccion.objects.filter(id=id).delete()
            return JsonResponse({'message': 'Fecha eliminada'}, status=200)
        else:
            return JsonResponse({'message': 'Fecha no encontrada'}, status=404)
