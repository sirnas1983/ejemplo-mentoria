from django.contrib import admin
from django.urls import path
from django.urls import include
from blog.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('usuario/', include('apps.usuario.urls')),
    path('posts/', include('apps.posts.urls')),
]