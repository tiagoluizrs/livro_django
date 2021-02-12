from django.forms import ModelForm
from django import forms
from medicSearch.models.Rating import Rating

class MedicRatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'user_rated', 'value', 'opinion']
        widgets = {
            'user': forms.HiddenInput(),
            'user_rated': forms.HiddenInput(),
            'value': forms.NumberInput(attrs={'class': "form-control"}),
            'opinion': forms.Textarea(attrs={'class': "form-control", "rows": 4}),
        }