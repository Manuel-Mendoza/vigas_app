from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrdenViewSet

router = DefaultRouter()
router.register(r'ordenes', OrdenViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
