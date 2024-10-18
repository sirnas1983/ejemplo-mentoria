from django.views.generic import CreateView, UpdateView, ListView
from apps.posts.forms import PosteoForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from apps.posts.models import Posts
# Create your views here.


class CrearPost(UserPassesTestMixin, CreateView):
    model = Posts
    form_class = PosteoForm
    template_name = 'posts/crear.html'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.fecha_publicacion = timezone.now()
        return super().form_valid(form)

class EditarPost(UserPassesTestMixin, UpdateView):
    model = Posts
    form_class = PosteoForm
    template_name = 'posts/crear.html'

    def test_func(self):
        return self.request.user == self.get_object.autor or self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.fecha_modificacion = timezone.now()
        return super().form_valid(form)

class VerPost(ListView):
    model = Posts
    template_name = 'posts/ver_todos.html'

class VerMisPost(ListView):
    model = Posts
    template_name = 'posts/ver_todos.html'

    def get_queryset(self):
        return super().get_queryset().filter(autor=self.request.user)