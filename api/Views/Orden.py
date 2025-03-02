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
        numero_orden = jsondata.get('numero_orden')
        produccion_fecha_id = jsondata.get('produccion_fecha_id')

        if not numero_orden:
                return JsonResponse({'message': 'Numero de orden es requerido'}, status=400)

        # Validar que el número de orden NO exista en la misma fecha
        if Orden.objects.filter(numero_orden=numero_orden, produccion_fecha_id=produccion_fecha_id).exists():
            return JsonResponse({'message': 'Numero de orden ya existe en esta fecha'}, status=400)


        print(produccion_fecha_id,numero_orden)

         # Crear la orden
        create_orden = Orden.objects.create(
                         produccion_fecha_id=produccion_fecha_id,
                         numero_orden=numero_orden)

        # Devolver la información del registro creado
        return JsonResponse({
                        'id': create_orden.id,
                        'produccion_fecha_id': create_orden.produccion_fecha_id,
                        'numero_orden': create_orden.numero_orden
                    }, status=201)
