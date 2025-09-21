from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('api/humanize/', humanize_text, name='humanize_text'),
    path('api/history/', get_history, name='get_history'),
]