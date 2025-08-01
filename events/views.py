from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.decorators import login_required

@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        Event.objects.create(title=title, description=description, date=date, creator=request.user)
        return redirect('event_list')
    return render(request, 'events/create_event.html')

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})
