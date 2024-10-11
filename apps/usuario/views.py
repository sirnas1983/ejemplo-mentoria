from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from apps.usuario.forms import FormRegistrarUsuario
from django.contrib.auth import login

from apps.usuario.models import Usuario




class RegistrarUsuario(CreateView):

    model = Usuario
    form_class = FormRegistrarUsuario
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        usuario = form.save()
        login(self.request, usuario)
        return super().form_valid(form)