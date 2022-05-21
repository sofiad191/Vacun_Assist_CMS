from django.db import models

# Create your models here.


class Usuario (models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.CharField(max_length=8)
    fecha_nacimiento=models.DateField()
    direccion=models.CharField(max_length=30)
    email=models.EmailField()
    contraseña=models.CharField(max_length=60)
    codigo=models.CharField(max_length=4)
    #Falta una lista de turnos, que pertenecen al usuario, puede estar vacia.

class Turno(models.Model):
    fecha=models.DateField()
    vacuna=models.CharField(max_length=40)
    # usuario_a_vacunar=models.Usuario() puede ser un campo de tipo usuario, o un campo de tipo dni 
    vacunatorio=models.CharField(max_length=40)