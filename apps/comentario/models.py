from django.utils import timezone
from django.db import models

from apps.posts.models import Posts

# Create your models here.
class Comentario(models.Model):
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(to=Posts, null=False, on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.fecha_creacion) + '-' + self.autor