from django.shortcuts import render
from .forms import PatientForm

def patient(request):
    form=PatientForm(request.POST or None)
    if form.is_valid():
        sex = form.cleaned_data['sex']
        lastname = form.cleaned_data['lastname']
        firstname = form.cleaned_data['firstname']
        birthdate = form.cleaned_data['birthdate']
        address = form.cleaned_data['address']
        postcode = form.cleaned_data['postcode']
        city = form.cleaned_data['city']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        comments = form.cleaned_data['comments']

        envoi=True

    return render(request, 'patient/new_patient.html', locals())
