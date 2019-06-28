from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


# User Registration Form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'password1',
            'password2'
        ]
        
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email has been taken!')
        return email

# User edit Form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User  
        fields = [
            'username',
            'email'
        ]


# User profile edit form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'image'
        ]


