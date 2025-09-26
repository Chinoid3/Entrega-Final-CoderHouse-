from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Modelo para extender la información del usuario"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Email")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Avatar")
    bio = models.TextField(max_length=500, blank=True, verbose_name="Biografía")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
