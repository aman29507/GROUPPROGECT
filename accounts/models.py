from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    """Custom user model with no additional fields."""
    pass  
def __str__(self):
        return self.username# Removed membership_type and MembershipRequest
 # Now it only extends Django's default user


# Create your models here.
