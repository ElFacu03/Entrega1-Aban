from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'AppLT/inicio.html')

def cliente(request):
    return render(request,'AppLT/cliente.html')

def planes(request):
    return render(request,'AppLT/planes.html')

def profe(request):
    return render(request,'AppLT/profe.html')