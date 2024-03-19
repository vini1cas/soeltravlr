from django import forms
from .models import Travel, Comment

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ('title', 'body', 'season', 'travel_date', 'rating')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'season' : forms.Select(attrs={'class': 'form-control'}),
            'travel_date' : forms.TextInput(attrs={'class': 'form-control'}),
            'rating' : forms.Select(attrs={'class': 'form-control'})
        }