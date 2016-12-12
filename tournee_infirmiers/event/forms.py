from django import forms


class AddNeedForm(forms.Form):
    startTime = forms.DateTimeField()
