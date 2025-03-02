import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from api.models import Viga

@method_decorator(csrf_exempt, name='dispatch')
class VigasView(View):


#-------------------POST-----------------
    @csrf_exempt
    def post(self, request):

        jsondata = json.loads(request.body)
        orden_id = jsondata.get('orden_id')
        nombre_viga = jsondata.get('nombre_viga')
        cantidad = jsondata.get('cantidad')
        medidas = jsondata.get('medidas')
        tipo = jsondata.get('tipo')

        create_orden = Viga.objects.create(
            orden_id=orden_id,
            nombre_viga=nombre_viga,
            cantidad=cantidad,
            medidas=medidas,
            tipo=tipo)

    # Devolver la información del registro creado
        response_data = {"id": create_orden.id,
			"orden_id": create_orden.orden_id,
			"nombre_viga": create_orden.nombre_viga,
			"cantidad": create_orden.cantidad,
			"medidas": create_orden.medidas,
			"tipo": create_orden.tipo}

        return JsonResponse(response_data, status=201)

#-------------------------------Get-----------------------------
    def get(self, request):
        vigas = list(Viga.objects.values())
        if len(vigas) > 0:
            datos = {'message': 'Vigas encontradas', 'vigas': vigas}
        else:
            datos = {'message': 'No se encontraron vigas'}
        return JsonResponse(datos)

#-------------------------------Delete-----------------------------
    def delete(self, request, id):
        try:
            Viga.objects.get(id=id).delete()
            datos = {'message': 'Viga eliminada'}
        except Viga.DoesNotExist:
            datos = {'message': 'Viga no encontrada'}

        return JsonResponse(datos)
