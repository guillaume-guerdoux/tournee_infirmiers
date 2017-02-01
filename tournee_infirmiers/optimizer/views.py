from django.shortcuts import render
from django.http import HttpResponse
from patient.models import Patient
from event.models import Need
from user.models import Nurse
from django.http import JsonResponse
import json
from django.core import serializers
from datetime import time, datetime, timedelta
from optimizer.models import EvolutionaryOptimizer
import numpy as np
import os

# Create your views here.


def optimize(request, year, month, day):
    generate_schedule_file(year, month, day)
    return HttpResponse("Done")


def get_schedule_file_path(year, month, day):
    return 'optimizer/schedules/{}_{}_{}'.format(year, month, day)


def generate_schedule_file(year, month, day):
    data = get_data_from_db(year, month, day)

    heal_duration_vector = [timedelta(minutes=30)
                            for i in range(data['nb_needs'])]
    time_distance_matrix = get_time_distance_matrix_from_adresses(data[
                                                                  'addresses'])

    identity = np.identity(data['nb_needs'])
    ones = np.ones(data['nb_needs'])
    time_distance_matrix = ones - identity

    try:
        evolutionary_optimizer = EvolutionaryOptimizer(
            nurse_nb=data['nb_nurses'],
            heal_nb=data['nb_needs'],
            time_distance_matrix=time_distance_matrix,
            heal_duration_vector=heal_duration_vector,
            mandatory_schedules=data['mandatory_schedules'])
        print("evolutionary_optimizer created")
        optimize_output = evolutionary_optimizer.get_optimize_population()
        print("optimize_output found")
        schedules = []
        for i in range(len(optimize_output)):
            schedule = {
                'nurse_id': data['nurses'][i].id,
                'ordered_need_ids': [data['needs'][n].id for n in optimize_output[i]]
            }
            schedules.append(schedule)
    except:
        print("Error")
        schedules = [{'error': True, 'nurse_id': data['nurses'][
            i].id, 'ordered_need_ids': []} for i in range(data['nb_nurses'])]

    with open(get_schedule_file_path(year, month, day), 'w') as outfile:
        json.dump(schedules, outfile)


def get_data_from_db(year, month, day):
    data = {
        'date': datetime(int(year), int(month), int(day)),
        'workday': 8 * 60 * 60,
        'startday': time(8),
        'addresses': {},
        'nurses': {},
        # 'durations': {},
        'mandatory_schedules': {},
        'needs': {},
    }

    needs = Need.objects.all().filter(start_time__year=year,
                                      start_time__month=month,
                                      start_time__day=day)
    nurses = Nurse.objects.all()

    data['nb_nurses'] = len(nurses)
    for i in range(len(nurses)):
        data['nurses'][i] = nurses[i]
    data['nb_patients'] = len(set([need.patient for need in needs]))
    data['nb_needs'] = len(needs)

    # print("{}, {}".format(nb_nurses, nb_patients))
    for i in range(len(needs)):
        need = needs[i]
        data['addresses'][i] = "{} {} {}".format(
            need.patient.address, need.patient.postcode, need.patient.city)
        # data['durations'][i] = need.duration
        data['mandatory_schedules'][i] = (need.start_time.time(
        ), (need.start_time + need.duration).time()) if need.start_time.time() != time() else None
        data['needs'][i] = need

    return data


def get_schedule_for_nurse(nurse_id, year, month, day):
    file_path = get_schedule_file_path(year, month, day)
    if not os.path.isfile(file_path):
        generate_schedule_file(year, month, day)

    with open(get_schedule_file_path(year, month, day), 'r') as outfile:
        schedules = json.load(outfile)

    schedule_list = None
    for s in schedules:
        # print(s, type(s['nurse_id']), int(nurse_id), s['nurse_id'] == int(nurse_id))
        if s['nurse_id'] == nurse_id:
            schedule_list = s

    # print(schedule_list)
    # print([id_need for id_need in schedule_list['ordered_need_ids']])
    return [Need.objects.get(id=id_need) for id_need in schedule_list['ordered_need_ids']] if schedule_list is not None else []


def get_time_distance_matrix_from_adresses(addresses):
    pass
