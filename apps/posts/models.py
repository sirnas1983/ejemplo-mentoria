from django.db import models
from django.utils import timezone
from apps.usuario.models import Usuario

# Create your models here.
class Posts(models.Model):
    titulo = models.CharField(max_length=30, help_text="Ingres un titulo para el posteo", null=False)
    contenido = models.TextField(null=False)
    autor = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=False)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(null=True)
    publicado = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='posts/', default='../static/default.png', null=True, blank=True)

    def __str__(self):
        return self.titulo