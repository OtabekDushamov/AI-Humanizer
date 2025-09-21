from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    """User model based on session key"""
    session_key = models.CharField(max_length=40, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-last_active']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"User {self.session_key[:8]}... ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
    
    def update_last_active(self):
        """Update the last active timestamp"""
        self.last_active = timezone.now()
        self.save(update_fields=['last_active'])


class Request(models.Model):
    """Request model to store all humanization requests"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    original_text = models.TextField()
    humanized_text = models.TextField()
    mode = models.CharField(max_length=20, choices=[
        ('academic', 'Academic'),
        ('casual', 'Casual'),
        ('emotional', 'Emotional'),
        ('marketing', 'Marketing'),
        ('storytelling', 'Storytelling'),
        ('simplify', 'Simplify'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    processing_time = models.FloatField(null=True, blank=True, help_text="Processing time in seconds")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
    
    def __str__(self):
        return f"Request {self.id} - {self.mode} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
    
    @property
    def text_preview(self):
        """Return a preview of the original text"""
        return self.original_text[:50] + "..." if len(self.original_text) > 50 else self.original_text
