from django import forms
from .models import Page, Comment

class PageForm(forms.ModelForm):
    """Formulario para crear y editar páginas"""
    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la página'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtítulo de la página'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    """Formulario para comentarios"""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe tu comentario...',
                'style': 'border-radius: 1rem; resize: none;'
            })
        }

class PageSearchForm(forms.Form):
    """Formulario para buscar páginas"""
    search = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar páginas...'
        })
    )
