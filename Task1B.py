"""Requirements for Task 1B"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from haversine import haversine
from floodsystem.utils import sorted_by_key  # noqa


### This is the same function as in geo.py, but modified to have TOWNS and not STATION ###
def towns_by_distance(stations, p):
  towns1 = []  #Empty list for town and distance tupples
  for station in stations:
    distance = haversine(station.coord, p)
    y = (station.town, distance) # Defines a new tupple for every town
    towns1.append(y) # Adds that tupple to list1
    #z = sorted_by_key(towns1, 1)
  return sorted_by_key(towns1, 1)

def demonstration():
    # Defines the coordinates of the city center of Cambridge
    cambridge_coord = (52.2053, 0.1218)

    # List of all the stations, with distance, ordered from closest to furthest from Cambridge
    list2 = stations_by_distance(build_station_list(), cambridge_coord)

    # List of all the towns, with distance, ordered from closest to furthest from Cambridge
    t = towns_by_distance(build_station_list(), cambridge_coord)

    list3 = []  # Empty list that will contain the final result
    i = 0 # In order to iterate through the list of towns "t" (there must be a much simpler way but this makes sense to me)
    
    # Iterates through the list of stations, and adds a tupple to list 3 every time, adding the Towns at the same time
    for j in list2:
        name = j[0]
        distance = j[1]
        list3.append((name, t[i][0], distance))
        i += 1
    return list3[:10], list3[-10:]

print(demonstration())