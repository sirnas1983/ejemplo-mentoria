from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import Usuario


class FormEditarUsuario(forms.Form):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'foto_perfil', 'sexo']

class FormRegistrarUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']