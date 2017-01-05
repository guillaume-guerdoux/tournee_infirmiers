from django.shortcuts import render
from django.shortcuts import redirect

from availability.models import Availability, AvailabilityGroup
from django.contrib.auth.models import User
from user.models import Nurse

from availability.forms import AddAvailabilityForm

# Transactions
from django.db import IntegrityError, transaction

# Date 
from datetime import datetime, timedelta
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
			print(frequency)
			nurse = user.person.nurse
			availability_group = AvailabilityGroup(nurse = nurse, frequency = frequency)
			availability_group.save()
			if frequency == "U":
				availability = Availability(start_date = start_date,
					duration = duration, 
					availability_group = availability_group)
				availability.save()
				
			if frequency == "D":
				# TODO : Find a way to add every day long time
				# TODO : Tell user those availabilities are available for one month
				for k in range (1,31):
					start_date_one_day =start_date + timedelta(days=k)
					availability = Availability(start_date = start_date_one_day,
						duration = duration, 
						availability_group = availability_group)
					availability.save()
			if frequency == "W":
				# TODO : Find a way to add every day long time
				# TODO : Tell user those availabilities are available for four month
				for k in range (1,28):
					start_date_one_week =start_date + timedelta(weeks=k)
					availability = Availability(start_date = start_date_one_week,
						duration = duration, 
						availability_group = availability_group)
					availability.save()
			return redirect("availability:manage_availability")
	else:
		add_availability_form = AddAvailabilityForm()
		availabilities = Availability.objects.filter(availability_group__nurse = user.person.nurse)
	return render(request, 'availability/manage_availabilities.html', 
					{"add_availability_form": add_availability_form, 
					"availabilities": availabilities})


def remove_unique_availability(request):
	if(request.is_ajax()):
		if request.method == "POST":
			id_availability = request.POST["remove-unique-availability-id"]
			availability = Availability.objects.get(id = id_availability)
			availability_group = availability.availability_group
			connected_user = request.user
			user_owner = availability_group.nurse.user
			if(user_owner == connected_user):
				if availability_group.frequency == "U":
					availability_group.delete()
				else:
					availability.delete()
				return HttpResponse("Availability removed")
			else:
				return HttpResponse("Not user availability") 
		else:
			return HttpResponse("Not Post") 
			#return render(request, 'service/add_services_register.html')
	else:
		return HttpResponse("Not ajax") 