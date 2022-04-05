from django.urls import path
from .views import inicio, cliente, planes, profe

urlpatterns = [

    path('', inicio),
    path('cliente/', cliente),
    path('planes/', planes),
    path('profe/', profe),
    
]