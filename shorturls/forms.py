from django import forms
from .models import short_urls
from.shortener import shortener
class URLForm(forms.ModelForm):
    long_url = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Enter URL'
    }))
    short_url = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Enter Short URL',
    }),required=False)

    class Meta:
        model = short_urls
        fields = ('long_url',)