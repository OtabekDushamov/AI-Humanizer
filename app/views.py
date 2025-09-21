from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from .openai import humanize
from .models import User, Request
import json
import time

# Create your views here.

def get_or_create_user(session_key):
    """Get or create a user based on session key"""
    if not session_key:
        return None
    
    user, created = User.objects.get_or_create(
        session_key=session_key,
        defaults={'last_active': timezone.now()}
    )
    
    # Update last active timestamp
    user.update_last_active()
    
    return user

def index(request):
    """Render the main index page"""
    return render(request, 'index.html')

@csrf_exempt
@require_http_methods(["POST"])
def humanize_text(request):
    """API endpoint to humanize text"""
    start_time = time.time()
    
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        mode = data.get('mode', 'casual')
        
        if not text.strip():
            return JsonResponse({'error': 'Text is required'}, status=400)
        
        # Get or create user based on session
        user = get_or_create_user(request.session.session_key)
        
        # Use OpenAI to humanize the text
        humanized_text = humanize(text, mode)
        
        # Calculate processing time
        processing_time = time.time() - start_time
        
        # Save to database if user exists
        if user:
            Request.objects.create(
                user=user,
                original_text=text,
                humanized_text=humanized_text,
                mode=mode,
                processing_time=processing_time
            )
        
        return JsonResponse({
            'original_text': text,
            'humanized_text': humanized_text,
            'mode': mode,
            'processing_time': processing_time
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def get_history(request):
    """API endpoint to get session history from database"""
    try:
        # Get user from session
        user = get_or_create_user(request.session.session_key)
        
        # Get history from database (last 3 requests)
        history = []
        if user:
            recent_requests = Request.objects.filter(user=user).order_by('-created_at')[:3]
            history = [
                {
                    'original_text': req.original_text,
                    'humanized_text': req.humanized_text,
                    'mode': req.mode,
                    'timestamp': req.created_at.timestamp(),
                    'created_at': req.created_at.isoformat()
                }
                for req in recent_requests
            ]
        
        return JsonResponse({
            'history': history
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
