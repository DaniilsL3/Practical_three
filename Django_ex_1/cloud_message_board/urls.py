from django.urls import path
from . import views

urlpatterns = [
    path('submit_message', views.submit_message, name="submit_message"),
    path('get_message', views.get_message, name="get_message"),
    path('chat', views.chat, name="chat"),
]