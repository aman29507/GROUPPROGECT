from django.shortcuts import render ,get_object_or_404, redirect

from .models import Message
from .forms import MessageForm

def index(request):
    return render(request, 'messaging/index.html')

def inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    print(messages)
    return render(request, 'messaging/inbox.html', {'messages': messages})

def message_list(request):
    messages = Message.objects.all()  # Or filter messages based on the user
    return render(request, 'messaging/message_list.html', {'messages': messages})

def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'messaging/message_detail.html', {'message': message})

def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inbox')  # Redirect to the inbox after sending
    else:
        form = MessageForm()
    
    return render(request, 'messaging/send_message.html', {'form': form})


# Create your views here.
