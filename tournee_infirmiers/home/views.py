from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return redirect('dashboard/')
    else:
        return render(request, 'home/home.html')


@login_required(redirect_field_name='dashboard')
def dashboard(request):
	return render(request, 'home/dashboard.html')
