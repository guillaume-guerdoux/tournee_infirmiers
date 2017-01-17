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

origins=['140 avenue jean jaurès 92290 Chatenay Malabry', '14 rue du Docteur le Savoureux 92290 Chatenay Malabry', '22 rue de Saclay 92290 Chatenay Malabry']
# origins est une liste d'adresses : adresse + code postal + ville
print(len(origins))
test_matrix=create_distance_matrix(origins, origins)

with open('matrix_test', 'wb') as test:
    pickler_test=pickle.Pickler(test)
    pickler_test.dump(test_matrix)