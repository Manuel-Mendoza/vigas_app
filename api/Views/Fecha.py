
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
            datos = {'Fecha': fecha}
        else:
            datos = {'message': 'No se encontraron Fechas'}
        return JsonResponse(datos)




#-------------------Dispatch-----------------
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

        #Eliminar para se vaya a subir a la web
#-------------------------------------------------


    def post(self, request):
        print("Cuerpo de la solicitud:", request.body.decode('utf-8'))
        try:
            # Inicializar con None para detectar si no se proporcionó fecha
            fecha_str = None  # Guardar el string
            fecha_obj = None  # Para el objeto datetime

            # Si hay datos en el body, extraemos la fecha
            if request.body:
                jsondata = json.loads(request.body)
                if 'fecha' in jsondata and jsondata['fecha']:
                    fecha_str = jsondata['fecha']
                    try:
                        # Convertir string a objeto datetime
                        fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d')
                    except ValueError:
                        return JsonResponse({'error': 'Formato de fecha inválido. Use YYYY-MM-DD'}, status=400)

            # Si no se proporcionó fecha, usamos la actual
            if fecha_obj is None:
                fecha_obj = datetime.now()

            # Convertir la fecha a un formato adecuado para ID (sin guiones)
            fecha_id = fecha_str.replace('-', '')

            # Verificar si ya existe un registro con esta fecha
            if Produccion.objects.filter(fecha=fecha_str).exists():
                return JsonResponse({
                    'error': 'Ya existe un registro con esta fecha',
                    'fecha': fecha_str
                }, status=400)

            # Crear el registro con la fecha como ID
            produccion = Produccion(id=fecha_id, fecha=fecha_str)
            produccion.save()

            # Devolver la información del registro creado
            response_data = {
                'id': produccion.id,
                'fecha': produccion.fecha,
                'mensaje': 'Registro creado exitosamente'
            }
            return JsonResponse(response_data, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
