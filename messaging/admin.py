from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'sender', 'receiver', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at', 'sender', 'receiver']
    search_fields = ['subject', 'content', 'sender__username', 'receiver__username']
    list_per_page = 20
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información del Mensaje', {
            'fields': ('sender', 'receiver', 'subject')
        }),
        ('Contenido', {
            'fields': ('content',)
        }),
        ('Estado', {
            'fields': ('is_read',)
        }),
        ('Fecha', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f"{queryset.count()} mensajes marcados como leídos.")
    mark_as_read.short_description = "Marcar como leído"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, f"{queryset.count()} mensajes marcados como no leídos.")
    mark_as_unread.short_description = "Marcar como no leído"
    
    actions = [mark_as_read, mark_as_unread]
