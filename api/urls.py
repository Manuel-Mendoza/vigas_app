from django.urls import path
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import OrdenViewSet

router = DefaultRouter()
router.register(r'ordenes', OrdenViewSet)

urlpatterns = [
    # URLs para la documentación de la API
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Interfaz Swagger UI opcional
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Interfaz ReDoc opcional
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
