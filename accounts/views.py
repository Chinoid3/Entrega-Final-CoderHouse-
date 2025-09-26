from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserProfileForm, UserForm
from .models import UserProfile

class CustomLoginView(LoginView):
    """Vista personalizada de login"""
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pages:home')

    def form_valid(self, form):
        messages.success(self.request, f'¡Bienvenido/a {form.get_user().username}!')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    """Vista personalizada de logout"""
    next_page = reverse_lazy('pages:home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Has cerrado sesión correctamente.')
        return super().dispatch(request, *args, **kwargs)

class UserRegistrationView(CreateView):
    """Vista para registro de usuarios"""
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        messages.success(self.request, '¡Registro exitoso! Ya puedes iniciar sesión.')
        return super().form_valid(form)

@login_required
def profile_view(request):
    """Vista para mostrar el perfil del usuario"""
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Crear perfil si no existe
        profile = UserProfile.objects.create(
            user=request.user,
            first_name=request.user.first_name,
            last_name=request.user.last_name,
            email=request.user.email
        )
    return render(request, 'accounts/profile.html', {'profile': profile})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Vista para editar perfil (CBV con mixin)"""
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado correctamente.')
        return super().form_valid(form)

@login_required
def edit_user_view(request):
    """Vista para editar datos básicos del usuario (función con decorador)"""
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Datos actualizados correctamente.')
            return redirect('accounts:profile')
    else:
        user_form = UserForm(instance=request.user)
    
    return render(request, 'accounts/edit_user.html', {'user_form': user_form})

@login_required
def change_password_view(request):
    """Vista para cambiar contraseña"""
    from django.contrib.auth.forms import PasswordChangeForm
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Contraseña cambiada correctamente.')
            return redirect('accounts:profile')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'accounts/change_password.html', {'form': form})
