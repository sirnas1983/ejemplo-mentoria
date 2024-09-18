from django.contrib import admin

from apps.comentario.models import Comentario

# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'contenido','fecha_creacion', 'post')
    list_filter = ('autor', 'fecha_creacion')
    search_fields = ('autor', 'contenido','fecha_creacion', 'post')

admin.site.register(Comentario, ComentarioAdmin)

