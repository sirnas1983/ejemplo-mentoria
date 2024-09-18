from django.contrib import admin

from apps.posts.models import Posts

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ('fecha_publicacion','titulo','autor', 'contenido')
    list_filter = ('autor', 'titulo', 'fecha_publicacion')
    search_fields = ('autor', 'titulo', 'fecha_publicacion')

admin.site.register(Posts, PostsAdmin)

