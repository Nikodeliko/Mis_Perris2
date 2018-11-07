from django import forms

#class AgregarUsuario(forms.Form):
 #   username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
  #  password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")
   # correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
perfiles=(
    ('Administrador','Administrador'),
    ('Usuario','Usuario'),
)

class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    perfil=forms.ChoiceField(choices=perfiles)


class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")