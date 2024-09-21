from django.contrib import admin
from django.urls import path

from noticiero.views import Inicio, inicio, main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.as_view(), name='inicio'),
    path('main/', main, name='main'),
]
