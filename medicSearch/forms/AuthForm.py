from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
