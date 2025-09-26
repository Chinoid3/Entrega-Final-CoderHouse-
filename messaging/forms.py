from django import forms
from django.contrib.auth.models import User
from .models import Message, Conversation

class MessageForm(forms.ModelForm):
    """Formulario para enviar mensajes"""
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Escribe tu mensaje aquí...',
                'style': 'border-radius: 1rem; resize: none;'
            })
        }

class ConversationForm(forms.ModelForm):
    """Formulario para crear conversaciones"""
    receiver = forms.ModelChoiceField(
        queryset=User.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Selecciona un usuario"
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 3, 
            'placeholder': 'Escribe tu mensaje inicial...',
            'style': 'border-radius: 1rem; resize: none;'
        })
    )

    class Meta:
        model = Conversation
        fields = []

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Excluir al usuario actual de la lista de destinatarios
            self.fields['receiver'].queryset = User.objects.exclude(id=user.id)
