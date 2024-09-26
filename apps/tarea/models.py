from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):

    titulo = models.CharField(max_length=40)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateTimeField()
    tarea = models.TextField()
    is_concluida = models.BooleanField(default=False)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self) -> str:
        return f'{self.titulo} - By: {self.creado_por}'
    
    def is_vencida(self):
        return self.fecha_vencimiento.timestamp() < timezone.now().timestamp() and self.is_concluida == False