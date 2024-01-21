"""
URL configuration for exrone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from exrone_app.views import hello_world_view
from exrtwoapp.views import hello_MVT_view
from cloud_message_board.views import submit_message, get_message, chat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world_view),
    path('hello_MVT', hello_MVT_view),
    path('messages/submit_message/', submit_message, name="submit_message"),
    path('messages/get_messages/', get_message, name="get_messages"),
    path('messages/chat', chat, name="chat"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
