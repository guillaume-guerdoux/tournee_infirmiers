from django.shortcuts import render
from .forms import AddNeedForm


def add_need(request):
    form = AddNeedForm(request.POST or None)
    if form.is_valid():
        isValid = True
        form.save()
    return render(request, 'need/add_need.html', locals())
