from django.urls import path
from .views import profeFormulario, planFormulario, clienteFormulario, indumentaria, inicio, cliente, planes, profe

urlpatterns = [

    path('', inicio, name="Inicio"),
    path('cliente/', cliente, name="Cliente"),
    path('planes/', planes, name="Planes"),
    path('profe/', profe, name="Profe"),
    path('indumentaria/', indumentaria, name="Indumentaria"),
    path('clienteFormulario/', clienteFormulario, name="clienteFormulario"),
    path('planFormulario/', planFormulario, name="planFormulario"),
    path('profeFormulario/', profeFormulario, name="profeFormulario"),
    
]