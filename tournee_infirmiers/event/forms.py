from django.db import models
from django import forms
from .models import Need


class AddNeedForm(forms.Form):
    need_string = forms.CharField(min_length=3, max_length=4, label='Indice du traitement',
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indice du traitement'}))
    date = forms.DateField(label='Date du soin',
                           widget=forms.DateInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Date de début : AAAA-MM-DD'}))
    start = forms.TimeField(label='Début du soin obligatoire (facultatif)',
                            widget=forms.TimeInput(attrs={'class': 'form-control',
                                                          'placeholder': 'HH:MM:SS'}),
                            required=False)
    end = forms.TimeField(label='Fin du soin obligatoire (facultatif)',
                            widget=forms.TimeInput(attrs={'class': 'form-control',
                                                          'placeholder': 'HH:MM:SS'}),
                            required=False)
    duration_heal = forms.DurationField(label='Durée du soin')

    '''def clean(self):
        cleaned_data = super(AddNeedForm, self).clean()
        duration = cleaned_data.get("duration")
        duration_heal = cleaned_data.get("duration_heal")
        if (duration < duration_heal):
            raise forms.ValidationError(
                "Temps insuffisant pour réaliser le traitement"
            )'''
