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
        # Get the new values from the form
        new_email = request.POST.get('email')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_membership_type = request.POST.get('membership_type')

        # Update email if it has changed
        if new_email:
            if new_email == user.email:
                return JsonResponse({'message': 'The new email is the same as the current email. No changes made.'}, status=400)
            else:
                user.email = new_email  # Update the email
                user.save()

        # Update first name if it has changed
        if new_first_name and new_first_name != user.first_name:
            user.first_name = new_first_name  # Update the first name
            user.save()

        # Update last name if it has changed
        if new_last_name and new_last_name != user.last_name:
            user.last_name = new_last_name  # Update the last name
            user.save()

        return JsonResponse({'message': 'Your profile has been updated successfully!'}, status=200)

    return render(request, 'profile.html', {'user': user})
# def events_view(request):
#     return render(request, 'events.html')

# def achievements_view(request):
#     return render(request, 'achievements.html')

     

# def benefits_view(request):
#     return render(request, 'benefits.html')

def benefits_view(request):
    user = request.user  # Assuming `user` object contains the membership_type field
    return render(request, 'benefits.html', {'user': user})

# def community_involvement_view(request):
    # return render(request, 'community_involvement.html')