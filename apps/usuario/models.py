from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):

    foto_perfil = models.ImageField(upload_to='usuario/', default='../static/usuarios/default.png')
    sexo = models.CharField(max_length=20)

    REQUIRED_FIELDS = ['first_name', 'email']

    @property
    def nombre(self):
        return self.first_name

    @property
    def apellido(self):
        return self.last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'