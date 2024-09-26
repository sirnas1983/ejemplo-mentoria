from django.shortcuts import get_object_or_404, redirect
from .forms import TareaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.decorators.http import require_POST
from .models import Tarea

class TareaListView(ListView):
    model = Tarea
    template_name = 'tarea_list.html'
    context_object_name = 'tareas'

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea_detail.html'
    context_object_name = 'tarea'

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tarea_confirm_delete.html'
    success_url = reverse_lazy('tarea-list')

class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tarea-list')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user  # Asignamos el usuario autenticado
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Muestra errores de validación en la consola
        return super().form_invalid(form)

class TareaUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tarea-list')

def toggle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if not tarea.is_vencida(): 
        tarea.is_concluida = not tarea.is_concluida 
    tarea.save()
    return redirect('tarea-list')

