from django import forms
from django.forms.widgets import DateTimeInput


FREQUENCY_CHOICES = (('U', 'Unique',), ('D', 'Tous les jours',), ('W', 'Toutes les semaines',))
MONTHS = {1: ('Janvier'), 2: ('Février'), 3: ('Mars'), 4: ('Avril'),
          5: ('Mai'), 6: ('Juin'), 7: ('Juillet'), 8: ('Août'),
          9: ('Septembre'), 10: ('Octobre'), 11: ('Novembre'), 12: ('Décembre')}


# TODO : Red border for input when error
class AddAvailabilityForm(forms.Form):
    start_date = forms.DateTimeField(label='A partir de quand êtes-vous disponible ?',
                                     input_formats=['%d/%m/%Y %H:%M'], widget=DateTimeInput)
    duration = forms.DurationField(label='Combien de temps êtes-vous disponible ? (format HH:mm:ss)')
    frequency = forms.ChoiceField(label='Quelle est la fréquence de cette disponibilité ?',
                                  widget=forms.RadioSelect, choices=FREQUENCY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(AddAvailabilityForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs['class'] = 'form-control input-lg'
        self.fields['start_date'].widget.attrs['placeholder'] = 'Début de la disponibilité'
        self.fields['duration'].widget.attrs['class'] = 'form-control input-lg'
        self.fields['duration'].widget.attrs['placeholder'] = "Durée (HH:mm:ss)"

