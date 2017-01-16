from django.shortcuts import render, redirect
from .forms import PatientForm
from . import models
from datetime import date


def new_patient(request):
    form = PatientForm(request.POST or None)
    new_patient = models.Patient()
    if form.is_valid():
        new_patient.sex = form.cleaned_data['sex']
        new_patient.last_name = form.cleaned_data['lastname']
        new_patient.first_name = form.cleaned_data['firstname']
        new_patient.birthdate = form.cleaned_data['birthdate']
        new_patient.address = form.cleaned_data['address']
        new_patient.postcode = form.cleaned_data['postcode']
        new_patient.city = form.cleaned_data['city']
        new_patient.email = form.cleaned_data['email']
        new_patient.phone = form.cleaned_data['phone']
        new_patient.information = form.cleaned_data['comments']

        new_patient.save()
        success = True

    return render(request, 'patient/new_patient.html', locals())


def patient_info(request, id_patient):
    # Create a patient object to be displayed in the template.
    # Need to fetch in from the database once we have a way of creating it.
    try:
        patient = models.Patient.objects.get(id=id_patient)
    except models.Patient.DoesNotExist:
        # Pour l'instant si le patient n'existe pas on en crée un fictif pour tester la vue
        patient = models.Patient()
        patient.first_name = 'Pierre'
        patient.last_name = 'Durand'
        patient.email = 'pdurand@domainname.com'
        patient.sex = '1'
        patient.address = '2 avenue Sully Prudhomme'
        patient.postcode = 92295
        patient.city = 'Châtenay-Malabry'
        patient.profile_type = 'PATIENT'
        patient.birthdate = date(1985, 8, 23)
        patient.information = "ATTENTION ! Ce patient est un placeholder" \
                              " pour vous donner une idée de l'aspect de cette page." \
                              " Si vous voyez ce patient cela veut dire " \
                              "qu'il n'y en a aucun d'enregistré dans votre base de données."

    return render(request, 'patient/patient_info.html', {'patient': patient})


def patient_list(request):
    # retrieves the list of patients in the database
    patients_list = list(models.Patient.objects.all())

    if len(patients_list) == 0:
        # Temporary patient to fill up the list until we create patients in database
        patient = models.Patient()
        patient.first_name = 'Pierre'
        patient.last_name = 'Durand'
        patient.email = 'pdurand@domainname.com'
        patient.sex = '1'
        patient.address = '2 avenue Sully Prudhomme'
        patient.postcode = 92295
        patient.city = 'Châtenay-Malabry'
        patient.profile_type = 'PATIENT'
        patient.birthdate = date(1985, 8, 23)
        patient.information = "ATTENTION ! Ce patient est un placeholder" \
                              " pour vous donner une idée de l'aspect de cette page." \
                              " Si vous voyez ce patient cela veut dire " \
                              "qu'il n'y en a aucun d'enregistré dans votre base de données."
        patient.id = 0

        patients_list.append(patient)

    return render(request, 'patient/patient_list.html', {'patients': patients_list})


def delete_patient(request, id_patient):
    # removes a patient from the database
    try:
        patient_to_remove = models.Patient.objects.get(id=id_patient)
        patient_to_remove.delete()

        return redirect('patient:patient_list')
    except models.Patient.DoesNotExist:
        return redirect('patient:patient_list')
