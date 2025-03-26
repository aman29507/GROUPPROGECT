from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, AuthenticationForm  # Use the correct forms
from .models import CustomUser  # Ensure CustomUser is imported
from django.contrib.auth.decorators import login_required

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


