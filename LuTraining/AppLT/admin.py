from multiprocessing.connection import Client
from django.contrib import admin
from .models import Cliente, PlanEntrenamiento, Profe

# Register your models here.

admin.site.register(Cliente)
admin.site.register(PlanEntrenamiento)
admin.site.register(Profe)