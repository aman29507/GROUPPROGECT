from django.db import models

# Create your models here.

class LandingContent(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='landing_images/', null=True, blank=True)

    def __str__(self):
        return self.title

