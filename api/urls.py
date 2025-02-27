from django.urls import path
from api.views import VigasView

urls = [
    path('proyectos/',VigasView.as_view(), name='proyectos'),
]
