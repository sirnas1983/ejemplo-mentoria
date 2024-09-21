from django.contrib import admin
from apps.noticia.models import Noticia

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'subtitulo' ,'fecha_creacion', 'autor', 'imagen_portada', 'noticia']

admin.site.register(Noticia ,NoticiaAdmin)