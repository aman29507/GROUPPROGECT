from django.db import models
from django.conf import settings



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)  # ✅ Make sure this exists
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ Organizer as User

    def __str__(self):
        return self.title
