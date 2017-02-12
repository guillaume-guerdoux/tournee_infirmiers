from django import forms


class OptimizerDateForm(forms.Form):
    date = forms.DateField(label="Date de la tournée à optimiser", widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Date de la tournée'}))
