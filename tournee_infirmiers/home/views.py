from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import optimizer.views as opt
from datetime import datetime
import os.path

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return redirect('dashboard/')
    else:
        return render(request, 'home/home.html')


@login_required(redirect_field_name='dashboard')
def dashboard(request):
	now = datetime.now()
	year, month, day = now.year, now.month, now.day
	file_path = opt.get_schedule_file_path(year, month, day)
	if not os.path.isfile(file_path):
		opt.generate_schedule_file(year, month, day)

	return render(request, 'home/dashboard.html')