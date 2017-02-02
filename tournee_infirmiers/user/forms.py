import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import RegexValidator


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Mot de passe',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(label='Mot de passe (vérification)',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
    USER_CHOICES = (
        ('1', 'Infirmier',),
        ('2', 'Cabinet',)
    )
    user_type = forms.ChoiceField(widget=forms.RadioSelect, choices=USER_CHOICES, label="Type d'utilisateur")

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Les mots de passe sont différents')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError(
                "Le nom d'utilisateur ne peut contenir que des caractères alphanumériques et underscore")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Le nom d'utilisateur est déjà pris.")


class NurseForm(forms.Form):
    GENDER_CHOICES = (
        ('1', 'Homme',),
        ('2', 'Femme',)
    )

    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES, label="Genre")
    lastname = forms.CharField(max_length=255, label="Nom",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))
    firstname = forms.CharField(max_length=255, label="Prénom",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}))
    birthdate = forms.DateField(label="Date de naissance", input_formats=['%d/%m/%Y'],
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
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}))


class OfficeForm(forms.Form):
    address = forms.CharField(max_length=255, label="Adresse",
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}))
    postcode = forms.CharField(label="Code Postal",
                               validators=[RegexValidator(r'^[0-9]{5}$', 'Entrez un code postal valide')],
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code Postal'}))
    city = forms.CharField(max_length=255, label="Ville",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}))
    geographical_area = forms.IntegerField(label="Rayon géographique couvert",
                                           widget=forms.NumberInput(attrs={
                                               'class': 'form-control',
                                               'placeholder': 'Rayon géographique (en km)'
                                           }))
