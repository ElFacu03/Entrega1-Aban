from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    
    def __str__(self):
        return self.nombre


class PlanEntrenamiento(models.Model):    
    precio=models.IntegerField()
    fecha_inicio=models.DateField()
    tipo=models.CharField(max_length=10)
    


class Profe(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    tel=models.IntegerField()