from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    """Custom signup form without membership_type."""

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  # ❌ Removed 'membership_type'

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        field_classes = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }
        
        for field, placeholder in field_classes.items():
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': placeholder})
