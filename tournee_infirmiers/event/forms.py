from django.db import models
from django import forms
from .models import Need


class AddNeedForm(forms.Form):
    need_string = forms.CharField(min_length=3, max_length=4, label='Indice du traitement',
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indice du traitement'}))
    start_time = forms.DateTimeField(label='Date et heure de début',
                                     widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date et heure de début'}))
    duration_heal = forms.DurationField(label='Durée du soin')
    duration = forms.DurationField(label='Durée de la disponibilité')

    def clean(self):
        cleaned_data = super(AddNeedForm, self).clean()
        duration = cleaned_data.get("duration")
        duration_heal = cleaned_data.get("duration_heal")
        if (duration < duration_heal):
            raise forms.ValidationError(
                "Temps insuffisant pour réaliser le traitement"
            )
