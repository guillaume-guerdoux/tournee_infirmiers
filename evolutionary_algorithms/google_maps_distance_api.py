import requests
import json
import pprint
import pickle

''' JSON returned by google maps API
    Example : origins = [V, Se]
              destinations = [Sa ,B]
    Json returned J : [ V/S V/B
                        Se/Se Se/B]
'''


def create_distance_matrix(origins=[],
                           destinations=[]):
    origins_str = "|".join(origins)
    destinations_str = "|".join(destinations)
    url = 'http://maps.googleapis.com/maps/api/distancematrix/json?'\
          'origins={0}&'\
          'destinations={1}&'\
          'mode=driving&'\
          'language=en-EN&'\
          'sensor=false'.format(origins_str, destinations_str)
    resp = requests.get(url)
    resp_json = resp.json()
    pprint.pprint(resp_json)
    distance_matrix = []
    for element in resp_json["rows"]:
        row = []
        for value in element['elements']:
            row.append(value["duration"]['value'])
        distance_matrix.append(row)
    return distance_matrix

# Création et enregistrement d'une matrice test (30 patients)

origins=['140 avenue jean jaurès 92290 Chatenay Malabry', '14 rue du Docteur le Savoureux 92290 Chatenay Malabry', '22 rue de Saclay 92290 Chatenay Malabry', '31 rue Yvonne 92330 Bourg-la-Reine', '147 rue de Chalais 94240 L\'Hay-les-Roses', '6 rue de l\'Abbaye 92160 Antony', '120 avenue François Molé 92160 Antony', '44 rue Maurice Ténine 94260 Fresnes', '15 avenue du 8 mai 1945 94260 Fresnes', '10 avenue de la Gare 92330 Sceaux', '4 boulevard du marechal juin 91370 Verrières-le-buisson', '19 allée georges brassens 92290 Chatenay-Malabry', '93 rue du colonel fabien 92160 Antony', '3 rue léo delibes 92330 Sceaux', '20 rue de l\'eglise 91370 verrièes-le-buisson', '29 place des ailantes 92330 Sceaux', '67 boulevard pasteur 94260 Fresnes', '16 rue Eistein 92160 Antony', '5 avenue Sully Prud\'homme 92290 Chatenay Malabry', '18 rue Achille Garnon 92330 Sceaux', '36 rue des grands chênes 91370 Verrières-le-buisson', '4 rue prosper legouté 92160 Antony' '212 avenue du président kennedy 92160 antony', '10 rue boucicaut 92260 Fontenay-aux-roses', '55 rue vincent fayo 92290 Chatenay Malabry', '8 rue jean louis sinet 92330 Sceaux', '21 rue des blagis 92340 Bourg-la-reine', '63 rue de l\'yser 92330 Sceaux', '1 rue le bouvier 92340 Bourg-la-reine', '31 rue delabergerie 92340 Bourg-la-reine', "27 rue de la chrétienté 92330 Sceaux"]
# origins est une liste d'adresses : adresse + code postal + ville
print(len(origins))
test_matrix=create_distance_matrix(origins, origins)

with open('matrix_test', 'wb') as test:
    pickler_test=pickle.Pickler(test)
    pickler_test.dump(test_matrix)