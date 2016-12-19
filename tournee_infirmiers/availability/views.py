from django.shortcuts import render
from django.shortcuts import redirect

from availability.models import Availability, AvailabilityGroup
from django.contrib.auth.models import User
from user.models import Nurse

from availability.forms import AddAvailabilityForm

# Transactions
from django.db import IntegrityError, transaction

# Create your views here.

# TODO restrict access to nurse
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
					nurse = user.person.nurse
					availability_group = AvailabilityGroup(nurse = nurse, frequency = frequency)
					availability_group.save()
					if frequency == "U":
						availability = Availability(start_date = start_date,
							duration = duration, 
							availability_group = availability_group)
						availability.save()

					print(start_date)
					print(duration.days)
					print(duration.seconds)
					print(frequency)
					return redirect("availability:manage_availability")
			except IntegrityError:
				return render(request, 'availability/manage_availabilities.html', 
					{"add_availability_form": add_availability_form})
			
	else:
		add_availability_form = AddAvailabilityForm()
	return render(request, 'availability/manage_availabilities.html', 
					{"add_availability_form": add_availability_form})