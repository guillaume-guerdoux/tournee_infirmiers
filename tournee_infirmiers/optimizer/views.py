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
import pickle

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
        'addresses': {},
        'nurses': {},
        # 'durations': {},
        'mandatory_schedules': {},
        'needs': {},
    }

    needs = Need.objects.all().filter(date__year=year,
                                      date__month=month,
                                      date__day=day)
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
        # data['mandatory_schedules'][i] = (need.start_time.time(
        # ), (need.start_time + need.duration).time()) if need.start_time.time() != time() else None
        if need.start is None or need.end is None:
            data['mandatory_schedules'][i] = None
            print("ok")
        else:
            data['mandatory_schedules'][i] = (need.start, need.end)
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
    with open('general_matrix', 'rb') as matrix:
        depickler_test = pickle.Unpickler(matrix)
        all_addresses_matrix = depickler_test.load()

    all_addresses = ['140 avenue jean jaurès 92290 Chatenay Malabry',
                     '14 rue du Docteur le Savoureux 92290 Chatenay Malabry',
                     '22 rue de Saclay 92290 Chatenay Malabry', '31 rue Yvonne 92330 Bourg-la-Reine',
                     '147 rue de Chalais 94240 L\'Hay-les-Roses', '6 rue de l\'Abbaye 92160 Antony',
                     '120 avenue François Molé 92160 Antony', '44 rue Maurice Ténine 94260 Fresnes',
                     '15 avenue du 8 mai 1945 94260 Fresnes', '10 avenue de la Gare 92330 Sceaux',
                     '4 boulevard du marechal juin 91370 Verrières-le-buisson',
                     '19 allée georges brassens 92290 Chatenay-Malabry', '93 rue du colonel fabien 92160 Antony',
                     '3 rue léo delibes 92330 Sceaux', '20 rue de l\'eglise 91370 verrièes-le-buisson',
                     '29 place des ailantes 92330 Sceaux', '67 boulevard pasteur 94260 Fresnes',
                     '16 rue Eistein 92160 Antony', '5 avenue Sully Prud\'homme 92290 Chatenay Malabry',
                     '18 rue Achille Garnon 92330 Sceaux', '36 rue des grands chênes 91370 Verrières-le-buisson',
                     '4 rue prosper legouté 92160 Antony', '212 avenue du président kennedy 92160 antony',
                     '10 rue boucicaut 92260 Fontenay-aux-roses', '55 rue vincent fayo 92290 Chatenay Malabry',
                     '8 rue jean louis sinet 92330 Sceaux', '21 rue des blagis 92340 Bourg-la-reine',
                     '63 rue de l\'yser 92330 Sceaux', '1 rue le bouvier 92340 Bourg-la-reine',
                     '31 rue delabergerie 92340 Bourg-la-reine', "27 rue de la chrétienté 92330 Sceaux"]

    nb_addresses = len(addresses)
    matrix = []
    for i in range(nb_addresses):
        index_i = all_addresses.index(addresses[i])
        line = []
        for j in range(nb_addresses):
            index_j = all_addresses.index(addresses[j])
            line.append(all_addresses_matrix[index_i][index_j])
        matrix.append(line)

    return matrix
