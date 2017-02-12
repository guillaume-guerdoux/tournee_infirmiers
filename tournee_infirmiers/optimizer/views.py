from django.shortcuts import redirect
from django.http import HttpResponse
from patient.models import Patient
from event.models import Need
from event.models import Appointment
from user.models import Nurse
from datetime import time, timedelta, datetime, date
from optimizer.models import EvolutionaryOptimizer
import pickle
import time
import requests
import pprint


# Create your views here.


def optimize(request):
    Appointment.objects.filter(start__year=2017,
                               start__month=2,
                               start__day=13).delete()
    # Appointment.objects.filter(start__year=date.today().year,
    #                            start__month=date.today().month,
    #                            start__day=date.today().day).delete()

    # Get nurses
    nurses = Nurse.objects.all()
    nurse_nb = len(nurses)

    # Get heals and associate a number
    needs = Need.objects.all().filter(date__year=2017,
                                      date__month=2,
                                      date__day=13)
    # needs = Need.objects.all().filter(date__year=date.today().year,
    #                                   date__month=date.today().month,
    #                                   date__day=date.today().day)

    heals = []
    dict_heal_needs = {}
    addresses = []
    mandatory_schedules = {}
    heal_duration_vector = []
    if len(needs) == 0:
        return HttpResponse("No need today")
    for index, need in enumerate(needs):
        print(index)
        heals.append(index)
        dict_heal_needs[index] = need
        addresses.append("{} {} {}".format(
            need.patient.address, need.patient.postcode, need.patient.city))
        if need.start is None or need.end is None:
            mandatory_schedules[index] = None
        else:
            mandatory_schedules[index] = (need.start, need.end)
        heal_duration_vector.append(timedelta(minutes=30))

    time_distance_matrix = get_time_distance_matrix_from_adresses(addresses)

    # try:
    evolutionary_optimizer = EvolutionaryOptimizer(
        nurse_nb=nurse_nb,
        heals=heals,
        time_distance_matrix=time_distance_matrix,
        heal_duration_vector=heal_duration_vector,
        mandatory_schedules=mandatory_schedules)
    print("evolutionary_optimizer created")
    optimize_output = evolutionary_optimizer.get_optimize_population()
    print("optimize_output found")
    for i in range(len(optimize_output)):
        nurse = nurses[i]
        for heal_nb in optimize_output[i]:
            heal = dict_heal_needs[heal_nb]
            heal_date = heal.date
            # heal_start = heal.start
            heal_duration = heal.duration_heal
            appointment = Appointment(
                start=heal_date,
                duration=heal_duration, nurse=nurse, need=heal)
            appointment.save()
    return HttpResponse("Done")


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


def create_distance_matrix(request):  # origins is a list of strings 'adresse + code postal + ville'

    patients = Patient.objects.all()

    all_addresses = []
    for patient in patients:
        all_addresses.append("{} {} {}".format(
            patient.address, patient.postcode, patient.city))
    print(all_addresses)
    distance_matrix = []
    n = len(all_addresses)

    for i in range(n):
        row = []
        for j in range(n):
            time.sleep(5)  # not exceed the API query limit
            address1 = all_addresses[i]
            address2 = all_addresses[j]
            url = 'http://maps.googleapis.com/maps/api/distancematrix/json?' \
                  'origins={0}&' \
                  'destinations={1}&' \
                  'mode=driving&' \
                  'language=en-EN&' \
                  'sensor=false'.format(address1, address2)
            resp = requests.get(url)
            resp_json = resp.json()
            pprint.pprint(resp_json)
            for element in resp_json["rows"]:
                for value in element['elements']:
                    row.append(value["duration"]['value'])
        distance_matrix.append(row)

    with open('../general_matrix', 'wb') as matrix:
        pickler_matrix = pickle.Pickler(matrix)
        pickler_matrix.dump(distance_matrix)

    return redirect('/patient/list/?matrix_generated=true')
