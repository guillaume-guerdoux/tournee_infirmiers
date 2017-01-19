from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login


def error_login(request):
    return render(request, 'user/error_login.html')


@login_required(redirect_field_name='account')
def account(request):
    return render(request, 'user/account.html', {'user': request.user})


@csrf_exempt
def register(request):
    invalid_form = False
    user_form = RegistrationForm(request.POST or None)
    if user_form.is_valid():
        user = User.objects.create_user(username=user_form.cleaned_data['username'],
                                            password=user_form.cleaned_data['password1'],
                                            email=user_form.cleaned_data['email'])
        user.save()

        user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password1'])
        login(request, user)
        if user_form.cleaned_data['user_type'] == '1':
            return redirect('user:new_nurse')
        else:
            return redirect('user:create_office')
    elif request.method == 'POST':
        invalid_form = True

    variables = RequestContext(request, {'form': user_form, 'invalid_form': invalid_form})
    return render_to_response('user/register.html', variables)


def nurse(request):
    form = NurseForm(request.POST or None, initial={'email': request.user.email})
    new_nurse = Nurse()
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

        new_nurse.user = request.user

        new_nurse.save()
        success = True

    return render(request, 'user/new_nurse.html', locals())


def register_success(request):
    return render_to_response(
        'user/success.html',
        context=RequestContext(request)
    )


def edit_self_info(request):
    nurse_to_edit = request.user.nurse
    edit = True
    form = NurseForm(request.POST or None, initial={
            'sex': nurse_to_edit.sex,
            'lastname': nurse_to_edit.last_name,
            'firstname': nurse_to_edit.first_name,
            'birthdate': nurse_to_edit.birthdate,
            'address': nurse_to_edit.address,
            'postcode': nurse_to_edit.postcode,
            'city': nurse_to_edit.city,
            'email': nurse_to_edit.email,
            'phone': nurse_to_edit.phone,
        })

    if form.is_valid():
        nurse_to_edit.sex = form.cleaned_data['sex']
        nurse_to_edit.last_name = form.cleaned_data['lastname']
        nurse_to_edit.first_name = form.cleaned_data['firstname']
        nurse_to_edit.birthdate = form.cleaned_data['birthdate']
        nurse_to_edit.address = form.cleaned_data['address']
        nurse_to_edit.postcode = form.cleaned_data['postcode']
        nurse_to_edit.city = form.cleaned_data['city']
        nurse_to_edit.email = form.cleaned_data['email']
        nurse_to_edit.phone = form.cleaned_data['phone']

        nurse_to_edit.save()
        success = True

    return render(request, 'user/new_nurse.html', locals())


def create_office(request):
    form = OfficeForm(request.POST or None)
    office = Office()
    if form.is_valid():
        office.address = form.cleaned_data['address']
        office.postcode = form.cleaned_data['postcode']
        office.city = form.cleaned_data['city']
        office.geographical_area = form.cleaned_data['geographical_area']

        office.user = request.user

        office.save()
        success = True

    return render(request, 'user/new_office.html', locals())


def edit_office_info(request):
    office_to_edit = request.user.office
    edit = True
    form = OfficeForm(request.POST or None, initial={
        'address' : office_to_edit.address,
        'postcode': office_to_edit.postcode,
        'city': office_to_edit.city,
        'geographical_area': office_to_edit.geographical_area
    })

    if form.is_valid():
        office_to_edit.address = form.cleaned_data['address']
        office_to_edit.postcode = form.cleaned_data['postcode']
        office_to_edit.city = form.cleaned_data['city']
        office_to_edit.geographical_area = form.cleaned_data['geographical_area']

        office_to_edit.user = request.user

        office_to_edit.save()
        success = True

    return render(request, 'user/new_office.html', locals())
