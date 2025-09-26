from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """Modelo para mensajes entre usuarios"""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name="Remitente")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', verbose_name="Destinatario")
    subject = models.CharField(max_length=200, verbose_name="Asunto")
    content = models.TextField(verbose_name="Contenido")
    is_read = models.BooleanField(default=False, verbose_name="Leído")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} - {self.sender} a {self.receiver}"
