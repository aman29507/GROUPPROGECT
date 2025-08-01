from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def send_message(request):
    if request.method == 'POST':
        receiver_id = request.POST['receiver']
        body = request.POST['body']
        receiver = User.objects.get(id=receiver_id)
        Message.objects.create(sender=request.user, receiver=receiver, body=body)
        return redirect('inbox')
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messaging/send_message.html', {'users': users})

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {'messages': messages})
