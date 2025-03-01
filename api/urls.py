from django.urls import path
from .Views.Vigas import VigasView
from .Views.Fecha import FechaView
from .Views.Orden import OrdenView

urlpatterns = [
    #-------------APIs FechaView-----------------
    path('fecha/',FechaView.as_view(), name='fecha'),
    path('fecha/<int:id>/',FechaView.as_view(), name='deletefecha'),
    #-------------APIs VigasView-----------------
    path('vigas/',VigasView.as_view(), name='vigas'),
    #-------------APIs OrdenView-----------------
    path('ordenes/',OrdenView.as_view(), name='ordenes'),
]
