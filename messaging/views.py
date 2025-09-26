from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import models
from .models import Message, Conversation
from .forms import MessageForm, ConversationForm

@login_required
def message_list(request):
    """Vista para listar todas las conversaciones del usuario (función con decorador)"""
    conversations = Conversation.objects.filter(participants=request.user).order_by('-updated_at')
    
    context = {
        'conversations': conversations,
    }
    return render(request, 'messaging/message_list.html', context)

@login_required
def conversation_detail(request, conversation_id):
    """Vista para mostrar una conversación específica"""
    conversation = get_object_or_404(Conversation, id=conversation_id, participants=request.user)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            return redirect('messaging:conversation', conversation_id=conversation_id)
    else:
        form = MessageForm()
    
    context = {
        'conversation': conversation,
        'form': form,
        'messages': conversation.messages.all()
    }
    return render(request, 'messaging/conversation_detail.html', context)

@login_required
def start_conversation(request):
    """Vista para iniciar una nueva conversación"""
    if request.method == 'POST':
        form = ConversationForm(request.POST, user=request.user)
        if form.is_valid():
            # Crear conversación
            conversation = Conversation.objects.create()
            conversation.participants.add(request.user, form.cleaned_data['receiver'])
            
            # Crear mensaje inicial
            Message.objects.create(
                conversation=conversation,
                sender=request.user,
                content=form.cleaned_data['content']
            )
            
            messages.success(request, 'Conversación iniciada correctamente.')
            return redirect('messaging:conversation', conversation_id=conversation.id)
    else:
        form = ConversationForm(user=request.user)
    
    return render(request, 'messaging/start_conversation.html', {'form': form})

@login_required
def inbox_view(request):
    return render(request, "messaging/inbox.html")