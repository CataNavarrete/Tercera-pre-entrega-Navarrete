from django import forms
from .models import TVSeries

class TVSeriesForm(forms.ModelForm):
    class Meta:
        model = TVSeries
        fields = ['title', 'description', 'rating']
