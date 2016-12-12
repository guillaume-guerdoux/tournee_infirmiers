from django.shortcuts import render
from . import models
from datetime import date
from django.contrib.auth.models import User


def patient_info(request):
    # Create a patient object to be displayed in the template.
    # Need to fetch in from the database once we have a way of creating it.
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

    return render(request, 'user/patient_info.html', {'patient': patient})
