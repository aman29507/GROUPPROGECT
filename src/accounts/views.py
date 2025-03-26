from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from .forms import SignupForm, AuthenticationForm  # Use the correct forms
from .models import CustomUser  # Ensure CustomUser is imported
from django.contrib.auth.decorators import login_required
from .models import Activity
from django.db.models import Sum
import pandas as pd
from django.utils.timezone import now


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)  # Use the SignupForm instead of CustomUser
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signing up
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = SignupForm()  # Create an empty instance of SignupForm
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')  # Render the dashboard template


def activity_report(request):
    time_period = request.GET.get('period', 'monthly')
    content_type = request.GET.get('content_type', None)

    filters = {}
    if content_type:
        filters['content__content_type'] = content_type

    activities = Activity.objects.filter(**filters)

    # Aggregate data
    report_data = activities.values('date').annotate(
        total_views=Sum('views'),
        total_likes=Sum('likes'),
        total_comments=Sum('comments'),
        total_shares=Sum('shares'),
    ).order_by('date')

    return JsonResponse(list(report_data), safe=False)