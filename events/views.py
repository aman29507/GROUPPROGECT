from .forms import EventForm
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Event


def index(request):
    return render(request, 'events/index.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to event list after successful creation
    else:
        form = EventForm()

    return render(request, 'events/event_form.html', {'form': form})