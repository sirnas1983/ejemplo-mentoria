from django.contrib import admin

from apps.usuario.models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_staff']