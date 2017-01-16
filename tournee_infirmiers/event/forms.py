from django.db import models
from django import forms
from .models import Need


class AddNeedForm(forms.Form):
    need_string = forms.CharField(min_length=3, max_length=4, label='Indice du traitement')
    start_time = forms.DateTimeField(label='Date et heure de début')
    duration = forms.DurationField(label='Durée')
