from django.forms import ModelForm
from django import forms
from medicSearch.models.Profile import Profile
from django.contrib.auth.models import User

class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'role', 'birthday', 'image']
        widgets = {
            'user': forms.HiddenInput(),
            'role': forms.Select(attrs={'class': "form-control"}),
            'birthday': forms.DateInput(attrs={'class': "form-control"}),
            'image': forms.FileInput(attrs={'class': "form-control"})
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"})
        }
