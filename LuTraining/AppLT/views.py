from django.http import HttpResponse
from django.shortcuts import render

from .forms import ClienteFormulario, PlanFormulario, ProfeFormulario
from .models import Cliente, PlanEntrenamiento, Profe

# Create your views here.

def inicio(request):
    return render(request,'AppLT/inicio.html')

def cliente(request, nombre, apellido, email):
    
    nuevo_cliente=Cliente(nombre=nombre, apellido=apellido, email=email )
    nuevo_cliente.save()
    return render(request,'AppLT/cliente.html')

def planes(request):
    return render(request,'AppLT/planes.html')

def profe(request):
    return render(request,'AppLT/profe.html')

def indumentaria(request):
    return render(request,'AppLT/indumentaria.html')

def clienteFormulario(request):
    
    if request.method == "POST":
        
        mi_formulario = ClienteFormulario(request.POST)

        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data

            mi_cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            mi_cliente.save()
        
        return render(request, "AppLT/inicio.html")
    else:
        mi_formulario=ClienteFormulario()

        return render(request, "AppLT/clienteFormulario.html", {"mi_formulario":mi_formulario})

def planFormulario(request):
    
    if request.method == "POST":
        
        plan_formulario = PlanFormulario(request.POST)

        if plan_formulario.is_valid():
            
            informacion = plan_formulario.cleaned_data

            mi_plan = PlanEntrenamiento(precio=informacion['precio'], fecha_inicio=informacion['fecha_inicio'], tipo=informacion['tipo'])
            mi_plan.save()
        
        return render(request, "AppLT/inicio.html")
    else:
        plan_formulario=PlanFormulario()

        return render(request, "AppLT/planFormulario.html", {"plan_formulario":plan_formulario})

def profeFormulario(request):
    
    if request.method == "POST":
        
        profe_formulario = ProfeFormulario(request.POST)

        if profe_formulario.is_valid():
            
            informacion = profe_formulario.cleaned_data

            mi_profe = Profe(precio=informacion['precio'], fecha_inicio=informacion['fecha_inicio'], tipo=informacion['tipo'])
            mi_profe.save()
        
        return render(request, "AppLT/inicio.html")
    else:
        profe_formulario=ProfeFormulario()

        return render(request, "AppLT/profeFormulario.html", {"profe_formulario":profe_formulario})