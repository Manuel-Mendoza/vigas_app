from django.views import View
from django.http import JsonResponse
from .models import Viga


# Create your views here.

class VigasView(View):

    def get(self, request):
        vigas = list(Viga.objects.values())
        if len(vigas) > 0:
            datos = {'message': 'Vigas encontradas', 'vigas': vigas}
        else:
            datos = {'message': 'No se encontraron vigas'}
        return JsonResponse(datos)

#_____________________________GET_________________________

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
