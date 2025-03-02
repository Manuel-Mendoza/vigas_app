from django.views import View
from django.http import JsonResponse
from api.models import Viga
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class VigasView(View):

#-------------------------------Post-----------------------------
    @csrf_exempt
    def post(self, request):
        datos = {'message': 'success'}
        return JsonResponse(datos)

#-------------------------------Get-----------------------------
    def get(self, request):
        vigas = list(Viga.objects.values())
        if len(vigas) > 0:
            datos = {'message': 'Vigas encontradas', 'vigas': vigas}
        else:
            datos = {'message': 'No se encontraron vigas'}
        return JsonResponse(datos)
