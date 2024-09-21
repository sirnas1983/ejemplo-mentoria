from django.utils import timezone
from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=False)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=None, null=True)
    noticia = models.TextField(help_text="...ingrese aqui la noticia...", null= False)
    imagen_portada = models.ImageField(upload_to='noticias/', default='../static/noticias/default.png')
    autor = models.CharField(max_length=50)