from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    """Modelo para conversaciones entre usuarios"""
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Conversación"
        verbose_name_plural = "Conversaciones"
        ordering = ['-updated_at']

    def __str__(self):
        return f"Conversación entre {', '.join([p.username for p in self.participants.all()])}"

class Message(models.Model):
    """Modelo para mensajes en conversaciones"""
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages', null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name="Remitente")
    content = models.TextField(verbose_name="Contenido")
    is_read = models.BooleanField(default=False, verbose_name="Leído")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['created_at']

    def __str__(self):
        return f"Mensaje de {self.sender.username} en conversación {self.conversation.id}"
