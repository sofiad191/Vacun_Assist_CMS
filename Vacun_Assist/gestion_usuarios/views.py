import re
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from gestion_usuarios.forms import FormularioLogin, FormularioRegistro
from gestion_usuarios.models import Usuario
from django.core.mail import send_mail



# Create your views here.

def inicio(request):
    return render(request, "gestion_usuarios/inicio.html")
    
def registro(request):
    if request.method=="POST":
        miFormulario=FormularioRegistro(request.POST)
    
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data

            #Validar el DNI con el renaper

            #%infForm['codigo']
            mensaje="Se registro tu informacion en VacunAssist! Tu codigo para iniciar sesion es: %s" %(infForm['codigo'])
            send_mail("Registro completo en VacunAssist", mensaje, 'vacunassist.cms@gmail.com', infForm['email'],)

            return render(request, "autenticacion/reg_exito.html")

        
    else:
        miFormulario=FormularioRegistro()

    
    return render(request, "autenticacion/registro.html")


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


def iniciar_sesion(request):
    #Entra una vez que aprieta el boton de enviar
    if request.method=="POST":
        miFormulario=FormularioLogin(request.POST)
    
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data #Aca se guarda toda la info que se lleno en los formularios


            usuario=authenticate(infForm['email'], infForm['password'], infForm['codigo'])

            #Si existe el usuario
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
 

    else:
        #Si entra al else, seria el formulario vacio, para que llene los datos
        miFormulario=FormularioLogin()

    
    return render(request, "autenticacion/login.html", {"form": miFormulario})




def cargar_info_covid(request):


    return render(request, "cargar_info/info_covid.html")

def cargar_info_fiebre_a(request):


    return render(request, "cargar_info/info_fiebre_a.html")

def cargar_info_gripe(request): 


    return render(request, "cargar_info/info_gripe.html")


def modificar_perfil(request):
    #No se puede cambiar todos los datos.
    #Seria reemplazar en la base de datos, los datos viejos con los datos nuevos
    return render(request, "gestion_usuarios/modificar_perfil.html")

def estatus_turno(request):
    #En el archivo html: si tiene elementos: recorrer la lista, y mostrar datos

    return render(request, "gestion_usuarios/estatus_turno.html")
