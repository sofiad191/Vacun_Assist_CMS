import re
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
#from django.contrib import messages
from gestion_usuarios.forms import FormularioAutenticacion, FormularioRegistro



# Create your views here.

def inicio(request):
    return render(request, "gestion_usuarios/inicio.html")
    
def registro(request):
    #Entra una vez que aprieta el boton de enviar
    if request.method=="POST":
        miFormulario=FormularioRegistro(request.POST)
    
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data

            #Aca seria registrar la info
            #Mandar mail con el codigo generado

    else:
        #Si entra al else, seria el formulario vacio, para que llene los datos
        miFormulario=FormularioRegistro()

    
    return render(request, "autenticacion/registro.html", {"form": miFormulario})


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def iniciar_sesion(request):
    if request.method=="POST":
        miFormulario=FormularioAutenticacion(request.POST)
    
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data

            #Aca seria guardar chequear la data en base de datos y "entrar" a la sesion

    else:
        miFormulario=FormularioAutenticacion()

    
    return render(request, "autenticacion/login.html", {"form": miFormulario})