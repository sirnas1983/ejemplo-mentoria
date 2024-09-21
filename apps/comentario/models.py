from django.utils import timezone
from django.db import models

from apps.noticia.models import Noticia

# Create your models here.
class Comentario(models.Model):
    autor = models.CharField(max_length=50, null = False)
    fecha_comentario = models.DateTimeField(default=timezone.now, null=False)
    comentario = models.TextField()
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, null=False)