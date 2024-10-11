from apps.usuario.views import RegistrarUsuario
from django.urls import path

app_name = 'usuario'

urlpatterns = [
    path('registro/', RegistrarUsuario.as_view(), name='registrar'),
]