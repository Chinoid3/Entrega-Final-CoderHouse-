from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    """Formulario para enviar mensajes"""
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'content']
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto del mensaje'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe tu mensaje aquí...'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Excluir al usuario actual de la lista de destinatarios
            self.fields['receiver'].queryset = User.objects.exclude(id=user.id)
        else:
            self.fields['receiver'].queryset = User.objects.all()
