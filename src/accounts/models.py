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
class Content(models.Model):
    TYPE_CHOICES = [
        ('article', 'Article'),
        ('video', 'Video'),
        ('webinar', 'Webinar'),
    ]
    
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Activity(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.content.title} - {self.date}"
    class CustomUser(AbstractUser):
    pass  # Extend if needed