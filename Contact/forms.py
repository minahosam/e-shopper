from django import forms
from .models import *
class contactform(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your mail'}))
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter subject'}))
    message=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter message'}))
    class Meta:
        model=contact_info
        fields='__all__'