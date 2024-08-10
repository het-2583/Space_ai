from django.urls import path
from .views import space_ai_view



urlpatterns = [
    path('', space_ai_view, name='space_bot/templates.space_ai'),
]