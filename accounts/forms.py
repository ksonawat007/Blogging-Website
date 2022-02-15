from django import forms
from .models import NewUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username...'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email...'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password...'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'Re-enter password...'})
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ['bio','birthDate']