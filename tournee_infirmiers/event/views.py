from django.shortcuts import render
from patient.models import Patient
from .models import Need, Appointment
from .forms import AddNeedForm


def add_need(request, patient_number):
    form = AddNeedForm(request.POST or None)
    current_patient = Patient.objects.get(id=patient_number)
    if form.is_valid():
        need = Need(need_string=form.cleaned_data['need_string'],
                    date=form.cleaned_data['date'],
                    start=form.cleaned_data['start'],
                    end=form.cleaned_data['end'],
                    duration_heal=form.cleaned_data['duration_heal'],
                    patient=current_patient)
        need.save()
        success = True
    return render(request, 'need/add_need.html', locals())


def appointment_detail(request, id_appointment):
    try:
        appointment = Appointment.objects.get(id=id_appointment)
        patient = appointment.need.patient
    except Appointment.DoesNotExist:
        exception_raised = True
    return render(request, 'event/appointment_detail.html', locals())
