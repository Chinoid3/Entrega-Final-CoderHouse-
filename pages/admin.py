from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'author', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'author']
    search_fields = ['title', 'subtitle', 'content', 'author__username']
    list_per_page = 20
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'subtitle', 'author')
        }),
        ('Contenido', {
            'fields': ('content', 'image')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def save_model(self, request, obj, form, change):
        if not change:  # Si es una nueva página
            obj.author = request.user
        super().save_model(request, obj, form, change)
