from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    membership_type = forms.ChoiceField(
        choices=CustomUser.MEMBERSHIP_CHOICES,
       widget=forms.Select(attrs={'class': 'form-select'}),
        label='Membership Type'
    )

    class Meta:
        model =CustomUser  # Specify your custom user model
        fields = ['username', 'email', 'password1', 'password2', 'membership_type']  # Fields to include in the form

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # Optionally, customize field attributes here if needed
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

