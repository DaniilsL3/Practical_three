from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.display_chat, name='display_chat'),
    path('send-message/', views.process_message, name='process_message'),
]
