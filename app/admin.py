from django.contrib import admin
from .models import User, Request

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'created_at', 'last_active', 'request_count']
    list_filter = ['created_at', 'last_active']
    search_fields = ['session_key']
    readonly_fields = ['created_at', 'last_active']
    ordering = ['-last_active']
    
    def request_count(self, obj):
        return obj.requests.count()
    request_count.short_description = 'Total Requests'

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'mode', 'text_preview', 'created_at', 'processing_time']
    list_filter = ['mode', 'created_at', 'user']
    search_fields = ['original_text', 'humanized_text', 'user__session_key']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    def text_preview(self, obj):
        return obj.text_preview
    text_preview.short_description = 'Text Preview'
