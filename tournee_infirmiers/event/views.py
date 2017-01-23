from django.shortcuts import render
from patient.models import Patient
from .models import Need
from .forms import AddNeedForm


def add_need(request, patient_number):
    form = AddNeedForm(request.POST or None)
    current_patient = Patient.objects.get(id=patient_number)
    if form.is_valid():
        need = Need(need_string=form.cleaned_data['need_string'],
                    start_time=form.cleaned_data['start_time'],
                    duration=form.cleaned_data['duration'],
                    duration_heal=form.cleaned_data['duration_heal'],
                    patient=current_patient)
        need.save()
        success = True
    return render(request, 'need/add_need.html', locals())
