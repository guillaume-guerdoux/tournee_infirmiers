import requests
import pprint
import pickle
import time
from patient.models import Patient

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

def create_distance_matrix():  #origins is a list of strings 'adresse + code postal + ville'

    patients=Patient.objects.all()

    all_addresses = []
    for patient in range(len(patients)):
        all_addresses.append("{} {} {}".format(
            patient.address, patient.postcode, patient.city))
    print (all_addresses)
    distance_matrix = []
    n=len(all_addresses)
    for i in range(n):
        row = []
        for j in range(n):
            time.sleep(5)  #not exceed the API query limit
            address1=all_addresses[i]
            address2=all_addresses[j]
            url = 'http://maps.googleapis.com/maps/api/distancematrix/json?'\
                'origins={0}&'\
                'destinations={1}&'\
                'mode=driving&'\
                'language=en-EN&'\
                'sensor=false'.format(address1, address2)
            resp = requests.get(url)
            resp_json = resp.json()
            pprint.pprint(resp_json)
            for element in resp_json["rows"]:
                for value in element['elements']:
                    row.append(value["duration"]['value'])
        distance_matrix.append(row)

    with open('../general_matrix', 'wb') as matrix:
        pickler_matrix=pickle.Pickler(matrix)
        pickler_matrix.dump(distance_matrix)

print(create_distance_matrix())