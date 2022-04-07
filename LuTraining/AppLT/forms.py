
from django import forms

class ClienteFormulario(forms.Form):

    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()


class PlanFormulario(forms.Form):

    precio=forms.IntegerField()
    fecha_inicio=forms.DateField()
    tipo=forms.CharField(max_length=20)

class ProfeFormulario(forms.Form):

    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    tel=forms.IntegerField()