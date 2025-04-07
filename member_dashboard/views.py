from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages

def home_view(request):
        return render(request, 'base.html')

def member_dashboard(request):
        return render(request, 'member_dashboard.html')

# @login_required 
# def profile_view(request):
#     user = request.user
#     if request.method == 'POST':
#         new_email = request.POST.get('email')  # Get the new email from the form
#         if new_email:
#             user.email = new_email  # Update the email
#             user.save()  # Save the changes to the database
#             messages.success(request, 'Your email has been updated successfully!')
#             return redirect('profile')  # Redirect to the profile page
#         else:
#             messages.error(request, 'Invalid email address.')
#     return render(request, 'profile.html', {'user': user})

@login_required
def profile_view(request):
    user = request.user  # Get the logged-in user's details

    if request.method == 'POST':
        new_email = request.POST.get('email')  # Get the new email from the form
        if new_email:
            if new_email == user.email:  # Check if the new email is the same as the current email
                return JsonResponse({'message': 'The new email is the same as the current email. No changes made.'}, status=400)
            else:
                user.email = new_email  # Update the email
                user.save()  # Save the changes to the database
                return JsonResponse({'message': 'Your email has been updated successfully!'}, status=200)

    return render(request, 'profile.html', {'user': user})
# def events_view(request):
#     return render(request, 'events.html')

# def achievements_view(request):
#     return render(request, 'achievements.html')

     
def benefits_view(request):
    return render(request, 'benefits.html')


# def community_involvement_view(request):
    # return render(request, 'community_involvement.html')
