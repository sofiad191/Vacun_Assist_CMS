from django.urls import path

from .views import inicio, registro, cerrar_sesion, iniciar_sesion

urlpatterns = [
    path('', inicio, name= "inicio"),
    path('inicio', inicio, name= "inicio"),
    #path('registro',registro.as_view(), name="registro"),
    path('registro', registro, name="registro"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),

]
