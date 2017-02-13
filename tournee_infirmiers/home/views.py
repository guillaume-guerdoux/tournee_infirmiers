from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import optimizer.views as opt
from datetime import datetime, timedelta
from user.models import Office, Nurse
from event.models import Need
from optimizer.forms import OptimizerDateForm


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

    form = OptimizerDateForm(None)

    appointments = get_next_appointments(request)

    # Filter most urgent needs : displays all needs needed between today and a week from today.
    most_urgent_needs = Need.objects.filter(
        date__gte=datetime.today()).exclude(date__gte=datetime.today() + timedelta(days=7))

    # print(year, month, day, nurse_id, schedule)
    return render(request, 'home/dashboard.html', {"appointments": appointments,
                                                   "needs": most_urgent_needs,
                                                   "form": form})


# Get the next appointments to display on the dashboards
# handles the different user cases (office or nurse)
def get_next_appointments(request):
    appointments = []
    try:
        office = request.user.office
        for nurse in office.nurse_set.all():
            for appointment in nurse.appointment_set.filter(
                    start__gte=datetime.today()).exclude(start__gte=datetime.today() + timedelta(days=7)):
                patient = appointment.need.patient
                appointments.append((appointment, patient))

    except Office.DoesNotExist:
        try:
            nurse = request.user.nurse
            for appointment in nurse.appointment_set.filter(
                    start__gte=datetime.today()).exclude(start__gte=datetime.today() + timedelta(days=7)):
                patient = appointment.need.patient
                appointments.append((appointment, patient))
        except Nurse.DoesNotExist:
            pass

    appointments = sorted(appointments, key=get_start_time)
    return appointments


def get_start_time(tuple_app_p):
    return tuple_app_p[0].start
