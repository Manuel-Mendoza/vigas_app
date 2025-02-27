from django.urls import path
from .views import VigasView

urlpatterns = [
    path('proyectos/',VigasView.as_view(), name='proyectos'),
]
