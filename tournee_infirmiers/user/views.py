from django.shortcuts import render
from django.contrib.auth.models import User


def error_login(request):
    return render(request, 'user/error_login.html')

