import json
from django.views import View
from api.models import Orden
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class OrdenView(View):
    #---------------------------Get-----------------------------
    @csrf_exempt
    def get(self, request):
        orden = list(Orden.objects.values())
        if len(orden) > 0:
            datos = {'Ordenes': orden}
        else:
            datos = {'message': 'No se encontraron ordenes'}
        return JsonResponse(datos)

    #---------------------------Post-----------------------------
    @csrf_exempt
    def post(self, request):

        jsondata = json.loads(request.body)

        if jsondata['numero_orden']:
            numero_orden = jsondata['numero_orden']
        else:
            return JsonResponse({'message': 'Numero de orden es requerido'}, status=400)

        if jsondata['produccion_fecha_id']:
            produccion_fecha_id = jsondata['produccion_fecha_id']
        else:
            return JsonResponse({'message': 'produccion_fecha_id es requerido'}, status=400)

        print(produccion_fecha_id,numero_orden)

        # Validando que la numero de orden no exista en la base de datos
        if Orden.objects.filter(numero_orden=numero_orden).exists():
                return JsonResponse({'message': 'Numero de orden ya existe'}, status=400)

        # Crear el registro con el numero de orden
        create_orden = Orden.objects.create(produccion_fecha_id=produccion_fecha_id,numero_orden=numero_orden)

        # Devolver la información del registro creado
        response_data = {'id': create_orden.id,'produccion_fecha_id': create_orden.produccion_fecha_id,'numero_orden':create_orden.numero_orden}
        return JsonResponse(response_data, status=201)
