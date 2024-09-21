from django.shortcuts import render
from django.views.generic import TemplateView

# vista basada en funciones
def inicio(request):
    return render(request, 'inicio.html')

def main(request):
    contexto = {'variable' : "esta es mi variable"}
    lista = {}
    for i in range(10):
        lista[i] = str(i) + "variable" 
        print(str(i) + "variable")
    print(lista)
    contexto['lista'] = lista
    return render(request, 'main.html', contexto)

# vista basada en clase
class Inicio(TemplateView):
    template_name = 'inicio.html'