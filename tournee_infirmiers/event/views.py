from django.shortcuts import render
from .forms import AddNeedForm


def add_need(request):
    form = AddNeedForm(request.POST or None)
    if form.is_valid():
        startTime = form.cleaned_data['startTime']
        isValid = True
    return render(request, 'need/add_need.html', locals())
