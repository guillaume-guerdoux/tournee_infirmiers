from django import forms

class PatientForm(forms.Form):
    GENDER_CHOICES = (
        ('1', 'Homme',),
        ('2', 'Femme',)
    )

    sex = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENDER_CHOICES, label="Genre")
    lastname = forms.CharField(max_length=255, label="Nom")
    firstname = forms.CharField(max_length=255, label="Prénom")
    birthdate = forms.DateField(widget=forms.DateInput, label="Date de naissance")
    address = forms.CharField(max_length=255, label="Adresse")
    postcode = forms.IntegerField(label="Code Postal")
    city = forms.CharField(max_length=255, label="Ville")
    email = forms.CharField(max_length=255, label="Email")
    phone = forms.IntegerField(label="Numéro de téléphone")
    comments = forms.CharField(widget=forms.Textarea, label="Remarques")