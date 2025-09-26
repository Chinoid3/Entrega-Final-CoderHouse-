from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import models
from .models import Message
from .forms import MessageForm

class InboxView(LoginRequiredMixin, ListView):
    """Vista para mostrar mensajes recibidos (CBV con mixin)"""
    model = Message
    template_name = 'messaging/inbox.html'
    context_object_name = 'messages'
    paginate_by = 10

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user).order_by('-created_at')

class SentMessagesView(LoginRequiredMixin, ListView):
    """Vista para mostrar mensajes enviados"""
    model = Message
    template_name = 'messaging/sent_messages.html'
    context_object_name = 'messages'
    paginate_by = 10

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user).order_by('-created_at')

class MessageCreateView(LoginRequiredMixin, CreateView):
    """Vista para crear mensajes"""
    model = Message
    form_class = MessageForm
    template_name = 'messaging/send_message.html'
    success_url = reverse_lazy('messaging:sent')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        messages.success(self.request, 'Mensaje enviado correctamente.')
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class MessageDetailView(LoginRequiredMixin, DetailView):
    """Vista para mostrar detalles del mensaje"""
    model = Message
    template_name = 'messaging/message_detail.html'
    context_object_name = 'message'

    def get_queryset(self):
        # Solo permitir ver mensajes donde el usuario es remitente o destinatario
        return Message.objects.filter(
            models.Q(sender=self.request.user) | models.Q(receiver=self.request.user)
        )

    def get_object(self):
        message = super().get_object()
        # Marcar como leído si el usuario es el destinatario
        if message.receiver == self.request.user and not message.is_read:
            message.is_read = True
            message.save()
        return message

@login_required
def message_list(request):
    """Vista para listar todos los mensajes del usuario (función con decorador)"""
    sent_messages = Message.objects.filter(sender=request.user).order_by('-created_at')
    received_messages = Message.objects.filter(receiver=request.user).order_by('-created_at')
    
    context = {
        'sent_messages': sent_messages,
        'received_messages': received_messages,
    }
    return render(request, 'messaging/message_list.html', context)
