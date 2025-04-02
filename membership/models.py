from django.db import models
from django.conf import settings
# Create your models here.
class Membership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Reference the custom user model
    interests = models.JSONField(default=list)  # Store interests as a list (requires Django 3.1+)
    membership_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.membership_type}"