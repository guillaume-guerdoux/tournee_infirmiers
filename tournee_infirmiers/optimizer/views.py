from django.shortcuts import render
from django.http import HttpResponse
from patient.models import Patient
from event.models import Need
from user.models import Nurse
from django.http import JsonResponse
import json
from django.core import serializers
from datetime import time, datetime

# Create your views here.

def optimize(request, year, month, day):
	''' 
		K : nb_nurses
		P : 
		T : 
		D : 
		N : workday
		h : startday
		mandatory_schedule : mandatory_schedule 
	'''
	# year, month, day = 2017, 1, 17

	data = {
		'date': datetime(int(year), int(month), int(day)),
		'workday': 8 * 60 * 60,
		'startday': time(8),
		'addresses': {},
		'durations': {},
		'mandatory_schedules': {}
	}

	needs = Need.objects.all().filter(start_time__year=year,
					                  start_time__month=month, 
                         			  start_time__day=day)
	nurses = Nurse.objects.all()

	data['nb_nurses'] = len(nurses)
	data['nb_patients'] = len(set([need.patient for need in needs]))
	data['nb_needs'] = len(needs)

	# print("{}, {}".format(nb_nurses, nb_patients))
	for i in range(len(needs)):
		need = needs[i]
		data['addresses'][i] = "{} {} {}".format(need.patient.address, need.patient.postcode, need.patient.city)
		data['durations'][i] = need.duration
		data['mandatory_schedules'][i] = (need.start_time.time(), (need.start_time + need.duration).time()) if need.start_time.time() != time() else None


	print(data)
	
	# data = serializers.serialize('json', needs)
	return HttpResponse(data, content_type="application/json")