from django import forms
from .models import Need

class AddNeedForm(forms.ModelForm):
    class Meta:
        model = Need
        fields = '__all__'
