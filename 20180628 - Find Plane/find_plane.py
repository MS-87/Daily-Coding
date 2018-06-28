"""
We want to find the closest airborne aeroplane to any given position in North America or Europe. To assist in this we can use an API which will give us the data on all currently airborne commercial aeroplanes in these regions.

OpenSky's Network API can return to us all the data we need in a JSON format.
https://opensky-network.org/api/states/all
From this we can find the positions of all the planes and compare them to our given position.
Use the basic Euclidean distance in your calculation.
"""

import urllib.request
import json
import math

def retrieve_all_planes():
    '''
    Return list of all airplanes in the world
    '''
    all_planes = json.loads(urllib.request.urlopen("https://opensky-network.org/api/states/all").read())['states']
    return all_planes
    
def get_distance(lat_a, long_a, lat_b, long_b):
    '''
    calculate distance between two points
    '''
    distance = math.sqrt((lat_a - lat_b)**2 + (long_a - long_b)**2)

    return distance

def find_nearest_plane(my_lat, my_long):
    '''
    find nearest airplane
    '''
    all_planes = retrieve_all_planes()
    closest = [[None],999999]

    for plane in all_planes:
        if plane[5] and plane[6]:
            distance = get_distance(my_lat, my_long, plane[6], plane[5])
            if distance < closest[1]:
                closest = [plane, distance]
        
    print("Distance: {} Km".format(closest[1]*100))
    print("Callsign: {}".format(closest[0][1]))
    print("Lat/Long: {}, {}".format(closest[0][6], closest[0][5]))
    print("Altitude: {}".format(closest[0][7]))
    print("Country : {}".format(closest[0][2]))
    print("Velocity: {}".format(closest[0][9]))
    print("Vert rat: {}".format(closest[0][11]))
    print("Grounded: {}".format(closest[0][8]))
    

find_nearest_plane( 39, -104) #My lat long redacted for privacy