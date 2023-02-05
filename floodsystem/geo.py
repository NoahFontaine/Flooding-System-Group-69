# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from utils import sorted_by_key  # noqa
from haversine import haversine

### Part of 1B - Stations sorted by distance from coordinate ###

def stations_by_distance(stations, p):
  list1 = []  # Empty List
  for station in stations:
    distance = haversine(station.coord, p)
    x = (station.name, distance) # Defines a new tupple for every station
    list1.append(x) # Adds that tupple to list1
  return sorted_by_key(list1, 1) # Returns sorted list1 by 2nd element (distance)


### Part of 1C - Stations within a specific radius of a center coordinate ###

def stations_within_radius(stations, centre, r):
  l = []   # Empty list that will contain the output with all the correct stations
  for station in stations:
    distance = haversine(station.coord, centre) # Computes the distance of the station from the given centre coordinate
    if distance < r:
      l.append(station.name) # Adds the station name of the station if distance < given max radius
  return l  # Returns list of all the stations

### Part of 1D ###
def rivers_with_station(stations):
  rivers = []
  for station in stations:
    rivers.append(station.river)
  return set(rivers) # Returns set of all stations with river

def stations_by_river(stations):
  dict = {}
  for station in stations:
    dict[station.river] += station.name
  return dict # Returns dictionary of stations by river
  
  
### Part of 1E ###
def rivers_by_station_number(stations, N):
  list = [] # Empty list
  for station in stations:
    list.append(station.river,)

