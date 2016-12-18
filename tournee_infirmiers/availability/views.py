from django.shortcuts import render

from availability.models import Availability, AvailabilityGroup
from django.contrib.auth.models import User
from user.models import Nurse

from availability.forms import AddAvailabilityForm

# Transactions
from django.db import IntegrityError, transaction

# Create your views here.
@transaction.atomic
def manage_availability(request):
	user = request.user
	if request.method == "POST":
		add_availability_form = AddAvailabilityForm(request.POST)
		if add_availability_form.is_valid():
			start_date = add_availability_form.cleaned_data["start_date"]
			duration = add_availability_form.cleaned_data["duration"]
			frequency = add_availability_form.cleaned_data["frequency"]

			try:
				with transaction.atomic():
					print(start_date)
					print(duration)
					print(frequency)
					return redirect("home:home")
			except IntegrityError:
				return render(request, 'availability/manage_availabilities.html', 
					{"add_availability_form": add_availability_form})
			
	else:
		add_availability_form = AddAvailabilityForm()
	return render(request, 'availability/manage_availabilities.html', 
					{"add_availability_form": add_availability_form})