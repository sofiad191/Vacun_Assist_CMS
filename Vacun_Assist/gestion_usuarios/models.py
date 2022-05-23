from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random

# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self, dni, email, nombre, apellido, direccion, fecha_nacimiento, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        #normalize_email normaliza el correo para realizar validaciones
        #self.model = Usuario
        usuario=self.model(
            dni=dni, 
            email=self.normalize_email(email), 
            nombre=nombre, 
            apellido=apellido,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            codigo=random.randint(1001,9999))

        #Las contraseñas no se pueden guardar en texto plano
        #Django las encripta asi: Encripta la contraseña y la guarda en password
        usuario.set_password(password)
        usuario.save()
        return usuario

    #password aca es password sin el None
    def create_superuser(self, dni, email, nombre, apellido, direccion, fecha_nacimiento, codigo=None, password=None):
        usuario=self.create_user(
            email, 
            dni=dni, 
            nombre=nombre, 
            apellido=apellido,
            password=password,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            codigo=codigo)

        #No se encripta la contraseña ni se normaliza el email en este metodo porque
        #ya lo hace en el metodo create_user
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    dni=models.CharField('Dni', unique=True, max_length=8)
    email=models.EmailField('Email', max_length=60, unique=True)
    nombre=models.CharField('Nombre', max_length=50, blank=True, null=True) #Se puede dejar en blanco
    apellido=models.CharField('Apellido', max_length=50, blank=True, null=True)
    direccion=models.CharField('Apellido', max_length=50, blank=True, null=True)
    fecha_nacimiento=models.DateField('Fecha de nacimiento')
    codigo=models.CharField('Codigo unico', max_length=4, default=1000)
    usuario_activo=models.BooleanField(default=True) 
    password=models.CharField('Contraseña', max_length=60, default="hola123456")
    #Activado y desactivado de usuarios
    #Todo usuario que tenga el campo en true puede iniciar sesion, internamente django trabaja de esta manera
    usuario_administrador = models.BooleanField(default=False)
    #Se enlazan:
    objects=UsuarioManager()


    #Parametro unico que reconoce al usuario
    USERNAME_FIELD = 'email'

    #Valores que son pedidos
    REQUIRED_FIELDS = ['dni', 'email', 'nombre', 'apellido']

    def __str__(self):
        return f'Usuario {self.nombre}, {self.apellido}'

    def has_perm():
        #Para que se pueda usar el /admin o no. Tiene que estar para que aparezca en el panel
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property

    def is_staff(self):
        #Retorna si es administrador o no
        return self.usuario_administrador


#Agregar "Lista de turnos" a Usuario
#Definir modelo de turno

class Turno(models.Model):
    fecha=models.DateField()
    vacuna=models.CharField(max_length=30)
    usuario=Usuario() # esto ???
