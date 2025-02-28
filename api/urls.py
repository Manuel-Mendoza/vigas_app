from django.urls import path
from .views import VigasView,OrdenView,FechaView

urlpatterns = [
    path('vigas/',VigasView.as_view(), name='vigas'),
    path('ordenes/',OrdenView.as_view(), name='ordenes'),
    path('fecha/',FechaView.as_view(), name='produccion'),
]
