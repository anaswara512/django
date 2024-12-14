from django import forms
from .models import Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields=['firstname','lastname','email','address']
