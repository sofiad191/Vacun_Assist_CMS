from django import forms

class FormularioRegistro(forms.Form):

    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    dni=forms.CharField(max_length=8)
    fecha_nacimiento=forms.DateField()
    direccion=forms.CharField(max_length=30)
    email=forms.EmailField()
    contraseña1=forms.CharField(max_length=30)
    contraseña2=forms.CharField(max_length=30)


class FormularioAutenticacion(forms.Form):
    email=forms.EmailField()
    contraseña=forms.CharField(max_length=100)
    codigo=forms.CharField(max_length=4)
