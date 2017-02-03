from django.db import models
from django import forms
from .models import Need


class AddNeedForm(forms.Form):
    ''' Explanation of fields :
        nedd_string : Type of need
        date : date where needs is to be done
        start / end : If need has to be done in a particular time slot, start
        and end are the times where the heal has to be BEGUN
        duration_heal : Duration of the heal'''
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
