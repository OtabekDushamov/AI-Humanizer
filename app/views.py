from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import time

# Create your views here.

def index(request):
    """Render the main index page"""
    return render(request, 'index.html')

@csrf_exempt
@require_http_methods(["POST"])
def humanize_text(request):
    """API endpoint to humanize text"""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        mode = data.get('mode', 'casual')
        
        if not text.strip():
            return JsonResponse({'error': 'Text is required'}, status=400)
        
        # Simple text transformation based on mode
        # For now, just return the text as-is since no actual AI is implemented
        humanized_text = transform_text(text, mode)
        
        # Store in session for history (optional - frontend handles this)
        if 'humanizer_history' not in request.session:
            request.session['humanizer_history'] = []
        
        history_item = {
            'original_text': text,
            'humanized_text': humanized_text,
            'mode': mode,
            'timestamp': time.time()
        }
        
        # Add to session history (keep last 10 items)
        history = request.session.get('humanizer_history', [])
        history.insert(0, history_item)
        history = history[:10]  # Keep only last 10 items
        request.session['humanizer_history'] = history
        
        return JsonResponse({
            'original_text': text,
            'humanized_text': humanized_text,
            'mode': mode,
            'timestamp': history_item['timestamp']
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def get_history(request):
    """API endpoint to get session history"""
    try:
        history = request.session.get('humanizer_history', [])
        one_hour_ago = time.time() - 3600  # 1 hour ago
        
        # Filter out items older than 1 hour
        recent_history = [item for item in history if item.get('timestamp', 0) > one_hour_ago]
        
        return JsonResponse({
            'history': recent_history[:3]  # Return only first 3 items
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def transform_text(text, mode):
    """Transform text based on the selected mode"""
    # This is a simple placeholder transformation
    # In a real application, you would integrate with an AI service
    
    transformations = {
        'academic': lambda t: f"In this analysis, we observe that {t.lower()}",
        'casual': lambda t: f"Hey! So {t.lower()}",
        'emotional': lambda t: f"My heart feels that {t.lower()}",
        'marketing': lambda t: f"Amazing! {t} - This will revolutionize your experience!",
        'storytelling': lambda t: f"Once upon a time, {t.lower()}",
        'simplify': lambda t: f"Simply put: {t.lower()}"
    }
    
    return transformations.get(mode, lambda t: t)(text)
