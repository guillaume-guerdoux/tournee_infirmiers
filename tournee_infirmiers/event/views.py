from django.shortcuts import render
from .models import Need
from .forms import AddNeedForm


def add_need(request):
    form = AddNeedForm(request.POST or None)
    if form.is_valid():
        isValid = True
        need = Need(start_time=form.cleaned_data['start_time'], duration=form.cleaned_data['duration'])
        need.save()
    return render(request, 'need/add_need.html', locals())
