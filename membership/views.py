from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import Membership

@login_required
def membership_view(request):
    user = request.user

    # Get the user's membership and interests
    membership = Membership.objects.filter(user=user).first()
    interests = membership.interests if membership else []

    return render(request, 'membership/membership.html', {
        'membership': membership,
        'interests': interests,
    })  # Correct path to the template
@login_required
def membership_select(request):
    if request.method == 'POST':
        membership_type = request.POST.get('membership_type')
        interests = request.POST.get('interests', '')  # Get the interests as a string
        user = request.user  # Get the currently logged-in user

        # Save or update the Membership model
        membership, created = Membership.objects.get_or_create(user=user)

        # If membership_type is not already set, update it
        if not membership.membership_type:
            membership.membership_type = membership_type

        # Clean and update the interests field
        new_interests = [interest.strip() for interest in interests.split(',') if interest.strip()]  # Clean and remove empty strings
        if membership.interests:
            # Combine existing and new interests, avoiding duplicates
            membership.interests = list(set(membership.interests + new_interests))
        else:
            membership.interests = new_interests

        # Limit the total number of interests to 5
        membership.interests = membership.interests[:5]
        membership.save()

        return redirect('membership')  # Redirect back to the membership page

    return redirect('membership')   # Redirect back if the request is invalid



@login_required
def save_interests(request):
    if request.method == 'POST':
        interests = request.POST.get('interests')
        user = request.user

        # Save the interests to the user's profile or database
        user.profile.interests = interests  # Assuming you have a `profile` model with an `interests` field
        user.profile.save()

        return redirect('membership')  # Redirect back to the membership page
    

    