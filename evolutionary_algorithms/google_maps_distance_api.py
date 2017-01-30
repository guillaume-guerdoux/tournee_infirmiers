import requests
import json
import pprint
import pickle
import time

''' JSON returned by google maps API
    Example : origins = [V, Se]
              destinations = [Sa ,B]
    Json returned J : [ V/S V/B
                        Se/Se Se/B]
'''

def create_distance_matrix(origins):  #origins is a list of strings 'adresse + code postal + ville'
    distance_matrix = []
    n=len(origins)
    for i in range(n):
        row = []
        for j in range(n):
            time.sleep(5)  #not exceed the API query limit
            address1=origins[i]
            address2=origins[j]
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
    return distance_matrix