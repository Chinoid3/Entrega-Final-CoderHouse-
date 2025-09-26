from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Page(models.Model):
    """Modelo principal para las páginas del blog"""
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=300, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='pages/', verbose_name="Imagen")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
