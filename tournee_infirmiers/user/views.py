from .forms import *
from . import models
from .models import *
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


def error_login(request):
    return render(request, 'user/error_login.html')


@login_required(redirect_field_name='account')
def account(request):
    return render(request, 'user/account.html', {'user': request.user})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect('success/')
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('user/register.html', variables)


def nurse(request):
    form = NurseForm(request.POST or None)
    new_nurse = models.Nurse()
    if form.is_valid():
        new_nurse.sex = form.cleaned_data['sex']
        new_nurse.last_name = form.cleaned_data['lastname']
        new_nurse.first_name = form.cleaned_data['firstname']
        new_nurse.birthdate = form.cleaned_data['birthdate']
        new_nurse.address = form.cleaned_data['address']
        new_nurse.postcode = form.cleaned_data['postcode']
        new_nurse.city = form.cleaned_data['city']
        new_nurse.email = form.cleaned_data['email']
        new_nurse.phone = form.cleaned_data['phone']

        new_nurse.save()
        success = True

    return render(request, 'user/new_nurse.html', locals())


def register_success(request):
    return render_to_response(
        'user/success.html',
        context=RequestContext(request)
    )