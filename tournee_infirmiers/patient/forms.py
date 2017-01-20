from django import forms
from django.core.validators import RegexValidator


class PatientForm(forms.Form):
    GENDER_CHOICES = (
        ('1', 'Homme',),
        ('2', 'Femme',)
    )

    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES, label="Genre")
    lastname = forms.CharField(max_length=255, label="Nom",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))
    firstname = forms.CharField(max_length=255, label="Prénom",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}))
    birthdate = forms.DateField(label="Date de naissance",
                                widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de naissance'}))
    address = forms.CharField(max_length=255, label="Adresse",
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}))
    postcode = forms.CharField(label="Code Postal",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code Postal'}),
                               validators=[RegexValidator(r'^[0-9]{5}$', 'Entrez un code postal valide')])
    city = forms.CharField(max_length=255, label="Ville",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}))
    email = forms.CharField(max_length=255, label="Email",
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.CharField(max_length=255, label="Numéro de téléphone",
                            validators=[RegexValidator(r'^0[0-9]([ .-]?[0-9]{2}){4}$',
                                                       'Entrez un numéro de téléphone valide (et commençant par 0).')],
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}))
    comments = forms.CharField(label="Remarques", required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Remarques'}))
