from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.db import models
from .models import Message


# A view to retrieve the data for the chat. Uses request.session to remember the user.
def display_chat(request):
    if 'username' not in request.session:
        username = request.GET.get('username')
        if username:
            request.session['username'] = username
        else:
            # Redirect to a page to ask for username or handle it differently (Not implemented)
            pass

    username = request.session.get('username')
    messages = Message.objects.filter(
        models.Q(sender=username) | models.Q(recipient=username)
    ).order_by('timestamp')[:20]

    return render(request, 'chat_app/chat.html', {'messages': messages, 'username': username})


# A view to process the POST method: gets data and uploads it to the database.
def process_message(request):
    if request.method == 'POST':
        sender = request.session.get('username')
        recipient = request.POST.get('recipient')
        message_text = request.POST.get('message_text')

        Message.objects.create(sender=sender, recipient=recipient, message_text=message_text)

    return HttpResponseRedirect(reverse('display_chat'))
