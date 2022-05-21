import re
from django.shortcuts import render
from django.template import loader

# Create your views here.

def hola(request):
    return render(request, "gestion_usuarios/hola.html")


def chau(request):
    return render(request, "gestion_usuarios/chau.html")