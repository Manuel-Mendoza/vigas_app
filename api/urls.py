from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrdenViewSet 
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'ordenes', OrdenViewSet)

urlpatterns = [
    # Incluye las URLs generadas por el router
    path('', include(router.urls)),

    # URLs para la documentación de la API
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
