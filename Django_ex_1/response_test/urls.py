from django.urls import path
from . import views

urlpatterns = [
    path('http/', views.http_response, name='http_response'),
    path('httpnotfound/', views.not_found_response, name="http_notfound"),
    path('json/', views.json_response, name='json_response'),
    path('streaming/', views.streaming_response, name="straming_response"),
    path('file/', views.file_response, name="file_response"),
]
