import requests
import json
import pprint

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
            row.append(value["distance"]['value'])
        distance_matrix.append(row)
    return distance_matrix
if __name__ == "__main__":
    print(create_distance_matrix(origins=["Vancouver BC", "Seattle"],
                                 destinations=["San Francisco",
                                               "Victoria BC"]))
