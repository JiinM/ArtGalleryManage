from django import forms
from .models import Exhibits

class ExhibitForm(forms.ModelForm):
    class Meta:
        model = Exhibits
        fields = ['artist', 'title', 'date', 'description', 'capacity']
