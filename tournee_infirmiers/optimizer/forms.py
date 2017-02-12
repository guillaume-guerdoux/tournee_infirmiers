from django import forms


class OptimizerDateForm(forms.Form):
    date = forms.DateField(label="Date de la tournée à optimiser (si laissé vide, Aujourd'hui par défaut)", input_formats=['%d/%m/%Y'],
                           widget=forms.DateInput(
                                attrs={'class': 'form-control', 'placeholder': 'Date de la tournée'}))
