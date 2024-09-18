from django.utils import timezone
from django.db import models

# Create your models here.
class Posts(models.Model):
    titulo = models.CharField(max_length=30, help_text="Ingres un titulo para el posteo", null=False)
    contenido = models.TextField(null=False)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(null=True)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo