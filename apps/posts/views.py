from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.posts.forms import PosteoForm
from django.utils import timezone
from django.urls import reverse_lazy

from apps.posts.models import Posts
# Create your views here.


class CrearPost(LoginRequiredMixin, CreateView):
    model = Posts
    form_model = PosteoForm
    template_name = 'post/crear.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarPost(UpdateView):
    model = Posts
    form_model = PosteoForm
    template_name = 'post/crear.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.fecha_modificacion = timezone.now()
        return super().form_valid(form)
