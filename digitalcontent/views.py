# from django.shortcuts import render
# def digitalcontent_view(request):
#     return render(request, 'digitalcontent\digital.html') 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Event, RegisteredEvent  # Assuming these models exist
from accounts.models import MembershipRequest
# @login_required
# def digitalcontent_view(request):
#     # Fetch all events
#     events = Event.objects.all()

#     # Fetch registered events only for regular users
#     registered_events = None
#     if not request.user.is_staff:
#         registered_events = RegisteredEvent.objects.filter(user=request.user)

#     return render(request, 'digitalcontent/digital.html', {
#         'events': events,
#         'registered_events': registered_events,
#     })


# @login_required
# def digitalcontent_view(request):
#     # Fetch all events
#     events = Event.objects.all()

#     # Fetch registered events only for regular users
#     registered_events = None
#     if not request.user.is_staff:
#         registered_events = RegisteredEvent.objects.filter(user=request.user)

#     return render(request, 'digitalcontent/digital.html', {
#         'events': events,
#         'registered_events': registered_events,
#     })
@login_required
def digitalcontent_view(request):
    # Fetch all events
    events = Event.objects.all()
    print(events)  # Debugging: Print events to the console

    return render(request, 'digitalcontent/digital.html', {
        'events': events,
    })


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('login')  # Redirect non-admin users to login

    # Fetch pending membership requests
    pending_requests = MembershipRequest.objects.filter(status='pending')

    return render(request, 'accounts/admin_dashboard.html', {'pending_requests': pending_requests})


def digitalcontent_view(request):
    return render(request, 'digitalcontent/digitalcontent.html')  