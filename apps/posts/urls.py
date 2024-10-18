from django.urls import path
from apps.posts.views import CrearPost, EditarPost, VerPost

app_name = 'posts'

urlpatterns= [
    path('crear/', CrearPost.as_view(), name='crear'),
    path('editar/<int:pk>',EditarPost.as_view(), name="editar" ),
    path('', VerPost.as_view(), name='ver-todos')
]