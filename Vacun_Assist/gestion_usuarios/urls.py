from django.urls import path

from gestion_usuarios import views

urlpatterns = [
    path('', views.hola, name= "hola"),
    path('hola', views.hola, name="hola"),
    path('chau', views.chau, name="chau"),
]
