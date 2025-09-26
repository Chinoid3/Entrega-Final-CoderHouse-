from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Page
from .forms import PageForm, PageSearchForm

def home_view(request):
    """Vista de inicio"""
    return render(request, 'pages/home.html')

def about_view(request):
    """Vista 'Acerca de mí'"""
    return render(request, 'pages/about.html')

class PageListView(ListView):
    """Vista para listar páginas (CBV)"""
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    paginate_by = 6

    def get_queryset(self):
        queryset = Page.objects.all()
        search_query = self.request.GET.get('search')
        
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(subtitle__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = PageSearchForm(self.request.GET)
        return context

class PageDetailView(DetailView):
    """Vista para mostrar detalles de una página"""
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

class PageCreateView(LoginRequiredMixin, CreateView):
    """Vista para crear páginas (CBV con mixin)"""
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Página creada correctamente.')
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    """Vista para editar páginas"""
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')

    def form_valid(self, form):
        messages.success(self.request, 'Página actualizada correctamente.')
        return super().form_valid(form)

    def get_queryset(self):
        # Solo permitir editar páginas propias
        return Page.objects.filter(author=self.request.user)

class PageDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para eliminar páginas"""
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page_list')

    def form_valid(self, form):
        messages.success(self.request, 'Página eliminada correctamente.')
        return super().form_valid(form)

    def get_queryset(self):
        # Solo permitir eliminar páginas propias
        return Page.objects.filter(author=self.request.user)
