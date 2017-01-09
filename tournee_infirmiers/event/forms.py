from django.db import models
from django import forms
from .models import Need


class AddNeedForm(forms.Form):
    start_time = forms.DateTimeField()
    duration = forms.DurationField()
