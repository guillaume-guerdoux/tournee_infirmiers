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
def dashboard(request, year=None, month=None, day=None, user_id=None):
    now = datetime.now()
    year = year if year is not None else now.year
    month = month if month is not None else now.month
    day = day if day is not None else now.day

    try:
        nurse_id = int(user_id) if user_id is not None else request.user.nurse.id
        schedule = opt.get_schedule_for_nurse(nurse_id, year, month, day)
    except Exception as e:
        print("EXCEPTION : {}".format(e))
        schedule = []

    # print(year, month, day, nurse_id, schedule)
    return render(request, 'home/dashboard.html')
