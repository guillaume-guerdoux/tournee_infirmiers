from django.shortcuts import render
from .forms import PatientForm
from . import models
from datetime import date
from django.contrib.auth.models import User


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


def patient_info(request, id_patient):
    # Create a patient object to be displayed in the template.
    # Need to fetch in from the database once we have a way of creating it.
    try:
        patient = models.Patient.objects.get(user_id=id_patient)
    except models.Patient.DoesNotExist:
        # Pour l'instant si le patient n'existe pas on en crée un fictif pour tester la vue
        patient = models.Patient()
        patient.user = User()
        patient.user.first_name = 'Pierre'
        patient.user.last_name = 'Durand'
        patient.user.email = 'pdurand@domainname.com'
        patient.sex = '1'
        patient.address = '2 avenue Sully Prudhomme, 92295 Châtenay-Malabry'
        patient.profile_type = 'PATIENT'
        patient.birthdate = date(1985, 8, 23)
        patient.information = "Il est gentil."

    return render(request, 'patient/patient_info.html', {'patient': patient})


def patient_list(request):
    # retrieves the list of patients in the database
    patients_list = list(models.Patient.objects.all())

    if len(patients_list) == 0:
        # Temporary patient to fill up the list until we create patients in database
        patient = models.Patient()
        patient.user = User()
        patient.user.first_name = 'Pierre'
        patient.user.last_name = 'Durand'
        patient.user.email = 'pdurand@domainname.com'
        patient.sex = '1'
        patient.address = '2 avenue Sully Prudhomme, 92295 Châtenay-Malabry'
        patient.profile_type = 'PATIENT'
        patient.birthdate = date(1985, 8, 23)
        patient.information = "Il est gentil."
        patient.id = 0

        patients_list.append(patient)

    return render(request, 'patient/patient_list.html', {'patients': patients_list})
