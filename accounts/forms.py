from django import forms
from .models import NewUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ['bio','birthDate']