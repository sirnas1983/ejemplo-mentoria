from django.contrib import admin

from apps.comentario.models import Comentario

# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['id','autor','fecha_comentario','comentario','noticia']

admin.site.register(Comentario, ComentarioAdmin)