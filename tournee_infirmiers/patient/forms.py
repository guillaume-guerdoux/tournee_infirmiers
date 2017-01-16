from django import forms
from django.core.validators import RegexValidator


class PatientForm(forms.Form):
    GENDER_CHOICES = (
        ('1', 'Homme',),
        ('2', 'Femme',)
    )

    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES, label="Genre")
    lastname = forms.CharField(max_length=255, label="Nom")
    firstname = forms.CharField(max_length=255, label="Prénom")
    birthdate = forms.DateField(widget=forms.DateInput, label="Date de naissance")
    address = forms.CharField(max_length=255, label="Adresse")
    postcode = forms.CharField(label="Code Postal",
                               validators=[RegexValidator(r'^[0-9]{5}$', 'Entrez un code postal valide')])
    city = forms.CharField(max_length=255, label="Ville")
    email = forms.CharField(widget=forms.EmailInput, max_length=255, label="Email")
    phone = forms.CharField(max_length=255, label="Numéro de téléphone",
                            validators=[RegexValidator(r'^0[0-9]([ .-]?[0-9]{2}){4}$',
                                                       'Entrez un numéro de téléphone valide (et commençant par 0).')])
    comments = forms.CharField(widget=forms.Textarea, label="Remarques", required=False)
