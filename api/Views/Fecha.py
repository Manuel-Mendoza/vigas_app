
from django.views import View
from api.models import Produccion
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class FechaView(View):
    def get(self, request):
        fecha = list(Produccion.objects.values())
        if len(fecha) > 0:
            datos = {'Fecha': fecha}
        else:
            datos = {'message': 'No se encontraron Fechas'}
        return JsonResponse(datos)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
<<<<<<< HEAD
        # Se revisa si hay body, si no, simplemente continuamos
        if request.body:
            jsondata = json.loads(request.body)
            # Variable jsondata ahora está disponible para uso futuro si es necesario

        # Usar datetime.now() correctamente
        fecha_actual = datetime.now().strftime('%m-%d-%Y')
        Produccion.objects.create(fecha=fecha_actual)
        response_data = {'fecha': fecha_actual}
=======
        # Placeholder for handling POST requests
        # You can add the logic to handle POST data here
        response_data = {'message': 'POST request received'}
>>>>>>> parent of eaf2109 (Se puse autoejecutable el POST de Fecha, para que se cree automaticamente)
        return JsonResponse(response_data)
