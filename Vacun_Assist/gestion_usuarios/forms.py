from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from gestion_usuarios.models import Usuario


class FormularioRegistro(forms.ModelForm):
    """ Formulario de registro de un usuario en la base de datos
        Variables:
        -password1: Contraseña
        -password2: Verificacion de la contraseña
    
    """

    #widget tiene atributos
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña', 
            'id': 'password1',
            'required' : 'required',     
            }
    ), )

    password2= forms.CharField(label= 'Contraseña de confirmacion', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña nuevamente', 
            'id': 'password2',
            'required' : 'required',     
            }
    ))

    class Meta:
        model = Usuario
        #fields = ('__all__')
        fields = ('email', 'dni', 'nombre', 'apellido','direccion','fecha_nacimiento')
        widgets={
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Correo Electronico:', }
            ),
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre',}),
            'apellido': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido',}
            ),
            'dni': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese su DNI',}
            ),
            'direccion': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese un centro para vacunarse:',}
            ),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese su fecha de nacimiento',}
            ),

            

        }

class FormularioLogin(forms.ModelForm):

    password= forms.CharField(label= 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña ', 
            'id': 'password',
            'required' : 'required',     
            }
    ))


    class Meta:
        model = Usuario
        #fields = ('__all__')
        fields = ('email', 'codigo')
        widgets={
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Correo Electronico:', }
            ),
            'codigo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Codigo:', }
            ),
        }



class FormularioCovid(forms.Form):
    #Cantidad de dosis aplicadas
    pass

class FormularioFiebreA(forms.Form):
    #En que año se aplico
    pass

class FormularioGripe(forms.Form):
    #Fecha de la ultima aplicacion
    pass
