from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register CustomUser model with Django's built-in UserAdmin
admin.site.register(CustomUser, UserAdmin)
