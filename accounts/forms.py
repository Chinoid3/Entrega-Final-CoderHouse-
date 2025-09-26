from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    """Formulario para registro de usuarios"""
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=100, required=True, label="Nombre")
    last_name = forms.CharField(max_length=100, required=True, label="Apellido")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            # Crear perfil automáticamente
            UserProfile.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email']
            )
        return user

class UserProfileForm(forms.ModelForm):
    """Formulario para editar perfil de usuario"""
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'avatar', 'bio', 'birth_date']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

class UserForm(forms.ModelForm):
    """Formulario para editar datos básicos del usuario"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
