from django.shortcuts import render

def users_view(request):
    return render(request, 'users/users.html')  # Correct path to the template
