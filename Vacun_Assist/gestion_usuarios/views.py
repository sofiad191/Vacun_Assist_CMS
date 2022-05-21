import re
from django.shortcuts import render, redirect
# from django.template import loader
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from gestion_usuarios.forms import FormularioAutenticacion, FormularioRegistro



# Create your views here.

def inicio(request):
    return render(request, "gestion_usuarios/inicio.html")


"""class registro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, "autenticacion/registro.html", {"form": form})

    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():
            usuario=form.save()

            login(request, usuario)

            return redirect('inicio')

        else:
            #Por cada mensaje de error en el formulario.
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            #Devuelve el formulario como estaba antes (los campos validos) + los errores detallados  
            return render(request, "autenticacion/registro.html", {"form": form})"""
    
def registro(request):
    #Entra una vez que aprieta el boton de enviar
    if request.method=="POST":
        miFormulario=FormularioRegistro(request.POST)
    
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data

            #Aca seria registrar la info

    else:
        #Si entra al else, seria el formulario vacio, para que llene los datos
        miFormulario=FormularioRegistro()

    
    return render(request, "autenticacion/registro.html", {"form": miFormulario})


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


"""def iniciar_sesion(request):

    #Si se apreto el boton:
    if request.method=="POST":
        return redirect('inicio')
        form=AuthenticationForm(request, data=request.POST)
    
        if form.is_valid():
            #La informacion que ingreso el usuario
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            #Autenticar el usuario
            usuario=authenticate(username=nombre_usuario, password=contra)

            #Si existe el usuario
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')

            else:
                messages.error(request, "usuario no valido")

        else:
            messages.error(request, "Informacion incorrecta")

    #Mientras que no se apriete el boton:
        
    form=AuthenticationForm()
    return render(request, "autenticacion/login.html", {"form": form})"""

def iniciar_sesion(request):
    if request.method=="POST":
        miFormulario=FormularioAutenticacion(request.POST)
    
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data

            #Aca seria guardar chequear la data en base de datos y "entrar" a la sesion

    else:
        miFormulario=FormularioAutenticacion()

    
    return render(request, "autenticacion/login.html", {"form": miFormulario})