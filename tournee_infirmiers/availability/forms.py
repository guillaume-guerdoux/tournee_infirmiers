from django import forms
from django.forms import extras
from django.forms.widgets import HiddenInput, DateTimeInput

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from datetime import datetime, date, time, timedelta

FREQUENCY_CHOICES = (('U', 'Unique',), ('D', 'Tous les jours',), ('W', 'Toutes les semaines',))
MONTHS = {1:('Janvier'), 2:('Février'), 3:('Mars'), 4:('Avril'),
	5:('Mai'), 6:('Juin'), 7:('Juillet'), 8:('Août'),
	9:('Septembre'), 10:('Octobre'), 11:('Novembre'), 12:('Décembre')}


# TODO : Red border for input when error
class AddAvailabilityForm(forms.Form):
	start_date = forms.DateTimeField(input_formats = ['%d/%m/%Y %H:%M'], widget=DateTimeInput)
	duration = forms.DurationField()
	frequency =  forms.ChoiceField(widget=forms.RadioSelect, choices=FREQUENCY_CHOICES)
	def __init__(self, *args, **kwargs):
		super(AddAvailabilityForm, self).__init__(*args, **kwargs)
		self.fields['start_date'].widget.attrs['class'] = 'form-control input-lg'
		self.fields['start_date'].widget.attrs['placeholder'] = 'JJ/MM/YYYY HH:MM'
		self.fields['duration'].widget.attrs['class'] = 'form-control input-lg'
		self.fields['duration'].widget.attrs['placeholder'] = "HH:MM:SS"
		#self.fields['duration'].widget.attrs['value'] = str(timedelta(hours=10))
