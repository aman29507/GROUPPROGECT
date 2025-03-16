from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreationForm, AuthenticationForm
from .models import MembershipRequest

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
        MembershipRequest.objects.create(user=user, membership_type=user.membership_type)
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MembershipRequest

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admins to home page

    pending_requests = MembershipRequest.objects.filter(status='pending')
    return render(request, 'admin_dashboard.html', {'pending_requests': pending_requests})

@login_required
def approve_request(request, request_id):
    if request.user.is_superuser:
        membership_request = MembershipRequest.objects.get(id=request_id)
        membership_request.status = 'approved'
        membership_request.save()
    return redirect('admin_dashboard')

@login_required
def reject_request(request, request_id):
    if request.user.is_superuser:
        membership_request = MembershipRequest.objects.get(id=request_id)
        membership_request.status = 'rejected'
        membership_request.save()
    return redirect('admin_dashboard')
# Create your views here.
