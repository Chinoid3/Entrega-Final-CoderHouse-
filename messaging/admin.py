from django.contrib import admin
from .models import Message, Conversation

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'participants_list', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['participants__username']
    list_per_page = 20
    date_hierarchy = 'created_at'
    ordering = ['-updated_at']
    
    def participants_list(self, obj):
        return ', '.join([p.username for p in obj.participants.all()])
    participants_list.short_description = 'Participantes'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'conversation', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at', 'sender']
    search_fields = ['content', 'sender__username']
    list_per_page = 20
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información del Mensaje', {
            'fields': ('sender', 'conversation')
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
