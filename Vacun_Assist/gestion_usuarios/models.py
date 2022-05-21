from django.db import models

# Create your models here.


class Usuario (models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.CharField(max_length=8)
    fecha_nacimiento=models.DateField()
    direccion=models.CharField(max_length=30)
    email=models.EmailField()
