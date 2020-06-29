from django import forms
from .models import sumemrPhoto
class createForm(forms.ModelForm):
    class Meta:
        model = sumemrPhoto
        fields = ['title', 'photo']
        """ __all__ """