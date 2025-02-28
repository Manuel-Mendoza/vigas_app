from django.urls import path
from .Views.Vigas import VigasView
from .Views.Fecha import FechaView
from .Views.Orden import OrdenView

urlpatterns = [
    path('vigas/',VigasView.as_view(), name='vigas'),
    path('ordenes/',OrdenView.as_view(), name='ordenes'),
    path('fecha/',FechaView.as_view(), name='produccion'),
]
