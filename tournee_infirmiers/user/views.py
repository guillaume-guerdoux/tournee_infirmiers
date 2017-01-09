from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def error_login(request):
    return render(request, 'user/error_login.html')


@login_required(redirect_field_name='account')
def account(request):
    return render(request, 'user/account.html', {'user': request.user})
