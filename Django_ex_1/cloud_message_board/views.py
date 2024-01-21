from django.shortcuts import render, redirect
from .models import Message
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import logging

# Get an instance of a logger
# Used for debugging
logger = logging.getLogger(__name__)


# Create your views here.

# View to submit the message.
def submit_message(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        message = request.POST.get('message')

        Message.objects.create(sender=sender, recipient=recipient, message=message)
        return HttpResponse("Message submitted successfully!")
    return render(request, "submit_message.html")


# View to retrieve the message.
def get_message(request):
    name = request.GET.get('name', '')
    messages = []
    if name:
        messages = Message.objects.filter(
            Q(sender=name) | Q(recipient=name)
        ).order_by('-created_at')[:20]

    return render(request, 'message_list.html', {'messages': messages})


# View for chat rendition.
def chat(request):
    user_name = request.POST.get('user_name', '') if request.method == 'POST' else ''
    logger.info(f"User name received: {user_name}")

    if user_name:
        messages = Message.objects.filter(
            Q(sender=user_name) | Q(recipient=user_name)
        ).order_by('-created_at')[:20]
        logger.info(f"Messages returned: {messages}")
    else:
        messages = []

    return render(request, 'chat.html', {'messages': messages, 'user_name': user_name})
